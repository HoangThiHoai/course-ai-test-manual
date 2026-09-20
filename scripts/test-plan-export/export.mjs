#!/usr/bin/env node
// Xuất Master Test Plan (.md) sang HTML một file + PDF A4.
// Dùng: node scripts/test-plan-export/export.mjs <plan.md> [--no-pdf]
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { resolve, dirname, basename, extname, join } from 'node:path';
import { execFileSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';

const args = process.argv.slice(2);
const input = args.find(a => !a.startsWith('--'));
if (!input) {
  console.error('Cách dùng: node scripts/test-plan-export/export.mjs <plan.md> [--no-pdf]');
  process.exit(1);
}
const mdPath = resolve(input);
const outBase = join(dirname(mdPath), basename(mdPath, extname(mdPath)));
const md = readFileSync(mdPath, 'utf8').replace(/\r\n/g, '\n');

// ───────────────────────── inline ─────────────────────────
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

const ICONS = [
  [/✅/g, '<span class="ic ic-ok" title="Có / Đạt">✓</span>'],
  [/❌/g, '<span class="ic ic-no" title="Không / Chưa đạt">✕</span>'],
  [/❓/g, '<span class="ic ic-q" title="Chờ thông tin">?</span>'],
  [/☑/g, '<span class="cb cb-on">✓</span>'],
  [/☐/g, '<span class="cb"></span>'],
  [/⚠️/g, '<span class="ic ic-warn">!</span>'],
];
const DOTS = { '🔴': 'red', '🟠': 'orange', '🟡': 'yellow', '🟢': 'green', '🟩': 'green', '🟨': 'yellow', '🟦': 'blue', '⬛': 'grey', '⚪': 'grey', '⬜': 'grey' };

function inline(src) {
  const codes = [];
  let s = src.replace(/`([^`]+)`/g, (_, c) => `\u0000${codes.push(c) - 1}\u0000`);
  s = esc(s)
    .replace(/&lt;br&gt;/g, '<br>')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/(^|[^*\w])\*([^*\s][^*]*?)\*(?!\*)/g, '$1<em>$2</em>')
    .replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, (_, t, u) => `<a href="${u}">${t}</a>`);
  // "🔴 Cao" / "🔴 <strong>Critical</strong>" → nhãn màu
  s = s.replace(/(🔴|🟠|🟡|🟢|🟩|🟨|🟦|⬛|⚪|⬜)\s*(<strong>[^<]+<\/strong>|[^·,;()<|—\s][^·,;()<|—]*?)(?=\s*(?:·|,|;|\(|<|—|$))/gu,
    (_, dot, label) => `<span class="pill pill-${DOTS[dot]}">${label.replace(/<\/?strong>/g, '').trim()}</span>`);
  s = s.replace(/(🔴|🟠|🟡|🟢|🟩|🟨|🟦|⬛|⚪|⬜)/gu, (dot) => `<span class="dot dot-${DOTS[dot]}"></span>`);
  for (const [re, html] of ICONS) s = s.replace(re, html);
  s = s.replace(/[📘🔒🔧⭐📂📌]\uFE0F?\s?/gu, '');
  return s.replace(/\u0000(\d+)\u0000/g, (_, i) => `<code>${esc(codes[+i])}</code>`);
}
const plain = s => s.replace(/[`*]/g, '').trim();

// ───────────────────────── block ─────────────────────────
const toc = [];
let docTitle = '';
let banner = '';
const kv = {};

function slug(text) {
  const num = text.match(/^(\d+(?:\.\d+)*)\.?\s/);
  if (num) return 's' + num[1].replace(/\./g, '-');
  return 'h-' + text.normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/đ/gi, 'd')
    .toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

function splitRow(line) {
  return line.replace(/\\\|/g, '\u0001').trim().replace(/^\||\|$/g, '').split('|')
    .map(c => c.replace(/\u0001/g, '|').trim());
}

