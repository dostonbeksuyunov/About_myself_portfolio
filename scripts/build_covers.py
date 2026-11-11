"""Loyihalar uchun bir xil uslubdagi brand cover'lar, og-rasmlar va sayt ikonkalarini yasaydi.

Talab: pip install -r requirements-dev.txt && python -m playwright install chromium
Ishlatish:
    python scripts/build_covers.py              # hammasi
    python scripts/build_covers.py --only lumarcos
Natija: core/static/core/projects/<slug>/cover.webp (1600x1000), og.jpg (1200x630)
        core/static/core/og-default.jpg, favicon-32.png, apple-touch-icon.png
Yangi loyiha qo'shilganda skriptni qayta ishga tushirish kifoya (mavjud galereya fayllariga tegmaydi).
"""
import argparse
import hashlib
import io
import sys
from html import escape
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from projects_data import PROJECTS  # noqa: E402

STATIC = ROOT / 'core' / 'static' / 'core'
PROJECTS_DIR = STATIC / 'projects'

# (fon boshlanishi, fon oxiri, aksent) — saytning ko'k aksentiga mos oilalar
PALETTES = [
    ('#0b1226', '#1c2f78', '#8fb0ff'),
    ('#0a1a24', '#0f4b63', '#7fe0ff'),
    ('#13112b', '#3a2a8a', '#b4a6ff'),
    ('#0b1f1c', '#0f5c52', '#7ff0d4'),
    ('#1a1226', '#5a2a7a', '#e0a8ff'),
    ('#101a2b', '#24527a', '#9fd0ff'),
]
KIND_LABEL = {'work': 'WORK · LUMARC', 'client': 'CLIENT', 'personal': 'PERSONAL', 'learning': 'LEARNING'}
FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600'
         '&family=JetBrains+Mono:wght@500&family=Manrope:wght@700;800&display=swap" rel="stylesheet">')


def palette_for(slug):
    return PALETTES[int(hashlib.md5(slug.encode()).hexdigest(), 16) % len(PALETTES)]


def cover_html(project, width, height):
    c1, c2, accent = palette_for(project['slug'])
    scale = width / 1600
    chips = ''.join(f'<span>{escape(s.strip())}</span>' for s in project.get('stack', '').split(',')[:3] if s.strip())
    title_size = (132 if len(project['title']) < 14 else 104 if len(project['title']) < 22 else 84) * scale
    return f'''<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:{width}px;height:{height}px;overflow:hidden;font-family:Inter,sans-serif;color:#eef2fb;
 background:linear-gradient(135deg,{c1} 0%,{c2} 100%);position:relative}}
.grid{{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),
 linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:{64*scale}px {64*scale}px;
 mask-image:linear-gradient(160deg,#000 0%,transparent 70%)}}
.glow{{position:absolute;right:-{200*scale}px;top:-{200*scale}px;width:{900*scale}px;height:{900*scale}px;border-radius:50%;
 background:radial-gradient(circle,{accent}55,transparent 65%)}}
.initial{{position:absolute;right:{80*scale}px;bottom:-{120*scale}px;font:800 {820*scale}px Manrope;color:{accent};opacity:.12;line-height:1}}
.wrap{{position:absolute;inset:{80*scale}px;display:flex;flex-direction:column;justify-content:space-between}}
.route{{font:500 {38*scale}px "JetBrains Mono",monospace;color:{accent};letter-spacing:.5px}}
.kind{{display:inline-block;margin-top:{16*scale}px;padding:{6*scale}px {16*scale}px;border-radius:999px;border:1px solid {accent}88;
 font:500 {28*scale}px "JetBrains Mono",monospace;color:#eef2fb;letter-spacing:1px}}
h1{{font:800 {title_size}px/1.02 Manrope,sans-serif;letter-spacing:-.02em;max-width:{1100*scale}px}}
.chips{{display:flex;flex-wrap:wrap;gap:{12*scale}px;margin-top:{34*scale}px}}
.chips span{{padding:{10*scale}px {24*scale}px;border-radius:999px;background:rgba(255,255,255,.09);border:1px solid rgba(255,255,255,.16);
 font:500 {32*scale}px "JetBrains Mono",monospace}}
</style></head><body><div class="grid"></div><div class="glow"></div>
<div class="initial">{escape(project['title'][:1])}</div>
<div class="wrap"><div><div class="route">GET /projects/{escape(project['slug'])}</div>
<span class="kind">{KIND_LABEL[project['kind']]}</span></div>
<div><h1>{escape(project['title'])}</h1><div class="chips">{chips}</div></div></div></body></html>'''


