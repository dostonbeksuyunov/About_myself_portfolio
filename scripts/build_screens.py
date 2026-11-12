"""Galereya rasmlarini yasaydi: ochiq sahifalardan skrinshot, bot chat mockup'lari va diagrammalar.

Faqat ochiq (login talab qilmaydigan) sahifalar olinadi. Mockup va diagrammalar rasmda
"MOCKUP" / "DIAGRAM" deb belgilanadi; matnlar botlarning haqiqiy matn fayllaridan olingan,
statistik raqamlar yo'q.
Ishlatish: python scripts/build_screens.py [--only slug]
"""
import argparse
import io
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
PROJECTS = ROOT / 'core' / 'static' / 'core' / 'projects'

LIVE = {
    'lumarcos': [('https://lumarcos.uz', 1440, 900), ('https://lumarcos.uz', 390, 844)],
    'lumarcode': [('https://akromin.uz', 1440, 900)],
    'bahober': [('https://bahober.uz', 1440, 900), ('https://bahober.uz', 390, 844)],
    'lumarc-sayt': [('https://lumarc.uz', 1440, 900), ('https://lumarc.uz', 390, 844)],
}

STROY = 'https://uzstroymarket.uz'
STROY_THEME_KEY = 'stroymarkett.theme'  # saytning o'z mavzu kaliti (localStorage)


def phone_frame(shot):
    """Mobil skrinshotni gradient fon ustida telefon ramkasiga joylaydi (1600x1000)."""
    from PIL import ImageDraw
    canvas = Image.new('RGB', (1600, 1000), '#0b1226')
    grad = Image.new('RGB', (1600, 1000))
    px = grad.load()
    for y in range(1000):
        for x in range(0, 1600, 8):
            t = (x / 1600 + y / 1000) / 2
            color = (int(11 + 17 * t), int(18 + 29 * t), int(38 + 82 * t))
            for dx in range(8):
                px[x + dx, y] = color
    canvas.paste(grad)
    height = 860
    width = round(shot.width * height / shot.height)
    shot = shot.resize((width, height), Image.LANCZOS).convert('RGB')
    mask = Image.new('L', shot.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, width, height), radius=34, fill=255)
    x, y = (1600 - width) // 2, (1000 - height) // 2
    ImageDraw.Draw(canvas).rounded_rectangle((x - 12, y - 12, x + width + 12, y + height + 12), radius=46, fill='#1d2a3d')
    canvas.paste(shot, (x, y), mask)
    return canvas


AKROMIND = 'https://akromind.uz'


def capture_akromind(browser):
    """Akromind: bosh sahifa (kunduzgi va tungi rejim), loyihalar sahifasi va mobil ko'rinish."""
    images = []
    shots = [('/', 1440, 900, 'light'), ('/', 1440, 900, 'dark'), ('/loyihalar', 1440, 900, 'light'), ('/', 390, 844, 'light')]
    for path, w, h, mode in shots:
        ctx = browser.new_context(viewport={'width': w, 'height': h}, reduced_motion='reduce')
        ctx.add_init_script(f"try{{localStorage.setItem('akromind-mode','{mode}')}}catch(e){{}}")
        page = ctx.new_page()
        try:
            page.goto(AKROMIND + path, wait_until='domcontentloaded', timeout=45000)
            page.wait_for_timeout(4500)
            raw = Image.open(io.BytesIO(page.screenshot(type='png')))
            images.append(phone_frame(raw) if w < 600 else fit(raw))
        except Exception as exc:
            print(f'  ! {AKROMIND}{path} ({w}px, {mode}): {type(exc).__name__}')
        ctx.close()
    return images


def capture_stroy(browser):
    """Faqat ochiq sahifalar: bosh sahifa va kirish sahifasi (kunduzgi/tungi) hamda mobil ko'rinish.
    Katalog, mahsulot va panellar login talab qiladi — olinmaydi."""
    images = []

    def snap(path, w, h, theme):
        ctx = browser.new_context(viewport={'width': w, 'height': h}, reduced_motion='reduce', color_scheme=theme)
        ctx.add_init_script(f"try{{localStorage.setItem('{STROY_THEME_KEY}','{theme}')}}catch(e){{}}")
        page = ctx.new_page()
        try:
            page.goto(STROY + path, wait_until='load', timeout=45000)
            page.wait_for_timeout(3500)
            raw = Image.open(io.BytesIO(page.screenshot(type='png')))
            return phone_frame(raw) if w < 600 else fit(raw)
        except Exception as exc:
            print(f'  ! {STROY}{path} ({w}px, {theme}): {type(exc).__name__}')
            return None
        finally:
            ctx.close()

    shots = [('/', 1440, 900, 'light'), ('/', 1440, 900, 'dark'), ('/login', 1440, 900, 'light'),
             ('/login', 1440, 900, 'dark'), ('/', 390, 844, 'light'), ('/', 390, 844, 'dark')]
    for path, w, h, theme in shots:
        img = snap(path, w, h, theme)
        if img is not None:
            images.append(img)
    return images



FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600'
         '&family=JetBrains+Mono:wght@500&family=Manrope:wght@700;800&display=swap" rel="stylesheet">')

PHONE_CSS = '''
*{box-sizing:border-box;margin:0;padding:0}
body{width:1600px;height:1000px;font-family:Inter,sans-serif;display:flex;align-items:center;justify-content:center;
 background:linear-gradient(135deg,#0b1226,#1c2f78);position:relative}
.tag{position:absolute;top:36px;left:44px;font:500 22px "JetBrains Mono";color:#9fb6ff;letter-spacing:1px}
.phone{width:470px;height:880px;border-radius:56px;background:#0e1621;border:10px solid #1d2a3d;display:flex;flex-direction:column;overflow:hidden}
.head{padding:22px 26px;background:#17212b;color:#e8eef5;font:600 24px Inter;border-bottom:1px solid #0b121a}
.head small{display:block;font:400 16px Inter;color:#7f91a4;margin-top:2px}
.chat{flex:1;padding:22px 18px;display:flex;flex-direction:column;gap:14px;justify-content:flex-end}
.msg{max-width:86%;padding:14px 18px;border-radius:20px;font-size:19px;line-height:1.4;white-space:pre-wrap;color:#e8eef5}
.bot{background:#182533;align-self:flex-start;border-bottom-left-radius:6px}
.me{background:#2b5278;align-self:flex-end;border-bottom-right-radius:6px}
.btns{display:grid;grid-template-columns:1fr 1fr;gap:8px;align-self:flex-start;width:86%}
.btns span{background:#223244;border-radius:12px;padding:11px;text-align:center;font-size:18px;color:#8fb0ff}
b{font-weight:600}
'''


def phone_html(title, subtitle, messages):
    body = ''
    for kind, text, *buttons in messages:
        body += f'<div class="msg {kind}">{text}</div>'
        if buttons:
            body += '<div class="btns">' + ''.join(f'<span>{b}</span>' for b in buttons[0]) + '</div>'
    return (f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{PHONE_CSS}</style></head><body>'
            f'<div class="tag">MOCKUP · real bot matnlari asosida</div>'
            f'<div class="phone"><div class="head">{title}<small>{subtitle}</small></div>'
            f'<div class="chat">{body}</div></div></body></html>')


def diagram_html(title, steps):
    boxes = ''.join(
        f'<div class="box"><b>{name}</b><span>{desc}</span></div>' + ('<div class="arr">→</div>' if i < len(steps) - 1 else '')
        for i, (name, desc) in enumerate(steps)
    )
    return f'''<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1600px;height:1000px;font-family:Inter,sans-serif;color:#eef2fb;background:linear-gradient(135deg,#0b1226,#1c2f78);
 display:flex;flex-direction:column;justify-content:center;padding:0 80px;gap:56px}}
.tag{{font:500 22px "JetBrains Mono";color:#9fb6ff;letter-spacing:1px}}
h1{{font:800 56px Manrope;letter-spacing:-.02em}}
.row{{display:flex;align-items:stretch;gap:16px}}
.box{{flex:1;padding:28px 24px;border-radius:20px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18);
 display:flex;flex-direction:column;gap:10px}}
.box b{{font:700 28px Manrope}} .box span{{font-size:20px;line-height:1.4;color:#c8d4f0}}
.arr{{align-self:center;font:700 38px Manrope;color:#8fb0ff}}
</style></head><body><div class="tag">DIAGRAM</div><h1>{title}</h1><div class="row">{boxes}</div></body></html>'''


