const fs = require('fs');
const path = process.argv[2];
const text = fs.readFileSync(path, 'utf8');

const startMarker = '\\csname PreBibitemsHook\\endcsname';
const startIdx = text.indexOf(startMarker) + startMarker.length;
const endMarker = '\\end{thebibliography}';
const endIdx = text.indexOf(endMarker);

const header = text.slice(0, startIdx);
const footer = text.slice(endIdx);
const body = text.slice(startIdx, endIdx);

// Split into blocks by the "%%% N" comment markers
const parts = body.split(/\n%%% \d+\n/).filter(p => p.trim().length > 0);

function sortKey(block) {
  const m = block.match(/\\citeauthoryear\{([\s\S]*?)\}\{(\d{4}[a-z]?)\}/);
  if (!m) return { name: 'zzz', year: '9999' };
  let namePart = m[1];
  // take text before " and " or " et~al."
  namePart = namePart.split(/\s+and\s+/)[0];
  namePart = namePart.replace(/\s*et~al\.?/, '');
  // strip latex commands/braces/tildes/accents markup, normalize whitespace
  namePart = namePart.replace(/\{|\}/g, '').replace(/~/g, ' ').replace(/\\[a-zA-Z]+/g, '').trim();
  namePart = namePart.toLowerCase().replace(/[\s-]/g, '');
  return { name: namePart, year: m[2] };
}

const blocks = parts.map(p => ({ text: p.trim(), key: sortKey(p) }));

blocks.sort((a, b) => {
  if (a.key.name < b.key.name) return -1;
  if (a.key.name > b.key.name) return 1;
  return a.key.year.localeCompare(b.key.year);
});

// Diagnostic: print sorted order
blocks.forEach((b, i) => console.error(`${i+1}. ${b.key.name} (${b.key.year})`));

const rebuilt = blocks.map((b, i) => `%%% ${i+1}\n${b.text}`).join('\n\n');

const out = header + '\n\n' + rebuilt + '\n\n' + footer;
fs.writeFileSync(path, out);
console.error('Done. Wrote', blocks.length, 'entries.');
