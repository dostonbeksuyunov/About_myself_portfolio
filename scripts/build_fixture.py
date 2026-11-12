"""scripts/projects_data.py dan core/fixtures/projects.json yig'adi.

Ishlatish:  python scripts/build_fixture.py
Keyin:      python manage.py loaddata projects     (idempotent). Yangi loyihaga yangi (ishlatilmagan) pk bering.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from projects_data import PROJECTS  # noqa: E402

sys.path.insert(0, str(ROOT))
from core.orthography import uz_latin  # noqa: E402

LANGS = ('uz', 'ru', 'en')
MEDIA_ROOT = ROOT / 'core' / 'static' / 'core' / 'projects'


def gallery_for(slug):
    folder = MEDIA_ROOT / slug
    if not folder.is_dir():
        return []
    return [f'core/projects/{slug}/{p.name}' for p in sorted(folder.glob('gallery-*.webp'))]


def build():
    rows = []
    assert len({p['pk'] for p in PROJECTS}) == len(PROJECTS), 'pk lar takrorlanmasligi kerak'
    for p in PROJECTS:
        pk = p['pk']  # barqaror: loyiha o'chirilsa yoki qo'shilsa boshqalarning pk si o'zgarmaydi
        slug = p['slug']
        fields = {
            'slug': slug,
            'order': p['order'],
            'is_featured': p.get('featured', False),
            'is_published': True,
            'kind': p['kind'],
            'categories': p.get('categories', ''),
            'year_start': p['year_start'],
            'year_end': p.get('year_end'),
            'ongoing': p.get('ongoing', False),
            'status': p['status'],
            'confidential': p.get('confidential', False),
            'title': p['title'],
            'stack': p.get('stack', ''),
            'live_url': p.get('live_url', ''),
            'telegram_url': p.get('telegram_url', ''),
            'github_url': p.get('github_url', ''),
            'cover': f'core/projects/{slug}/cover.webp' if (MEDIA_ROOT / slug / 'cover.webp').exists() else '',
            'gallery': '\n'.join(gallery_for(slug)),
        }
        for i, lang in enumerate(LANGS):
            fields[f'role_{lang}'] = p['role'][i]
            fields[f'short_{lang}'] = p['short'][i]
            for key in ('problem', 'solution', 'result'):
                fields[f'{key}_{lang}'] = p.get(key, ('', '', ''))[i]
            fields[f'highlights_{lang}'] = '\n'.join(p['highlights'][i])
        rows.append({'model': 'core.project', 'pk': pk, 'fields': fields})
    # o'zbekcha maydonlar yangilangan lotin imlosida saqlanadi
    for row in rows:
        for name, value in row['fields'].items():
            if name.endswith('_uz') and isinstance(value, str):
                row['fields'][name] = uz_latin(value)
    out = ROOT / 'core' / 'fixtures' / 'projects.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'{len(rows)} ta loyiha -> {out.relative_to(ROOT)}')


if __name__ == '__main__':
    build()
