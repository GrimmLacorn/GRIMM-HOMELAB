#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";
import { JSDOM } from "jsdom";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const markdownFiles = [];
const errors = [];
let diagramCount = 0;

function walk(directory) {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    if (entry.name === ".git" || entry.name === "node_modules") continue;
    const fullPath = path.join(directory, entry.name);
    if (entry.isDirectory()) walk(fullPath);
    else if (entry.isFile() && entry.name.endsWith(".md")) markdownFiles.push(fullPath);
  }
}

walk(root);

// Mermaid's parser uses DOMPurify in its Node build. A local JSDOM instance
// supplies the document without launching a browser or opening local files.
const dom = new JSDOM("<!doctype html><html><body></body></html>", { pretendToBeVisual: true });
for (const key of ["window", "document", "Element", "HTMLElement", "SVGElement", "Node", "DOMParser", "XMLSerializer"]) {
  globalThis[key] = dom.window[key];
}
Object.defineProperty(globalThis, "navigator", { value: dom.window.navigator, configurable: true });
const { default: createDOMPurify } = await import("dompurify");
globalThis.DOMPurify = createDOMPurify(dom.window);
dom.window.DOMPurify = globalThis.DOMPurify;
const { default: mermaid } = await import("mermaid");
mermaid.initialize({ startOnLoad: false, securityLevel: "strict", theme: "base" });

for (const file of markdownFiles.sort()) {
  const contents = fs.readFileSync(file, "utf8");
  const blocks = contents.matchAll(/```mermaid\s*\r?\n([\s\S]*?)\r?\n```/g);
  let blockNumber = 0;
  for (const match of blocks) {
    blockNumber += 1;
    diagramCount += 1;
    const source = match[1].trim();
    const relative = path.relative(root, file);
    if (!source) {
      errors.push(`${relative}: Mermaid block ${blockNumber} is empty`);
      continue;
    }
    try {
      const result = await mermaid.parse(source);
      if (!result?.diagramType) errors.push(`${relative}: Mermaid block ${blockNumber} has no recognized diagram type`);
    } catch (error) {
      errors.push(`${relative}: Mermaid block ${blockNumber}: ${error.message}`);
    }
  }
}

if (diagramCount < 12) errors.push(`Expected at least 12 Mermaid diagrams; found ${diagramCount}`);

if (errors.length > 0) {
  for (const error of errors) console.error(`ERROR ${error}`);
  process.exitCode = 1;
} else {
  console.log(`Mermaid syntax valid (${diagramCount} diagram(s) across ${markdownFiles.length} Markdown file(s)).`);
}
