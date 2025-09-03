#!/usr/bin/env python3
import sys, os, html, datetime
from pathlib import Path

def list_samples(samples_dir: Path):
    files = sorted(samples_dir.glob("*.html"))
    items = []
    for f in files:
        mtime = datetime.datetime.fromtimestamp(f.stat().st_mtime)
        items.append((f.name, mtime.isoformat()))
    return items

TEMPLATE = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1" />
<title>SceneStealer Archive</title>
<style>
body{font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial;background:#0b0f16;color:#e7ecf5;margin:0}
.wrap{max-width:960px;margin:40px auto;padding:0 16px}
h1{font-size:28px;margin-bottom:8px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin-top:24px}
.card{border:1px solid rgba(255,255,255,.08);border-radius:12px;padding:16px;background:rgba(255,255,255,.02)}
.card a{color:#a5b4fc;text-decoration:none}
.meta{color:#94a3b8;font-size:12px;margin-top:6px}
.top{display:flex;justify-content:space-between;align-items:center;gap:12px}
.btn{border:1px solid rgba(255,255,255,.08);padding:8px 12px;border-radius:8px;color:#e7ecf5;text-decoration:none}
</style>
</head><body>
<div class="wrap">
  <div class="top">
    <h1>SceneStealer — Samples Archive</h1>
    <a class="btn" href="./index.html">Latest</a>
  </div>
  <div class="grid">
    {cards}
  </div>
</div>
</body></html>"""

CARD = """<div class="card">
  <strong>{name}</strong>
  <div class="meta">Updated: {mtime}</div>
  <div style="margin-top:10px;display:flex;gap:8px;flex-wrap:wrap">
    <a href="../samples/{name}" target="_blank">Preview</a>
    <a href="../samples/{name}" download>Download</a>
    <a href="../editor/index.html?load=../samples/{qname}" target="_blank">Open in Editor</a>
  </div>
</div>"""

def main():
    if len(sys.argv) != 3:
        print("Usage: generate_archive.py <samples_dir> <out_html>")
        sys.exit(1)
    samples_dir = Path(sys.argv[1]).resolve()
    out_html = Path(sys.argv[2]).resolve()
    items = list_samples(samples_dir)
    # 최신이 위로
    items.sort(key=lambda x: x[1], reverse=True)
    cards = []
    for name, mtime in items:
        cards.append(CARD.format(
            name=html.escape(name),
            qname=html.escape(name),
            mtime=html.escape(mtime)
        ))
    out_html.parent.mkdir(parents=True, exist_ok=True)
    out_html.write_text(TEMPLATE.replace("{cards}", "\n".join(cards)), encoding="utf-8")
    print(f"Wrote {out_html}")

if __name__ == "__main__":
    main()