MOCKUPS = {
    'moneyflow': phone_html('MoneyFlow', 'bot', [
        ('bot', "👋 Hi! I'm <b>MoneyFlow</b> — your assistant for tracking personal and business money flow.\n\n💸 Log income and expenses, view daily/weekly/monthly/yearly reports, export to Excel and PDF."),
        ('bot', "• <b>yolkira 10000</b>\n• <b>taksi 15 ming</b>\n• <b>tushum 200000 do'kon</b>\n• <b>oylik 5 mln</b>"),
        ('me', 'taksi 15 ming'),
        ('bot', '✅ Saved'),
    ]),
    'saveclip': phone_html('SaveClip', 'bot', [
        ('bot', "👋 <b>Salom!</b>\n\nMen <b>SaveClip</b> — video yuklovchi botman. 🎬\nMenga havola yuboring, men uni yuklab beraman.\n\n<b>Qo'llab-quvvatlanadi:</b> Instagram, TikTok, Twitter/X, Pinterest"),
        ('me', 'https://www.instagram.com/reel/…  (namuna havola)'),
        ('bot', '🔎 Havola tekshirilmoqda...'),
        ('bot', '🎞 <b>Video</b>\n\nSifatni tanlang:', ['HD', '2K', '4K', "🎵 Qo'shiqni yuklab olish"]),
    ]),
    'e-auksion-radar': phone_html('Тошкент лот радари', 'telegram', [
        ('bot', '🏙 <b>Тошкент — янги лотлар</b>\n\n📌 Бу сафар: N та лот'),
        ('bot', '🔻 <b>НАРХ ТУШДИ</b> — олдинги нарх кўрсатилади\n📋 Шартли лот\n\nҲар бир лот: нарх, майдон, ҳудуд, ўхшаш лотлар билан таққослаш ва ball.'),
        ('bot', '✅ <b>Ҳисобот якуни</b>'),
    ]),
}

DIAGRAMS = {
    'e-auksion-radar': diagram_html('Lot radari: jarayon', [
        ('e-auksion.uz', 'Toshkent va tutash tumanlar lotlari'), ('Yig\'ish', 'haftasiga 2 marta'),
        ('Saralash', 'mezonlar.json bo\'yicha'), ('Ball', 'narx solishtiruvi va baholash'),
        ('Telegram', 'TOP-10 tahlili bilan')]),
    'lumarcode': diagram_html('Lumarcode: arxitektura', [
        ('Telegram bot + Veb-UI', 'chat va kod rejimi'), ('Caddy', 'HTTPS, tashqi kirish'),
        ('Docker konteyner', 'izolyatsiyalangan, sirlar obrazdan tashqarida'), ('Claude', 'AI ish muhiti')]),
}


def save_webp(img, path, max_kb=250):
    quality = 82
    while True:
        buf = io.BytesIO()
        img.convert('RGB').save(buf, 'WEBP', quality=quality, method=6)
        if buf.tell() <= max_kb * 1024 or quality <= 50:
            break
        quality -= 6
    path.write_bytes(buf.getvalue())


def fit(img):
    """1600x1000 ga markazdan qirqib, moslashtiradi (skrinshotlar uchun)."""
    target = 1.6
    w, h = img.size
    if w / h > target:
        nw = int(h * target)
        img = img.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    else:
        nh = int(w / target)
        img = img.crop((0, 0, w, nh))
    return img.resize((1600, 1000), Image.LANCZOS)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--only')
    args = parser.parse_args()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        results = {}
        slugs = set(LIVE) | set(MOCKUPS) | set(DIAGRAMS) | {'uzstroymarket', 'akromind'}
        for slug in sorted(slugs):
            if args.only and slug != args.only:
                continue
            images = []
            if slug == 'uzstroymarket':
                images += capture_stroy(browser)
            if slug == 'akromind':
                images += capture_akromind(browser)
            for url, w, h in LIVE.get(slug, []):
                ctx = browser.new_context(viewport={'width': w, 'height': h}, reduced_motion='reduce')
                page = ctx.new_page()
                try:
                    page.goto(url, wait_until='networkidle', timeout=30000)
                    page.wait_for_timeout(1200)
                    images.append(fit(Image.open(io.BytesIO(page.screenshot(type='png')))))
                except Exception as exc:  # sayt ochilmasa — shu rasm o'tkazib yuboriladi
                    print(f'  ! {url} ({w}px): {type(exc).__name__}')
                ctx.close()
            for html in [MOCKUPS.get(slug), DIAGRAMS.get(slug)]:
                if html:
                    page = browser.new_page(viewport={'width': 1600, 'height': 1000})
                    page.set_content(html, wait_until='networkidle')
                    page.evaluate('document.fonts.ready')
                    images.append(Image.open(io.BytesIO(page.screenshot(type='png'))))
                    page.close()
            folder = PROJECTS / slug
            folder.mkdir(parents=True, exist_ok=True)
            for old in folder.glob('gallery-*.webp'):
                old.unlink()
            for i, img in enumerate(images, start=1):
                save_webp(img, folder / f'gallery-{i}.webp')
            results[slug] = len(images)
            print(slug, len(images))
        browser.close()


if __name__ == '__main__':
    main()
