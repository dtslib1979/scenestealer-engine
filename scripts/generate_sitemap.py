#!/usr/bin/env python3
import sys, datetime
from pathlib import Path
from xml.sax.saxutils import escape

def main():
    if len(sys.argv) != 3:
        print("Usage: generate_sitemap.py <web_dir> <out_xml>")
        sys.exit(1)
    web_dir = Path(sys.argv[1]).resolve()
    out_xml = Path(sys.argv[2]).resolve()
    base_url = "https://dtslib1979.github.io/scenestealer-engine"  # Updated for actual repo

    urls = []
    for f in web_dir.glob("*.html"):
        loc = f"{base_url}/{f.name}"
        lastmod = datetime.datetime.fromtimestamp(f.stat().st_mtime, tz=datetime.timezone.utc).date()
        urls.append(f"""<url><loc>{escape(loc)}</loc><lastmod>{lastmod}</lastmod></url>""")

    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{''.join(urls)}
</urlset>"""
    out_xml.parent.mkdir(parents=True, exist_ok=True)
    out_xml.write_text(xml, encoding="utf-8")
    print(f"Wrote {out_xml}")

if __name__ == "__main__":
    main()