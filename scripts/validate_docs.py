#!/usr/bin/env python3
"""Validate repository links and SVG assets without third-party Python packages."""

from __future__ import annotations

import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\((<[^>]+>|[^)\s]+)(?:\s+[^)]*)?\)")
REFERENCE_LINK = re.compile(r"^\s*\[[^\]]+\]:\s*(<[^>]+>|\S+)", re.MULTILINE)
HEADING = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$", re.MULTILINE)
HTML_ID = re.compile(r"\bid=[\"']([^\"']+)[\"']")
EXTERNAL_TIMEOUT_SECONDS = 20


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not any(part in {".git", "node_modules"} for part in path.parts)
    )


def heading_slugs(text: str) -> set[str]:
    counts: dict[str, int] = {}
    result: set[str] = set()
    for _, heading in HEADING.findall(text):
        value = re.sub(r"`([^`]+)`", r"\1", heading)
        value = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", value)
        value = re.sub(r"<[^>]+>", "", value)
        value = value.lower().strip()
        value = re.sub(r"[^\w\-\s]", "", value, flags=re.UNICODE)
        slug = re.sub(r"\s+", "-", value).strip("-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(slug if count == 0 else f"{slug}-{count}")
    result.update(HTML_ID.findall(text))
    return result


def extract_links(text: str) -> list[str]:
    links = [match.group(1).strip("<>") for match in MARKDOWN_LINK.finditer(text)]
    links.extend(match.strip("<>") for match in REFERENCE_LINK.findall(text))
    return links


def verify_external(url: str) -> str | None:
    headers = {"User-Agent": "GRIMM-HOMELAB-documentation-link-check/1.0"}
    request = urllib.request.Request(url, headers=headers, method="HEAD")
    try:
        with urllib.request.urlopen(request, timeout=EXTERNAL_TIMEOUT_SECONDS) as response:
            if response.status >= 400:
                return f"HTTP {response.status}"
            return None
    except urllib.error.HTTPError as error:
        if error.code not in {403, 405, 429, 501}:
            return f"HTTP {error.code}"
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        return f"request failed: {error}"

    # Some hosts reject HEAD while allowing GET. Request only a small byte range.
    headers["Range"] = "bytes=0-0"
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=EXTERNAL_TIMEOUT_SECONDS) as response:
            if response.status >= 400:
                return f"HTTP {response.status}"
            response.read(1)
            return None
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, OSError) as error:
        status = getattr(error, "code", None)
        return f"HTTP {status}" if status else f"request failed: {error}"


def validate_svg(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        root = ET.parse(path).getroot()
    except (ET.ParseError, OSError) as error:
        return [f"{path.relative_to(ROOT)}: invalid SVG/XML: {error}"]

    if root.tag != "{http://www.w3.org/2000/svg}svg":
        errors.append(f"{path.relative_to(ROOT)}: root element must be SVG")
    if not root.attrib.get("viewBox"):
        errors.append(f"{path.relative_to(ROOT)}: viewBox is required")
    for dimension in ("width", "height"):
        if not root.attrib.get(dimension):
            errors.append(f"{path.relative_to(ROOT)}: {dimension} is required")

    for node in root.iter():
        tag = node.tag.rsplit("}", 1)[-1].lower()
        if tag in {"script", "foreignobject", "iframe", "object", "embed"}:
            errors.append(f"{path.relative_to(ROOT)}: active element <{tag}> is not allowed")
        for attribute, value in node.attrib.items():
            local_name = attribute.rsplit("}", 1)[-1].lower()
            if local_name.startswith("on"):
                errors.append(f"{path.relative_to(ROOT)}: event handler '{local_name}' is not allowed")
            if local_name in {"href", "src"} and re.match(r"\s*(https?:|data:|javascript:)", value, re.I):
                errors.append(f"{path.relative_to(ROOT)}: external or executable asset reference is not allowed")
    return errors


def validate_links() -> tuple[list[str], int, int]:
    errors: list[str] = []
    internal_count = 0
    external_count = 0
    contents = {path: path.read_text(encoding="utf-8") for path in markdown_files()}
    slugs = {path: heading_slugs(text) for path, text in contents.items()}
    external_seen: set[str] = set()

    for source, text in contents.items():
        for destination in extract_links(text):
            parsed = urllib.parse.urlsplit(destination)
            if parsed.scheme.lower() in {"http", "https"}:
                external_count += 1
                if destination not in external_seen:
                    external_seen.add(destination)
                    error = verify_external(destination)
                    if error:
                        errors.append(f"{source.relative_to(ROOT)}: external link {destination}: {error}")
                continue
            if parsed.scheme or parsed.netloc or destination.startswith("mailto:"):
                continue

            target_part = urllib.parse.unquote(parsed.path)
            target = (source.parent / target_part).resolve() if target_part else source.resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{source.relative_to(ROOT)}: link escapes repository: {destination}")
                continue

            if target.is_dir():
                candidates = [target / "README.md", target / "index.md"]
                target = next((candidate for candidate in candidates if candidate.is_file()), target)
            if not target.is_file():
                errors.append(f"{source.relative_to(ROOT)}: missing internal target: {destination}")
                continue
            internal_count += 1

            fragment = urllib.parse.unquote(parsed.fragment)
            if fragment and target.suffix.lower() == ".md" and target in slugs and fragment not in slugs[target]:
                errors.append(f"{source.relative_to(ROOT)}: missing heading #{fragment} in {target.relative_to(ROOT)}")

    return errors, internal_count, external_count


def main() -> int:
    errors, internal_count, external_count = validate_links()
    svg_files = sorted(ROOT.rglob("*.svg"))
    for svg in svg_files:
        errors.extend(validate_svg(svg))

    if errors:
        for error in errors:
            print(f"ERROR {error}", file=sys.stderr)
        return 1

    print(
        f"Documentation links valid ({internal_count} internal, {external_count} external references); "
        f"SVG/XML assets valid ({len(svg_files)} files)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