function renderTable(rows, ctx) {
  const [head, , ...body] = rows.map(splitRow);
  const isKV = head.every(h => h === '');
  const cols = head.length;
  if (isKV && ctx.lastHeading === 'Thông tin tài liệu') {
    for (const r of body) kv[plain(r[0])] = r[1];
  }
  const cls = ['tbl', isKV ? 'tbl-kv' : '', cols >= 6 ? 'tbl-wide' : ''].filter(Boolean).join(' ');
  let h = `<div class="tbl-wrap${body.length <= 10 ? ' keep' : ''}"><table class="${cls}">`;
  if (!isKV) h += '<thead><tr>' + head.map(c => `<th>${inline(c)}</th>`).join('') + '</tr></thead>';
  h += '<tbody>';
  for (const r of body) {
    const total = /^\*\*(Tổng|Total)/.test(r[0]) ? ' class="row-total"' : '';
    const td = c => (/^\d{2}[-/]\d{2}[-/]\d{4}$/.test(plain(c)) ? `<td class="nowrap">${inline(c)}</td>` : `<td>${inline(c)}</td>`);
    h += `<tr${total}>` + r.map((c, i) => (isKV && i === 0 ? `<th scope="row">${inline(c)}</th>` : td(c))).join('') + '</tr>';
  }
  return h + '</tbody></table></div>';
}

