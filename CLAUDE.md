# CLAUDE.md — portfolio (Django 5.2)

## Buyruqlar
- Test: `python manage.py test` (80 ta; `projects` fixture'ini ishlatadi) · Tekshiruv: `python manage.py check`
- Lokal: `python manage.py migrate && python manage.py loaddata projects && python manage.py runserver 8010`
- Prod-ga o'xshash tekshiruv: `DEBUG=False SECURE_SSL_REDIRECT=False python manage.py collectstatic --noinput` so'ng runserver
- Havolalar: `python scripts/check_links.py http://127.0.0.1:8010`

## Tuzilma
- `core/models.py` — `Project` (3 tilli maydonlar `*_uz/ru/en`, kind, status, categories, stack, confidential, cover/gallery static yo'llari).
- `core/content.py` — UI matnlari (`_STRINGS`: kalit → (uz, ru, en)), `SKILLS`, `SERVICES`, `TIMELINE`, `CONTACT`. Loyihalar bu yerda EMAS.
- `core/views.py` — home, project_list (filtrlar `?kind=&cat=`, server tomonda), project_detail, robots, sitemap, 404/500.
- `core/context_processors.py` — til (`?lang=` > sessiya > uz), `t`, canonical/hreflang, `SITE_URL`.
- `core/templates/core/` — base, home, project_list, project_detail, `_project_card`, `_icons` (SVG sprite).
- `core/static/core/css/style.css` — faqat CSS tokenlari (`:root[data-theme=light|dark]`); qattiq yozilgan rang qo'shmang.
- `scripts/projects_data.py` → `core/fixtures/projects.json` (har loyihada barqaror `pk`; yangisiga yangi pk bering; o'chirish — data-migratsiya bilan).

## Qoidalar
- Loyiha matnlarida faqat haqiqiy faktlar (README/CLAUDE.md/kod asosida); raqam, foydalanuvchi soni, tezlik o'ylab topilmaydi.
- Ish loyihalari uchun GitHub havolasi qo'yilmaydi. Boshqa loyihada faqat repo ochiq bo'lsa (curl 200) qo'yiladi; yopiq repo → "Kod yopiq" belgisi.
- Live havola qo'yishdan oldin ochilishini tekshiring. Maxfiy loyihada `confidential=True`.
- Ish shartnomasi, bandlik turi, sinov muddati haqida saytda yozilmaydi (faqat lavozim, firma, sana, ishlar).
- "vibe coding" iborasi ishlatilmaydi.
- `.env`, token, server IP/kalitlar commit qilinmaydi; domen faqat `SITE_URL` env orqali.
- Media: WebP ≤ 250 KB; `{% static %}` yo'llari; rasmlarda `width/height` va `loading="lazy"` (birinchi ekrandagi rasmdan tashqari).
- Shriftlar o'z serverimizda (`core/static/core/fonts`, `css/fonts.css`); yangilash: `python scripts/fetch_fonts.py`. Google Fonts'ga tashqi so'rov qo'shmang.
- Mavzu faqat 2 ta: light / dark. `<head>` dagi inline skript `data-theme` ni CSS dan oldin qo'yadi (FOUC yo'q).
