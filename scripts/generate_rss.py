#!/usr/bin/env python3
import sys, datetime
from pathlib import Path
from xml.sax.saxutils import escape

def main():
    if len(sys.argv) != 3:
        print("Usage: generate_rss.py <samples_dir> <out_rss>")
        sys.exit(1)
    samples_dir = Path(sys.argv[1]).resolve()
    out_rss = Path(sys.argv[2]).resolve()

    base_url = "https://dtslib1979.github.io/scenestealer-engine"  # ← Updated for actual repo
    items = []
    for f in sorted(samples_dir.glob("*.html"), key=lambda p: p.stat().st_mtime, reverse=True):
        dt = datetime.datetime.fromtimestamp(f.stat().st_mtime, tz=datetime.timezone.utc)
        pub = dt.strftime("%a, %d %b %Y %H:%M:%S %z")
        url = f"{base_url}/samples/{f.name}"
        items.append(f"""<item>
<title>{escape(f.name)}</title>
<link>{escape(url)}</link>
<guid isPermaLink="true">{escape(url)}</guid>
<pubDate>{pub}</pubDate>
<description>SceneStealer sample: {escape(f.name)}</description>
</item>""")

    rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel>
<title>SceneStealer Samples</title>
<link>{escape(base_url)}/archive.html</link>
<description>Latest SceneStealer samples</description>
<lastBuildDate>{datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")}</lastBuildDate>
{''.join(items)}
</channel></rss>"""
    out_rss.parent.mkdir(parents=True, exist_ok=True)
    out_rss.write_text(rss, encoding="utf-8")
    print(f"Wrote {out_rss}")

if __name__ == "__main__":
    main()