function parseBlocks(lines, ctx = { lastHeading: '' }) {
  let out = '';
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    if (!line.trim()) { i++; continue; }

    const fence = line.match(/^```(\w*)/);
    if (fence) {
      const buf = [];
      i++;
      while (i < lines.length && !lines[i].startsWith('```')) buf.push(lines[i++]);
      i++;
      out += `<pre class="diagram"><code>${esc(buf.join('\n'))}</code></pre>`;
      continue;
    }

    const hd = line.match(/^(#{1,6})\s+(.*)$/);
    if (hd) {
      const level = hd[1].length;
      const text = hd[2].trim();
      ctx.lastHeading = plain(text);
      i++;
      if (level === 1) { docTitle = plain(text); continue; }
      const id = slug(plain(text));
      if (level <= 3) toc.push({ level, text: plain(text), id });
      const m = plain(text).match(/^(\d+(?:\.\d+)*)\.?\s+(.*)$/);
      const inner = m && level === 2
        ? `<span class="sec-no">${m[1]}</span><span>${inline(text.replace(/^\d+(?:\.\d+)*\.?\s+/, ''))}</span>`
        : inline(text);
      out += `<h${level} id="${id}">${inner}</h${level}>`;
      continue;
    }

    if (/^-{3,}\s*$/.test(line)) { i++; continue; }

    if (line.startsWith('>')) {
      const buf = [];
      while (i < lines.length && lines[i].startsWith('>')) buf.push(lines[i++].replace(/^>\s?/, ''));
      const first = buf.find(b => b.trim()) || '';
      const inner = parseBlocks(buf, ctx);
      if (first.startsWith('📘')) { banner = inner; continue; }
      const kind = first.startsWith('⚠️') ? 'warn' : /Ô còn treo/.test(first) ? 'todo' : 'note';
      out += `<aside class="callout callout-${kind}">${inner.replace(/^<p>(<span class="ic ic-warn">!<\/span>\s*)/, '<p>')}</aside>`;
      continue;
    }

    if (line.startsWith('|') && lines[i + 1] && /^\|?\s*:?-{2,}/.test(lines[i + 1])) {
      const rows = [];
      while (i < lines.length && lines[i].startsWith('|')) rows.push(lines[i++]);
      out += renderTable(rows, ctx);
      continue;
    }

    if (/^\s*[-*]\s+/.test(line)) {
      const items = [];
      while (i < lines.length && /^\s*[-*]\s+/.test(lines[i])) items.push(lines[i++].replace(/^\s*[-*]\s+/, ''));
      out += '<ul>' + items.map(it => `<li>${inline(it)}</li>`).join('') + '</ul>';
      continue;
    }

    const para = [];
    while (i < lines.length && lines[i].trim() && !/^(#|>|\||```|\s*[-*]\s)/.test(lines[i]) && !/^-{3,}\s*$/.test(lines[i])) para.push(lines[i++]);
    out += `<p>${inline(para.join(' '))}</p>`;
  }
  return out;
}

const body = parseBlocks(md.split('\n'));

// ───────────────────────── trang bìa + mục lục ─────────────────────────
const [titleMain, titleSub = ''] = docTitle.split(/\s+—\s+/);
const kvText = k => (kv[k] ? inline(kv[k]) : '—');
const statusRaw = plain(kv['Trạng thái'] || '');
const coverFields = [
  ['Mã tài liệu', 'Mã tài liệu'], ['Phiên bản', 'Phiên bản tài liệu'], ['Mức phân loại', 'Mức phân loại'],
  ['Ngày lập', 'Ngày lập'], ['Ngày hiệu lực', 'Ngày hiệu lực'], ['Người lập', 'Người lập'],
  ['Người phê duyệt', 'Người phê duyệt'], ['Hệ thống · Build', 'Hệ thống · Build'],
];
const cover = `
<section class="cover">
  <div class="cover-top">
    <div class="cover-kicker">Kế hoạch kiểm thử tổng thể</div>
    <h1 class="cover-title">${esc(titleMain || 'Master Test Plan')}</h1>
    <div class="cover-sub">${esc(titleSub)}</div>
    <div class="cover-status">${kvText('Trạng thái')}</div>
  </div>
  ${banner ? `<div class="cover-banner">${banner}</div>` : ''}
  <dl class="cover-meta">
    ${coverFields.map(([label, key]) => `<div><dt>${label}</dt><dd>${kvText(key)}</dd></div>`).join('')}
  </dl>
  <div class="cover-foot">Biên soạn theo cấu trúc ISO/IEC/IEEE 29119-3 — Test Plan · phủ nội dung điển hình ISTQB CTFL v4.0 mục 5.1.1</div>
</section>`;

const tocHtml = `<nav class="toc" aria-label="Mục lục"><div class="toc-title">Mục lục</div><ol>` +
  toc.filter(t => t.level === 2).map(t => {
    const kids = toc.slice(toc.indexOf(t) + 1);
    const end = kids.findIndex(k => k.level === 2);
    const subs = (end === -1 ? kids : kids.slice(0, end)).filter(k => k.level === 3);
    return `<li><a href="#${t.id}">${esc(t.text)}</a>${subs.length ? '<ol>' + subs.map(s => `<li><a href="#${s.id}">${esc(s.text)}</a></li>`).join('') + '</ol>' : ''}</li>`;
  }).join('') + '</ol></nav>';

const docCode = plain(kv['Mã tài liệu'] || basename(outBase));
const version = plain(kv['Phiên bản tài liệu'] || '');
const classification = plain(kv['Mức phân loại'] || '');

// ───────────────────────── CSS ─────────────────────────
const css = `
:root{--ink:#1c2430;--muted:#5b6675;--line:#dde3ea;--soft:#f4f6f9;--brand:#1f4e79;--brand-2:#2e75b6;--accent:#e8f0f8;
--ok:#1e7b46;--ok-bg:#e3f4ea;--no:#b42318;--no-bg:#fde8e7;--q:#a15c00;--q-bg:#fff2dc;--bg:#fff}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:#eef1f5;color:var(--ink);font:14px/1.6 "Be Vietnam Pro","Segoe UI",Roboto,Arial,sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.layout{display:grid;grid-template-columns:280px minmax(0,1fr);max-width:1400px;margin:0 auto;gap:28px;padding:28px}
.sidebar{position:sticky;top:28px;align-self:start;max-height:calc(100vh - 56px);overflow:auto;background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:18px 16px}
.page{background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:40px 48px;min-width:0}
.toc-title{font-weight:700;color:var(--brand);text-transform:uppercase;letter-spacing:.06em;font-size:12px;margin-bottom:10px}
.toc ol{list-style:none;margin:0;padding:0}
.toc>ol>li{margin:2px 0}
.toc a{display:block;color:var(--ink);text-decoration:none;padding:4px 8px;border-radius:6px;font-size:13px}
.toc a:hover{background:var(--accent);color:var(--brand)}
.toc>ol>li>a{font-weight:600}
.toc ol ol a{padding-left:20px;color:var(--muted);font-size:12.5px}
.toc a.active{background:var(--accent);color:var(--brand)}
.cover{border-radius:12px;overflow:hidden;border:1px solid var(--line);margin-bottom:36px}
.cover-top{background:linear-gradient(135deg,var(--brand) 0%,var(--brand-2) 100%);color:#fff;padding:44px 44px 36px}
.cover-kicker{text-transform:uppercase;letter-spacing:.14em;font-size:12px;opacity:.85}
.cover-title{font-size:38px;line-height:1.15;margin:10px 0 6px;font-weight:700}
.cover-sub{font-size:20px;opacity:.95}
.cover-status{margin-top:18px}
.cover-status .pill{font-size:13px;padding:4px 12px;background:#fff}
.cover-banner{background:#fff8e6;border-bottom:1px solid #f1dfb1;padding:14px 44px;font-size:13px;color:#6b4e00}
.cover-banner>p:first-child>strong:first-child{display:inline-block;text-transform:uppercase;letter-spacing:.06em;font-size:11px;background:#a15c00;color:#fff;padding:2px 8px;border-radius:4px;margin-bottom:6px}
.cover-banner p{margin:4px 0}
.cover-meta{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));margin:0;padding:8px 44px 20px;gap:0 32px}
.cover-meta div{padding:10px 0;border-bottom:1px solid var(--line)}
.cover-meta dt{font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.cover-meta dd{margin:2px 0 0;font-weight:500}
.cover-foot{padding:12px 44px;background:var(--soft);font-size:12px;color:var(--muted)}
h2{display:flex;align-items:center;gap:12px;font-size:22px;color:var(--brand);margin:44px 0 14px;padding-bottom:10px;border-bottom:2px solid var(--brand)}
h2:first-of-type{margin-top:0}
.sec-no{display:inline-flex;align-items:center;justify-content:center;min-width:34px;height:34px;padding:0 8px;border-radius:8px;background:var(--brand);color:#fff;font-size:16px}
h3{font-size:17px;color:var(--ink);margin:30px 0 10px;padding-left:10px;border-left:4px solid var(--brand-2)}
h4{font-size:15px;margin:22px 0 8px;color:var(--brand)}
p{margin:10px 0}
ul{margin:8px 0;padding-left:22px}
li{margin:3px 0}
a{color:var(--brand-2)}
code{font:12px/1.4 Consolas,"Cascadia Mono",monospace;background:#eef2f7;border:1px solid #e1e7ef;border-radius:4px;padding:1px 5px;color:#26354a;word-break:break-word}
pre.diagram{background:#0f1e2e;color:#dbe7f3;border-radius:10px;padding:18px 20px;overflow:auto;font:12.5px/1.5 Consolas,"Cascadia Mono",monospace}
pre.diagram code{background:none;border:0;color:inherit;padding:0}
.tbl-wrap{overflow-x:auto;margin:12px 0 18px;border:1px solid var(--line);border-radius:10px}
table.tbl{width:100%;border-collapse:collapse;font-size:13px}
.tbl thead th{background:var(--brand);color:#fff;text-align:left;font-weight:600;padding:9px 12px;white-space:nowrap}
.tbl td,.tbl tbody th{padding:8px 12px;border-top:1px solid var(--line);vertical-align:top;text-align:left}
.tbl tbody tr:nth-child(even) td{background:#fafbfd}
.tbl-kv tbody th{width:230px;background:var(--soft);color:var(--muted);font-weight:600}
.tbl-kv tbody tr:first-child th,.tbl-kv tbody tr:first-child td{border-top:0}
.tbl-wide{font-size:12.5px}
.tbl td.nowrap{white-space:nowrap}
.row-total td{background:var(--accent)!important;font-weight:600}
.callout{margin:14px 0;padding:12px 16px 12px 44px;border-radius:10px;position:relative;font-size:13.5px}
.callout p{margin:4px 0}
.callout::before{position:absolute;left:14px;top:12px;width:20px;height:20px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:12px;color:#fff}
.callout-note{background:#eef5fc;border:1px solid #cfe1f3}
.callout-note::before{content:"i";background:var(--brand-2)}
.callout-warn{background:#fff6e8;border:1px solid #f3d9a8}
.callout-warn::before{content:"!";background:#c77700}
.callout-todo{background:#f3f7ee;border:1px solid #d5e5c3}
.callout-todo::before{content:"✓";background:var(--ok)}
.pill{display:inline-block;padding:1px 9px;border-radius:999px;font-size:12px;font-weight:600;white-space:nowrap;border:1px solid transparent}
.pill-red{background:#fde8e7;color:#b42318;border-color:#f6c5c1}
.pill-orange{background:#fff0e0;color:#b54708;border-color:#f7d2a8}
.pill-yellow{background:#fff7d6;color:#8a6100;border-color:#f0dc92}
.pill-green{background:#e3f4ea;color:#1e7b46;border-color:#b7e0c6}
.pill-blue{background:#e6effa;color:#1f4e79;border-color:#bcd2ec}
.pill-grey{background:#eef0f3;color:#475467;border-color:#d6dbe1}
.dot{display:inline-block;width:9px;height:9px;border-radius:50%;margin:0 3px;vertical-align:0}
.dot-red{background:#d92d20}.dot-orange{background:#f79009}.dot-yellow{background:#eaaa08}.dot-green{background:#17b26a}.dot-blue{background:#2e75b6}.dot-grey{background:#98a2b3}
.ic{display:inline-flex;align-items:center;justify-content:center;width:18px;height:18px;border-radius:50%;font-size:11px;font-weight:700;vertical-align:-3px;margin-right:2px}
.ic-ok{background:var(--ok-bg);color:var(--ok)}
.ic-no{background:var(--no-bg);color:var(--no)}
.ic-q{background:var(--q-bg);color:var(--q)}
.ic-warn{background:#fff0d6;color:#b25e00}
.cb{display:inline-flex;align-items:center;justify-content:center;width:15px;height:15px;border:1.5px solid #8a96a6;border-radius:3px;font-size:11px;vertical-align:-2px;margin-right:4px}
.cb-on{background:var(--brand);border-color:var(--brand);color:#fff}
.doc-footer{margin-top:40px;padding-top:14px;border-top:1px solid var(--line);font-size:12px;color:var(--muted);display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap}
.print-toc{display:none}
@media screen and (max-width:1000px){.layout{grid-template-columns:1fr;padding:16px}.sidebar{position:static;max-height:none}.page{padding:24px 18px}.cover-top,.cover-meta,.cover-banner,.cover-foot{padding-left:20px;padding-right:20px}.cover-meta{grid-template-columns:1fr}.cover-title{font-size:30px}}
@page{size:A4;margin:18mm 14mm 18mm 14mm;
  @top-left{content:"${esc(titleMain)} — ${esc(titleSub)}";font:8pt "Segoe UI",Arial,sans-serif;color:#5b6675}
  @top-right{content:"${esc(classification)}";font:8pt "Segoe UI",Arial,sans-serif;color:#5b6675}
  @bottom-left{content:"${esc(docCode)} · ${esc(version)}";font:8pt "Segoe UI",Arial,sans-serif;color:#5b6675}
  @bottom-right{content:"Trang " counter(page) " / " counter(pages);font:8pt "Segoe UI",Arial,sans-serif;color:#5b6675}}
@page :first{margin:0;@top-left{content:none}@top-right{content:none}@bottom-left{content:none}@bottom-right{content:none}}
@media print{
  body{background:#fff;font-size:9.5pt}
  .layout{display:block;padding:0;max-width:none}
  .sidebar{display:none}
  .page{border:0;border-radius:0;padding:0}
  .cover{height:297mm;margin:0;border:0;border-radius:0;display:flex;flex-direction:column;break-after:page}
  .cover-top{padding:70mm 18mm 16mm}
  .cover-title{font-size:34pt}
  .cover-banner,.cover-meta,.cover-foot{padding-left:18mm;padding-right:18mm}
  .cover-meta{flex:1;align-content:start;padding-top:10mm}
  .cover-foot{margin-top:auto}
  .print-toc{display:block;break-after:page}
  .print-toc>.toc>ol{columns:2;column-gap:10mm}
  .print-toc>.toc>ol>li{break-inside:avoid}
  .print-toc .toc-title{font-size:18pt;text-transform:none;letter-spacing:0;color:var(--brand);border-bottom:2px solid var(--brand);padding-bottom:6px;margin-bottom:12px}
  .print-toc a{font-size:10pt;padding:2px 0}
  .print-toc ol ol a{padding-left:18px;font-size:9pt}
  h2{break-before:page;font-size:15pt;margin-top:0}
  h2 .sec-no{min-width:26px;height:26px;font-size:12pt}
  h3{font-size:12pt;break-after:avoid}
  h2,h3,h4{break-after:avoid}
  .tbl-wrap{overflow:visible;border-radius:6px}
  table.tbl{font-size:8.5pt}
  .tbl-wide{font-size:8pt}
  .tbl thead th{white-space:normal;padding:6px 8px}
  .tbl td,.tbl tbody th{padding:5px 8px}
  .tbl-kv tbody th{width:48mm}
  thead{display:table-header-group}
  tr,.callout,pre,.tbl-wrap.keep{break-inside:avoid}
  pre.diagram{font-size:8pt}
  a{color:inherit;text-decoration:none}
  .doc-footer{display:none}
}`;

const js = `
const links=[...document.querySelectorAll('.sidebar .toc a')];
const map=new Map(links.map(a=>[a.getAttribute('href').slice(1),a]));
const obs=new IntersectionObserver(es=>{for(const e of es){if(e.isIntersecting){links.forEach(l=>l.classList.remove('active'));const a=map.get(e.target.id);if(a){a.classList.add('active');a.scrollIntoView({block:'nearest'});}}}},{rootMargin:'0px 0px -75% 0px'});
document.querySelectorAll('.page h2[id],.page h3[id]').forEach(h=>obs.observe(h));`;

const html = `<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(docTitle)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>${css}</style>
</head>
<body>
<div class="layout">
  <aside class="sidebar">${tocHtml}</aside>
  <main class="page">
    ${cover}
    <div class="print-toc">${tocHtml}</div>
    ${body}
    <footer class="doc-footer"><span>${esc(docCode)} · ${esc(version)} · ${esc(classification)}</span><span>${esc(statusRaw)}</span></footer>
  </main>
</div>
<script>${js}</script>
</body>
</html>`;

writeFileSync(outBase + '.html', html, 'utf8');
console.log('HTML:', outBase + '.html');

if (!args.includes('--no-pdf')) {
  const candidates = [
    process.env.CHROME_PATH,
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/usr/bin/google-chrome', '/usr/bin/chromium',
  ].filter(Boolean);
  const browser = candidates.find(p => existsSync(p));
  if (!browser) {
    console.error('Không tìm thấy Chrome/Edge — đặt biến CHROME_PATH hoặc in HTML ra PDF bằng Ctrl+P.');
    process.exit(2);
  }
  execFileSync(browser, [
    '--headless=new', '--disable-gpu', '--no-pdf-header-footer', '--virtual-time-budget=8000',
    `--print-to-pdf=${outBase}.pdf`, pathToFileURL(outBase + '.html').href,
  ], { stdio: 'ignore' });
  console.log('PDF :', outBase + '.pdf');
}
