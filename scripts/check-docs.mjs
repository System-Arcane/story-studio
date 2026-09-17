import { readFile, readdir, access } from 'node:fs/promises';
import path from 'node:path';

// Local Markdown link integrity only; this does not verify semantic freshness.
async function walk(dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  const nested = await Promise.all(entries.map(e => e.isDirectory() ? walk(path.join(dir, e.name)) : e.name.endsWith('.md') ? [path.join(dir, e.name)] : []));
  return nested.flat();
}
const files = ['AGENTS.md', 'ARCHITECTURE.md', 'README.md', ...await walk('docs')];
const errors = [];
for (const file of files) {
  const text = await readFile(file, 'utf8');
  for (const match of text.matchAll(/\[[^\]]*\]\(([^)]+)\)/g)) {
    const href = match[1].trim().replace(/^<|>$/g, '');
    if (/^(https?:|mailto:|#)/.test(href)) continue;
    const target = href.split('#')[0];
    if (!target) continue;
    try { await access(path.resolve(path.dirname(file), decodeURIComponent(target))); }
    catch { errors.push(`${file}: missing linked file ${target}. Fix the link or restore its target.`); }
  }
}
if (errors.length) { console.error(errors.join('\n')); process.exitCode = 1; }
else console.log(`Documentation links OK (${files.length} files). Semantic freshness requires review.`);