def site_html(kind):
    if kind == 'og':
        return f'''<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1200px;height:630px;font-family:Inter,sans-serif;color:#eef2fb;position:relative;overflow:hidden;
 background:linear-gradient(135deg,#0b1226,#1c2f78)}}
.glow{{position:absolute;right:-160px;top:-160px;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,#8fb0ff55,transparent 65%)}}
.wrap{{position:absolute;inset:64px;display:flex;flex-direction:column;justify-content:space-between}}
.route{{font:500 24px "JetBrains Mono";color:#8fb0ff}}
h1{{font:800 96px/1 Manrope;letter-spacing:-.03em}} h1 span{{color:#8fb0ff}}
p{{font:600 36px Manrope;margin-top:18px}} small{{font:500 22px "JetBrains Mono";color:#c4d2ff}}
</style></head><body><div class="glow"></div><div class="wrap"><div class="route">GET /me</div>
<div><h1>Dostonbek <span>Suyunov</span></h1><p>Fullstack Developer</p></div>
<small>Python · Django · Next.js · TypeScript · NestJS · AI</small></div></body></html>'''
    return '''<!doctype html><html><body style="margin:0;background:transparent">
<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
<rect width="512" height="512" rx="112" fill="#2447e8"/>
<text x="256" y="338" font-family="Manrope,Arial,sans-serif" font-weight="800" font-size="230" text-anchor="middle" fill="#fff" letter-spacing="-8">DS</text></svg></body></html>'''


def shot(page, html, width, height):
    page.set_viewport_size({'width': width, 'height': height})
    page.set_content(html, wait_until='networkidle')
    page.evaluate('document.fonts.ready')
    return Image.open(io.BytesIO(page.screenshot(type='png')))


def save_webp(img, path, max_kb=250):
    quality = 82
    while True:
        buf = io.BytesIO()
        img.convert('RGB').save(buf, 'WEBP', quality=quality, method=6)
        if buf.tell() <= max_kb * 1024 or quality <= 50:
            break
        quality -= 6
    path.write_bytes(buf.getvalue())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--only')
    args = parser.parse_args()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        for project in PROJECTS:
            if args.only and project['slug'] != args.only:
                continue
            folder = PROJECTS_DIR / project['slug']
            folder.mkdir(parents=True, exist_ok=True)
            save_webp(shot(page, cover_html(project, 1600, 1000), 1600, 1000), folder / 'cover.webp')
            og = shot(page, cover_html(project, 1200, 630), 1200, 630).convert('RGB')
            og.save(folder / 'og.jpg', 'JPEG', quality=85, optimize=True)
            print('cover:', project['slug'])
        if not args.only:
            shot(page, site_html('og'), 1200, 630).convert('RGB').save(STATIC / 'og-default.jpg', 'JPEG', quality=85, optimize=True)
            icon = shot(page, site_html('icon'), 512, 512)
            icon.resize((180, 180), Image.LANCZOS).save(STATIC / 'apple-touch-icon.png')
            icon.resize((32, 32), Image.LANCZOS).save(STATIC / 'favicon-32.png')
            icon.save(STATIC / 'icon-512.png')
            icon.resize((192, 192), Image.LANCZOS).save(STATIC / 'icon-192.png')
            print('site assets done')
        browser.close()


if __name__ == '__main__':
    main()
