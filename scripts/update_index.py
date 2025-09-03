#!/usr/bin/env python3
import sys, os, datetime
from pathlib import Path

TEMPLATE = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>SceneStealer — Latest</title>
<style>
body{{font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial;background:#0b0f16;color:#e7ecf5;margin:0}}
.wrap{{max-width:960px;margin:40px auto;padding:0 16px}}
h1{{font-size:28px;margin-bottom:8px}}
a.btn{{border:1px solid rgba(255,255,255,.08);padding:8px 12px;border-radius:8px;color:#e7ecf5;text-decoration:none;margin-right:8px}}
.frame{{width:100%;height:80vh;border:1px solid rgba(255,255,255,.08);border-radius:12px;margin-top:16px;background:#111}}
.meta{{color:#94a3b8;font-size:12px;margin-top:6px}}
</style>
</head><body>
<div class="wrap">
  <h1>SceneStealer — Latest Sample</h1>
  <div class="meta">Latest: {name} (Updated: {mtime})</div>
  <div style="margin-top:12px">
    <a class="btn" href="./archive.html">All Samples</a>
    <a class="btn" href="../samples/{name}" target="_blank">Open Raw</a>
    <a class="btn" href="../editor/index.html?load=../samples/{name}" target="_blank">Open in Editor</a>
  </div>
  <iframe class="frame" src="../samples/{name}"></iframe>
</div>
</body></html>
"""

def main():
    if len(sys.argv) != 3:
        print("Usage: update_index.py <samples_dir> <out_html>")
        sys.exit(1)
    samples_dir = Path(sys.argv[1]).resolve()
    out_html = Path(sys.argv[2]).resolve()
    files = list(samples_dir.glob("*.html"))
    if not files:
        # 샘플이 없으면 기본 페이지
        out_html.parent.mkdir(parents=True, exist_ok=True)
        out_html.write_text("<!doctype html><meta charset='utf-8'><p>No samples yet.</p>", encoding="utf-8")
        return
    latest = max(files, key=lambda f: f.stat().st_mtime)
    mtime = datetime.datetime.fromtimestamp(latest.stat().st_mtime).isoformat()
    out_html.parent.mkdir(parents=True, exist_ok=True)
    out_html.write_text(TEMPLATE.format(name=latest.name, mtime=mtime), encoding="utf-8")
    print(f"Wrote {out_html} (latest = {latest.name})")

if __name__ == "__main__":
    main()