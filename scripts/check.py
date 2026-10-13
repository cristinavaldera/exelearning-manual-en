#!/usr/bin/env python3
"""Validates the packaged manual: python3 scripts/check.py <project.elpx> <site-dir>

- The .elpx is a valid ZIP with a well-formed content.xml, and every
  {{context_path}}/content/resources/... it references is inside the package.
- The exported site has index.html, and every local src/href in its pages
  points to an existing file. Links into the editor's own files (files/perm/)
  can never be exported: they come from the content and are only warnings.
Exits with status 1 and lists the problems if something fails.
"""
import html
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

URL_ATTRS = {"src", "href", "poster", "data"}


def check_elpx(path, errors):
    with zipfile.ZipFile(path) as z:
        bad = z.testzip()
        if bad:
            errors.append(f"{path}: corrupt entry {bad}")
        names = set(z.namelist())
        if "content.xml" not in names:
            errors.append(f"{path}: content.xml is missing")
            return
        xml = z.read("content.xml")
    try:
        ET.fromstring(xml)
    except ET.ParseError as e:
        errors.append(f"content.xml is not well-formed: {e}")
    text = html.unescape(xml.decode("utf-8"))
    refs = set(re.findall(r"\{\{context_path\}\}/(content/resources/[^\"'<>\\]+)", text))
    for ref in sorted(refs):
        if unquote(ref) not in names and ref not in names:
            errors.append(f"content.xml references {ref}, which is not in the package")
    print(f"{path}: {len(names)} files, {len(refs)} resource references")


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        self.urls += [v for k, v in attrs if k in URL_ATTRS and v]


def check_site(site, errors, warnings):
    site = Path(site)
    if not (site / "index.html").is_file():
        errors.append(f"{site}/index.html is missing")
    pages = sorted(site.rglob("*.html"))
    checked = 0
    for page in pages:
        text = page.read_text(encoding="utf-8")
        # Diagrams left unrendered are drawn in the browser by libs/mermaid/.
        if 'class="mermaid"' in text and not (site / "libs/mermaid/mermaid.min.js").is_file():
            errors.append(f"{page.relative_to(site)}: Mermaid diagram without libs/mermaid/mermaid.min.js")
        parser = Links()
        parser.feed(text)
        for url in parser.urls:
            parts = urlsplit(url)
            if parts.scheme or parts.netloc or not parts.path or "{{" in url:
                continue
            target = (page.parent / unquote(parts.path)).resolve()
            checked += 1
            if not target.exists():
                problems = warnings if "files/perm/" in url else errors
                problems.append(f"{page.relative_to(site)}: broken link {url}")
    print(f"{site}: {len(pages)} pages, {checked} local links")


def main(elpx, site):
    errors, warnings = [], []
    check_elpx(elpx, errors)
    check_site(site, errors, warnings)
    for w in warnings:
        print("WARNING", w)
    for e in errors:
        print("ERROR", e)
    print("OK" if not errors else f"{len(errors)} problems")
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.exit(main(*sys.argv[1:]))
