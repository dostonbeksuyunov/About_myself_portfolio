"""Google Fonts shriftlarini o'z serverimizga ko'chiradi (tashqi so'rovsiz, tezroq va barqaror).

Natija: core/static/core/fonts/*.woff2 va core/static/core/css/fonts.css (unicode-range bilan).
Faqat kerakli to'plamlar: latin, latin-ext (o', g' belgilari), cyrillic (ru tili).
Ishlatish: python scripts/fetch_fonts.py
"""
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTS_DIR = ROOT / 'core' / 'static' / 'core' / 'fonts'
CSS_OUT = ROOT / 'core' / 'static' / 'core' / 'css' / 'fonts.css'

# (oila, Google so'rovi, fayl prefiksi)
FAMILIES = [
    ('Inter', 'Inter:wght@400..600', 'inter'),
    ('JetBrains Mono', 'JetBrains+Mono:wght@400..500', 'jetbrains-mono'),
    ('Manrope', 'Manrope:wght@600..800', 'manrope'),
]
SUBSETS = ('cyrillic', 'latin-ext', 'latin')
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36'


def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def main():
    FONTS_DIR.mkdir(parents=True, exist_ok=True)
    blocks = []
    for family, query, prefix in FAMILIES:
        css = get(f'https://fonts.googleapis.com/css2?family={query}&display=swap').decode('utf-8')
        for subset, body in re.findall(r'/\* ([a-z-]+) \*/\s*(@font-face \{.*?\})', css, re.S):
            if subset not in SUBSETS:
                continue
            url = re.search(r'src: url\((https://[^)]+\.woff2)\)', body).group(1)
            name = f'{prefix}-{subset}.woff2'
            (FONTS_DIR / name).write_bytes(get(url))
            body = re.sub(r'src: url\([^)]+\) format\(\'woff2\'\);', f"src: url('../fonts/{name}') format('woff2');", body)
            blocks.append(f'/* {family} {subset} */\n{body}')
            print('ok', name, (FONTS_DIR / name).stat().st_size // 1024, 'KB')
    CSS_OUT.write_text('/* Avtomatik yaratilgan: python scripts/fetch_fonts.py */\n' + '\n'.join(blocks) + '\n', encoding='utf-8')
    print('->', CSS_OUT.relative_to(ROOT))


if __name__ == '__main__':
    main()
