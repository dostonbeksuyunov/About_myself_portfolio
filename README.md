# Dostonbek Suyunov — portfolio

Django 5.2 da yozilgan shaxsiy portfolio: bosh sahifa, loyihalar ro'yxati (`/projects/`) va har bir
loyiha uchun keys sahifasi (`/projects/<slug>/`). Til: uz / ru / en (`?lang=`), mavzu: kunduzgi / tungi.

## Lokal ishga tushirish

```bash
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt     # Linux/macOS: .venv/bin/pip
copy .env.example .env                                           # SECRET_KEY ni o'zgartiring
python manage.py migrate
python manage.py loaddata projects                               # loyihalarni bazaga yuklaydi (qayta yuklash xavfsiz)
python manage.py runserver 8010
```

Sayt: http://127.0.0.1:8010 · Admin: http://127.0.0.1:8010/admin/ (`createsuperuser` bilan).

Testlar: `python manage.py test` · Tekshiruv: `python manage.py check`.

## Yangi loyiha qanday qo'shiladi

**1-yo'l — admin orqali** (kod yozmasdan): `/admin/` → *Projects* → *Add*. Matn maydonlari har til uchun
alohida (`short_uz/ru/en`, `problem_*`, `solution_*`, `result_*`, `highlights_*` — har qator bitta band).
`kind`: work / client / personal / learning. `categories`: vergul bilan `web, bot, ai, backend, 3d, automation`.
`stack` — vergul bilan. `confidential` belgilansa havolalar va galereya ko'rsatilmaydi.
`order` kichik bo'lsa — yuqorida. `is_published` o'chirilsa — sahifa 404 beradi.

**2-yo'l — fixture orqali** (tavsiya: ma'lumot git'da saqlanadi):
1. `scripts/projects_data.py` ga yangi obyektni qo'shing va unga **yangi `pk`** bering (ishlatilmagan eng katta raqamdan keyingi).
   `pk` barqaror: loyiha o'chirilsa boshqalarniki o'zgarmaydi. Loyihani butunlay olib tashlash uchun: obyektni ro'yxatdan
   o'chiring, `core/static/core/projects/<slug>/` papkasini o'chiring va slug'ni o'chiruvchi data-migratsiya yozing
   (namuna: `core/migrations/0002_remove_online_book_store.py`) — `loaddata` mavjud qatorni o'chirmaydi.
2. `python scripts/build_covers.py --only <slug>` — cover (`cover.webp`, `cover-800.webp`) va `og.jpg` yasaydi.
3. (ixtiyoriy) galereya rasmlarini `core/static/core/projects/<slug>/gallery-1.webp, gallery-2.webp…` ga qo'ying
   yoki `scripts/build_screens.py` ga ochiq URL / mockup qo'shing.
4. `python scripts/build_fixture.py` → `core/fixtures/projects.json` yangilanadi, so'ng `python manage.py loaddata projects`.

Rasm qoidalari: `core/static/core/projects/<slug>/` ichida WebP (sifat ~82), har biri ≤ 250 KB;
cover 1600×1000, og.jpg 1200×630. Rasm `ImageField` emas — static yo'l (prod'da media whitenoise orqali berilmaydi).

Skriptlar uchun: `pip install -r requirements-dev.txt && python -m playwright install chromium`.

| Skript | Vazifasi |
|---|---|
| `scripts/build_fixture.py` | `projects_data.py` → `core/fixtures/projects.json` |
| `scripts/build_covers.py` | brand cover, og-rasm, favicon va ikonkalar |
| `scripts/build_screens.py` | ochiq sahifa skrinshotlari, bot mockup'lari, diagrammalar |
| `scripts/check_links.py` | ishlab turgan saytdagi barcha havolalarni tekshiradi |

## Sozlamalar (`.env`)

| O'zgaruvchi | Izoh |
|---|---|
| `SECRET_KEY`, `DEBUG` | Django |
| `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS` | domen va IP lar (vergul bilan) |
| `SITE_URL` | kanonik URL, sitemap va Open Graph uchun, masalan `https://suyunovdev.uz` |
| `SECURE_SSL_REDIRECT`, `SECURE_HSTS_SECONDS` | HTTPS sozlanmagan serverda `SECURE_SSL_REDIRECT=False` |

## Deploy (qisqacha)

```bash
git pull
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata projects
python manage.py collectstatic --noinput
sudo systemctl restart gunicorn
```
