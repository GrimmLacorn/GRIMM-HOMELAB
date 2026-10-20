import fs from "node:fs";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";
import YAML from "yaml";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const checked = [];
const errors = [];

function walk(directory) {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const fullPath = path.join(directory, entry.name);
    if (entry.isDirectory()) {
      walk(fullPath);
    } else if (entry.isFile() && /\.ya?ml$/i.test(entry.name)) {
      checked.push(fullPath);
    }
  }
}

function parseYaml(contents, source) {
  const document = YAML.parseDocument(contents, { uniqueKeys: true, prettyErrors: true });
  if (document.errors.length > 0) {
    for (const error of document.errors) errors.push(`${source}: ${error.message}`);
  }
  return document;
}

walk(path.join(root, ".github"));
for (const file of checked) {
  const source = path.relative(root, file);
  parseYaml(fs.readFileSync(file, "utf8"), source);
}

const skillRoot = path.join(root, ".agents", "skills");
for (const entry of fs.readdirSync(skillRoot, { withFileTypes: true })) {
  if (!entry.isDirectory()) continue;
  const skillPath = path.join(skillRoot, entry.name, "SKILL.md");
  if (!fs.existsSync(skillPath)) {
    errors.push(`${path.relative(root, skillPath)}: SKILL.md is required`);
    continue;
  }
  const source = path.relative(root, skillPath);
  const contents = fs.readFileSync(skillPath, "utf8");
  const match = contents.match(/^---\s*\r?\n([\s\S]*?)\r?\n---\s*(?:\r?\n|$)/);
  if (!match) {
    errors.push(`${source}: YAML frontmatter is required`);
    continue;
  }
  const metadata = parseYaml(match[1], source).toJSON();
  if (!metadata || typeof metadata !== "object") {
    errors.push(`${source}: frontmatter must be a mapping`);
    continue;
  }
  const name = metadata.name;
  const description = metadata.description;
  if (typeof name !== "string" || name.length < 1 || name.length > 64) {
    errors.push(`${source}: name must contain 1 to 64 characters`);
  } else if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(name)) {
    errors.push(`${source}: name must use lowercase letters, numbers, and single hyphens`);
  } else if (name !== entry.name) {
    errors.push(`${source}: name '${name}' must match directory '${entry.name}'`);
  }
  if (typeof description !== "string" || description.trim().length < 1 || description.length > 1024) {
    errors.push(`${source}: description must contain 1 to 1024 characters`);
  }
}

if (errors.length > 0) {
  for (const error of errors) console.error(`ERROR ${error}`);
  process.exitCode = 1;
} else {
  console.log(`YAML and skill metadata valid (${checked.length} workflow file(s), ${fs.readdirSync(skillRoot).filter((name) => fs.statSync(path.join(skillRoot, name)).isDirectory()).length} skill(s)).`);
}
