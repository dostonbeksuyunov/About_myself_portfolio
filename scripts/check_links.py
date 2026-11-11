"""Ishlab turgan saytdagi barcha havolalarni tekshiradi (ichki va tashqi).

Ishlatish:  python scripts/check_links.py [http://127.0.0.1:8010]
Ichki havolalar 200 bo'lishi, tashqilari 200/3xx qaytarishi kerak. LinkedIn bot'larga 999 beradi —
bu ogohlantirish sifatida chiqadi, xato emas. Xato bo'lsa chiqish kodi 1.
"""
import re
import sys
import urllib.error
import urllib.request
from html import unescape
from urllib.parse import urljoin, urlparse

BASE = (sys.argv[1] if len(sys.argv) > 1 else 'http://127.0.0.1:8010').rstrip('/')
UA = {'User-Agent': 'Mozilla/5.0 (compatible; portfolio-link-check)'}
SOFT = {999}  # LinkedIn


def fetch(url, method='GET'):
    req = urllib.request.Request(url, headers=UA, method=method)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.status, resp.read().decode('utf-8', 'replace') if method == 'GET' else ''
    except urllib.error.HTTPError as exc:
        return exc.code, ''
    except Exception as exc:  # tarmoq xatosi
        return f'ERR {type(exc).__name__}', ''


def links_of(html, page_url):
    found = set()
    for attr in ('href', 'src'):
        for raw in re.findall(rf'{attr}="([^"#][^"]*)"', html):
            raw = unescape(raw)
            if raw.startswith(('mailto:', 'tel:', 'javascript:', 'data:')):
                continue
            found.add(urljoin(page_url, raw))
    return found


def main():
    listing = fetch(BASE + '/projects/')[1]
    slugs = sorted(set(re.findall(r'/projects/([a-z0-9-]+)/', listing)))
    pages = ['/', '/projects/'] + [f'/projects/{s}/' for s in slugs]
    pages += [f'{p}?lang={lang}' for p in ('/', '/projects/') for lang in ('ru', 'en')]
    pages += ['/robots.txt', '/sitemap.xml']
    checked, errors, warnings = {}, [], []
    for path in pages:
        status, html = fetch(BASE + path)
        if status != 200:
            errors.append((path, status))
            continue
        for url in links_of(html, BASE + path):
            if url in checked:
                continue
            host = urlparse(url).netloc
            if 'fonts.g' in host:
                continue
            code, _ = fetch(url)
            checked[url] = code
            ok = code == 200 or (isinstance(code, int) and 300 <= code < 400)
            if not ok and code in SOFT:
                warnings.append((url, code))
            elif not ok:
                errors.append((url, code))
    print(f'Sahifalar: {len(pages)}, noyob havolalar: {len(checked)}')
    for url, code in warnings:
        print('  ogohlantirish:', code, url)
    for url, code in errors:
        print('  XATO:', code, url)
    print('Natija:', 'OK' if not errors else f'{len(errors)} ta xato')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
