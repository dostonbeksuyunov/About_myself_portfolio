"""Loyihalar ma'lumotlari — core/fixtures/projects.json shu fayldan yig'iladi.

Faqat haqiqiy faktlar yoziladi (README / CLAUDE.md / kod asosida). Raqamlar,
foydalanuvchi soni, tezlik kabi ma'lumotlar hujjatda bo'lmasa yozilmaydi.
Tahrirlagach:  python scripts/build_fixture.py
Har bir matn maydoni (uz, ru, en) tartibida beriladi; highlights — qatorlar ro'yxati.
"""

LUMARC = 'work'
CLIENT = 'client'
PERSONAL = 'personal'
LEARNING = 'learning'

PROJECTS = [
    # ------------------------------------------------------------ ISH — LUMARC
    dict(
        slug='lumarc-sayt', title='Lumarc', kind=LUMARC, order=10, featured=True,
        categories='web,3d', year_start=2026, ongoing=True, status='live',
        stack='Next.js 16, React 19, TypeScript, NestJS 11, Prisma, PostgreSQL, Three.js, Photo Sphere Viewer',
        role=("Fullstack dasturchi", "Fullstack-разработчик", "Fullstack Developer"),
        short=(
            "Arxitektura va dizayn studiyasining kompaniya sayti: loyihalar katalogi, 360° virtual turlar va admin panel.",
            "Сайт архитектурно-дизайнерской студии: каталог проектов, виртуальные туры 360° и админ-панель.",
            "Company website of an architecture and design studio: project catalog, 360° virtual tours and an admin panel.",
        ),
        problem=(
            "Studiya o'z ishlarini zamonaviy ko'rinishda ko'rsatishi va kontentni dasturchisiz yangilab turishi kerak edi.",
            "Студии нужно было современно показывать свои работы и обновлять контент без участия разработчика.",
            "The studio needed to showcase its work in a modern way and update content without a developer.",
        ),
        solution=(
            "Next.js ilova va NestJS API ajratildi: ochiq katalog faol loyihalarni API'dan oladi, admin panel orqali loyiha, blog, jamoa va murojaatlar boshqariladi. Loyiha sahifalarida 360° tur va 3D sahnalar bor.",
            "Next.js-приложение и NestJS API разделены: публичный каталог берёт активные проекты из API, через админ-панель управляются проекты, блог, команда и обращения. На страницах проектов есть туры 360° и 3D-сцены.",
            "A Next.js app and a NestJS API are split: the public catalog reads active projects from the API, while the admin panel manages projects, blog, team and inquiries. Project pages include 360° tours and 3D scenes.",
        ),
        result=(
            "Sayt jonli ishlaydi; yangi dizayn (redesign) hozir ishlab chiqilmoqda.",
            "Сайт работает; новый дизайн (редизайн) сейчас в разработке.",
            "The site is live; a new design (redesign) is currently in progress.",
        ),
        highlights=(
            ["Uch tilli sayt (uz / ru / en)", "Scroll-story hero va loyiha sahifalari", "360° virtual tur (Photo Sphere Viewer) va Three.js sahnalari", "Admin panel: loyihalar, blog, jamoa, murojaatlar, fayl yuklash", "SEO: sitemap, robots, JSON-LD; API uzilsa — aniq xato holati va qayta urinish"],
            ["Три языка (uz / ru / en)", "Scroll-story hero и страницы проектов", "Виртуальные туры 360° (Photo Sphere Viewer) и сцены Three.js", "Админ-панель: проекты, блог, команда, обращения, загрузка файлов", "SEO: sitemap, robots, JSON-LD; при сбое API — понятное состояние ошибки и повтор"],
            ["Three languages (uz / ru / en)", "Scroll-story hero and project pages", "360° virtual tours (Photo Sphere Viewer) and Three.js scenes", "Admin panel: projects, blog, team, inquiries, file uploads", "SEO: sitemap, robots, JSON-LD; explicit error state with retry when the API is down"],
        ),
    ),
    dict(
        slug='lumarcos', title='Lumarcos', kind=LUMARC, order=20, featured=True,
        categories='ai,web,backend', year_start=2026, ongoing=True, status='live',
        live_url='https://lumarcos.uz',
        stack='Next.js 16, React 19, NestJS 11, Prisma, PostgreSQL, BullMQ, Redis, MinIO, Docker Compose, Caddy, Gemini / Vertex AI, fal.ai',
        role=("Fullstack dasturchi", "Fullstack-разработчик", "Fullstack Developer"),
        short=(
            "Arxitektorlar uchun AI platforma: renderlarga post-production, Image Studio va rasm/video generatsiya.",
            "AI-платформа для архитекторов: постпродакшн рендеров, Image Studio и генерация изображений и видео.",
            "An AI platform for architects: render post-production, Image Studio and image/video generation.",
        ),
        problem=(
            "Arxitektorlar render natijalarini qo'lda qayta ishlashga ko'p vaqt sarflaydi; generativ AI vositalari esa tarqoq.",
            "Архитекторы тратят много времени на ручную доработку рендеров, а инструменты генеративного ИИ разрознены.",
            "Architects spend a lot of time retouching renders by hand, and generative AI tools are scattered.",
        ),
        solution=(
            "Bitta platformada Post-Pro (render ishlov), Image Studio va Generate bo'limlari: AI so'rovlari navbat (BullMQ + Redis) orqali bajariladi, fayllar S3-mos omborda saqlanadi, foydalanish kredit tizimi va to'lov orqali boshqariladi.",
            "В одной платформе разделы Post-Pro (обработка рендеров), Image Studio и Generate: AI-запросы выполняются через очередь (BullMQ + Redis), файлы хранятся в S3-совместимом хранилище, использование регулируется кредитами и оплатой.",
            "One platform with Post-Pro (render processing), Image Studio and Generate sections: AI requests run through a queue (BullMQ + Redis), files live in S3-compatible storage, and usage is governed by a credit and payment system.",
        ),
        result=(
            "Platforma lumarcos.uz da jonli ishlaydi: kirish (OTP / email), kredit va to'lov (Payme, Click), admin panel va CI (lint, build, test, e2e) bilan.",
            "Платформа работает на lumarcos.uz: вход (OTP / email), кредиты и оплата (Payme, Click), админ-панель и CI (lint, build, тесты, e2e).",
            "The platform runs live at lumarcos.uz with sign-in (OTP / email), credits and payments (Payme, Click), an admin panel and CI (lint, build, tests, e2e).",
        ),
        highlights=(
            ["pnpm monorepo: NestJS API, Next.js web va umumiy paket", "Gemini / Vertex AI va fal.ai integratsiyasi", "BullMQ navbati, MinIO (S3) ombor, sharp bilan rasm ishlov", "Kredit va to'lov (Payme, Click), admin panel", "Docker Compose + Caddy (HTTPS), deploy skripti; Playwright e2e smoke"],
            ["pnpm-монорепо: NestJS API, Next.js web и общий пакет", "Интеграция Gemini / Vertex AI и fal.ai", "Очередь BullMQ, хранилище MinIO (S3), обработка изображений sharp", "Кредиты и оплата (Payme, Click), админ-панель", "Docker Compose + Caddy (HTTPS), скрипт деплоя; Playwright e2e smoke"],
            ["pnpm monorepo: NestJS API, Next.js web and a shared package", "Gemini / Vertex AI and fal.ai integration", "BullMQ queue, MinIO (S3) storage, image processing with sharp", "Credits and payments (Payme, Click), admin panel", "Docker Compose + Caddy (HTTPS), deploy script; Playwright e2e smoke"],
        ),
    ),
    dict(
        slug='e-auksion-radar', title="E-auksion lot radari", kind=LUMARC, order=30, featured=True,
        categories='bot,automation,backend', year_start=2026, ongoing=True, status='live',
        stack='Python (standart kutubxona), SQLite, Telegram Bot API, unittest',
        role=("Fullstack dasturchi", "Fullstack-разработчик", "Fullstack Developer"),
        short=(
            "e-auksion.uz dagi Toshkent lotlarini avtomatik yig'ib, saralab, eng yaxshi 10 tasini Telegram'ga yuboradigan bot.",
            "Бот, который автоматически собирает лоты Ташкента с e-auksion.uz, фильтрует их и отправляет лучшие 10 в Telegram.",
            "A bot that automatically collects Tashkent lots from e-auksion.uz, screens them and sends the best 10 to Telegram.",
        ),
        problem=(
            "Auksion platformasida minglab lot bor — mos keladiganlarini qo'lda kuzatib borish juda ko'p vaqt oladi.",
            "На аукционной платформе тысячи лотов — отслеживать подходящие вручную слишком долго.",
            "The auction platform lists thousands of lots, and watching for the relevant ones by hand takes too long.",
        ),
        solution=(
            "Dastur haftasiga ikki marta lotlarni yig'adi, mezonlar fayli bo'yicha saralaydi, narxni boshqa lotlar bilan solishtiradi, ball beradi va TOP-10 ni tahlili bilan Telegram'ga yuboradi. Yuborilgan lot narxi tushmaguncha qayta kelmaydi.",
            "Программа дважды в неделю собирает лоты, фильтрует по файлу критериев, сравнивает цены с другими лотами, начисляет баллы и отправляет ТОП-10 с анализом в Telegram. Отправленный лот не приходит повторно, пока не упадёт цена.",
            "Twice a week the program collects lots, screens them by a criteria file, compares prices with other lots, scores them and sends the TOP-10 with analysis to Telegram. A lot that was already sent is not repeated unless its price drops.",
        ),
        result=(
            "Serverda jadval bo'yicha real ishlab turibdi. Kod faqat Python standart kutubxonasiga tayanadi va 200 dan ortiq avtomatik test bilan qoplangan.",
            "Работает на сервере по расписанию. Код опирается только на стандартную библиотеку Python и покрыт более чем 200 автоматическими тестами.",
            "Runs on a server on a schedule. The code relies only on the Python standard library and is covered by 200+ automated tests.",
        ),
        highlights=(
            ["Mezonlar JSON faylida: mulk guruhi, toifa, boshlang'ich narx, to'lov shartlari", "Narx solishtiruvi va ball tizimi", "Takroriy lotlarni filtrlash (SQLite)", "Dry-run rejimi va jurnal; tashqi bog'liqliklar yo'q"],
            ["Критерии в JSON: группа имущества, категория, начальная цена, условия оплаты", "Сравнение цен и система баллов", "Фильтрация повторных лотов (SQLite)", "Режим dry-run и журнал; внешних зависимостей нет"],
            ["Criteria in JSON: property group, category, starting price, payment terms", "Price comparison and a scoring system", "Duplicate-lot filtering (SQLite)", "Dry-run mode and logging; no external dependencies"],
        ),
    ),
    dict(
        slug='lumarcode', title='Lumarcode', kind=LUMARC, order=40, featured=True,
        categories='ai,backend,automation', year_start=2026, ongoing=True, status='live',
        live_url='https://akromin.uz',
        stack='Claude, Docker, Caddy, Telegram bot, Linux',
        role=("Fullstack dasturchi", "Fullstack-разработчик", "Fullstack Developer"),
        short=(
            "Jamoa uchun Claude asosidagi ichki AI ish platformasi: chat va kod rejimi, Telegram bot va veb-interfeys.",
            "Внутренняя AI-платформа для команды на базе Claude: режимы чата и кода, Telegram-бот и веб-интерфейс.",
            "An internal Claude-based AI workspace for the team: chat and code modes, a Telegram bot and a web UI.",
        ),
        problem=(
            "Jamoa AI vositasidan xavfsiz, bir joydan foydalanishi va boshqa servislarga tegmasligi kerak edi.",
            "Команде нужен был безопасный единый доступ к AI-инструменту без влияния на соседние сервисы.",
            "The team needed safe, single-point access to an AI tool without affecting neighbouring services.",
        ),
        solution=(
            "Ilova production serverda alohida Docker konteynerda izolyatsiyada ishga tushirilgan: sirlar obrazdan tashqarida saqlanadi, tashqi kirish Caddy orqali HTTPS bilan beriladi, ishga tushirish va ekspluatatsiya qarorlari ADR hujjatlarida yozilgan.",
            "Приложение запущено на продакшн-сервере в отдельном Docker-контейнере в изоляции: секреты хранятся вне образа, внешний доступ отдаётся через Caddy по HTTPS, решения по запуску и эксплуатации описаны в ADR.",
            "The app runs on the production server in its own isolated Docker container: secrets are kept outside the image, external access goes through Caddy over HTTPS, and launch and operations decisions are documented as ADRs.",
        ),
        result=(
            "Platforma ishlaydi; kirish faqat xodimlar uchun, shuning uchun ichki ekranlar ko'rsatilmaydi.",
            "Платформа работает; доступ только для сотрудников, поэтому внутренние экраны не показываются.",
            "The platform is running; access is for staff only, so internal screens are not shown.",
        ),
        highlights=(
            ["Chat va kod rejimi, Telegram bot + veb-UI", "Izolyatsiyalangan Docker konteyner, boshqa konteynerlarga tegmaydi", "Sirlar obrazdan tashqarida, HTTPS orqali kirish", "Arxitektura qarorlari ADR sifatida hujjatlashtirilgan"],
            ["Режимы чата и кода, Telegram-бот + веб-UI", "Изолированный Docker-контейнер, соседние контейнеры не затрагиваются", "Секреты вне образа, доступ по HTTPS", "Архитектурные решения оформлены как ADR"],
            ["Chat and code modes, Telegram bot + web UI", "Isolated Docker container that leaves neighbouring containers untouched", "Secrets kept outside the image, access over HTTPS", "Architecture decisions documented as ADRs"],
        ),
    ),
    dict(
        slug='akromind', title='Akromind', kind=LUMARC, order=50, featured=True,
        categories='web', year_start=2026, ongoing=True, status='in_development',
        live_url='https://akromind.uz',
        stack='Next.js, React, TypeScript, Tailwind CSS, Docker',
        role=("Fullstack dasturchi", "Fullstack-разработчик", "Fullstack Developer"),
        short=(
            "IT va AI yechimlar kompaniyasining sayti: xizmatlar, portfolio, maqolalar va aloqa.",
            "Сайт компании IT- и AI-решений: услуги, портфолио, статьи и контакты.",
            "Website of an IT and AI solutions company: services, portfolio, articles and contact.",
        ),
        problem=(
            "Kompaniyaga xizmatlari va ishlarini bir joyda ko'rsatadigan, kengaytirish oson sayt kerak edi.",
            "Компании нужен сайт, который показывает услуги и работы в одном месте и легко расширяется.",
            "The company needed a site that presents its services and work in one place and is easy to extend.",
        ),
        solution=(
            "Next.js + TypeScript'da sayt: xizmatlar (veb va mobil ilovalar, AI/LLM integratsiyasi, Telegram botlar, IT konsalting), portfolio va maqolalar. Yangi loyiha bitta ma'lumot faylidagi obyekt qo'shish bilan chiqadi.",
            "Сайт на Next.js + TypeScript: услуги (веб и мобильные приложения, интеграция AI/LLM, Telegram-боты, IT-консалтинг), портфолио и статьи. Новый проект добавляется одним объектом в файле данных.",
            "A Next.js + TypeScript site: services (web and mobile apps, AI/LLM integration, Telegram bots, IT consulting), portfolio and articles. A new project is added with a single object in a data file.",
        ),
        result=(
            "Sayt ishlab chiqilmoqda; akromind.uz da ochiq.",
            "Сайт в разработке; доступен на akromind.uz.",
            "The site is in development and reachable at akromind.uz.",
        ),
        highlights=(
            ["Next.js + TypeScript + Tailwind CSS", "Portfolio va xizmatlar ma'lumot fayllaridan chiqariladi", "Loyiha sahifalari /loyihalar/<slug>", "Docker orqali ishga tushirish"],
            ["Next.js + TypeScript + Tailwind CSS", "Портфолио и услуги берутся из файлов данных", "Страницы проектов /loyihalar/<slug>", "Запуск через Docker"],
            ["Next.js + TypeScript + Tailwind CSS", "Portfolio and services are rendered from data files", "Project pages at /loyihalar/<slug>", "Runs through Docker"],
        ),
    ),
    # ------------------------------------------------------------ BOTLAR (shaxsiy)
    dict(
        slug='moneyflow', title='MoneyFlow', kind=PERSONAL, order=60, featured=True,
        categories='bot,backend', year_start=2026, status='live',
        telegram_url='https://t.me/moneyflow_uz_bot',
        stack='Python, python-telegram-bot, PostgreSQL, SQLAlchemy, Alembic, pandas, openpyxl, ReportLab, Docker',
        role=("Dasturchi (yakka)", "Разработчик (соло)", "Solo developer"),
        short=(
            "Shaxsiy va biznes daromad/xarajatlarini yuritish uchun Telegram bot: 6 tilda, Excel va PDF hisobot bilan.",
            "Telegram-бот для учёта личных и бизнес-доходов и расходов: 6 языков, отчёты в Excel и PDF.",
            "A Telegram bot for tracking personal and business income and expenses: 6 languages, Excel and PDF reports.",
        ),
        problem=(
            "Kundalik xarajatlarni yuritish ko'pincha murakkab ilovalar tufayli yarim yo'lda to'xtaydi.",
            "Ведение ежедневных расходов часто бросают из-за сложных приложений.",
            "Tracking daily spending is often abandoned because of overly complex apps.",
        ),
        solution=(
            "Yozuvlar oddiy matn bilan kiritiladi (masalan, «yolkira 10000»); bot kunlik, haftalik, oylik va yillik hisobotni oldingi davr bilan solishtiradi, yozuvlarni sahifalab ko'rsatadi va o'chirishga imkon beradi.",
            "Записи вводятся обычным текстом (например, «yolkira 10000»); бот строит отчёты за день, неделю, месяц и год со сравнением с прошлым периодом, показывает записи постранично и позволяет удалять.",
            "Entries are typed as plain text (for example “yolkira 10000”); the bot builds daily, weekly, monthly and yearly reports compared with the previous period, lists records with pagination and allows deletion.",
        ),
        result=(
            "Bot jonli; interfeys uz, ru, en, fr, tr va ar tillarida (arab tili — o'ngdan chapga), Excel va PDF eksport mavjud.",
            "Бот работает; интерфейс на uz, ru, en, fr, tr и ar (арабский — справа налево), доступен экспорт в Excel и PDF.",
            "The bot is live; the interface supports uz, ru, en, fr, tr and ar (Arabic is right-to-left), with Excel and PDF export.",
        ),
        highlights=(
            ["6 interfeys tili", "Erkin matn orqali yozuv kiritish", "Davrlar bo'yicha hisobot va oldingi davr bilan taqqoslash", "Excel va PDF eksport", "Alembic migratsiyalar, pytest testlari, Docker"],
            ["6 языков интерфейса", "Ввод записей свободным текстом", "Отчёты по периодам со сравнением с предыдущим", "Экспорт в Excel и PDF", "Миграции Alembic, тесты pytest, Docker"],
            ["6 interface languages", "Free-text entry input", "Period reports with comparison to the previous period", "Excel and PDF export", "Alembic migrations, pytest tests, Docker"],
        ),
    ),
    dict(
        slug='saveclip', title='SaveClip', kind=PERSONAL, order=70, featured=True,
        categories='bot,automation', year_start=2026, status='live',
        telegram_url='https://t.me/saveclipuz_bot',
        stack='Python, python-telegram-bot, yt-dlp, ffmpeg, SQLite, APScheduler, Docker',
        role=("Dasturchi (yakka)", "Разработчик (соло)", "Solo developer"),
        short=(
            "YouTube, Instagram, TikTok, X, Facebook va Pinterest havolalaridan video yuklab beruvchi Telegram bot.",
            "Telegram-бот, скачивающий видео по ссылкам YouTube, Instagram, TikTok, X, Facebook и Pinterest.",
            "A Telegram bot that downloads videos from YouTube, Instagram, TikTok, X, Facebook and Pinterest links.",
        ),
        problem=(
            "Video yuklash uchun saytlar reklamaga to'la, Telegram chegarasi (50 MB) esa katta fayllarga to'sqinlik qiladi.",
            "Сайты для скачивания видео забиты рекламой, а лимит Telegram (50 МБ) мешает большим файлам.",
            "Video download sites are full of ads, and Telegram's 50 MB limit gets in the way of large files.",
        ),
        solution=(
            "Havola yuboriladi — bot yuklab, sifat tanlovini (720p / 480p / 360p / MP3) beradi. 50 MB dan oshsa sifatni tushiradi, ffmpeg bilan siqadi yoki to'g'ridan-to'g'ri havola beradi; bir xil havola file_id keshi bilan darhol qayta yuboriladi.",
            "Отправляете ссылку — бот скачивает и предлагает выбор качества (720p / 480p / 360p / MP3). Если больше 50 МБ — снижает качество, сжимает через ffmpeg или даёт прямую ссылку; повторная ссылка отдаётся мгновенно из кэша file_id.",
            "Send a link and the bot downloads it and offers a quality choice (720p / 480p / 360p / MP3). Above 50 MB it lowers the quality, compresses with ffmpeg or returns a direct link; the same link is re-sent instantly from a file_id cache.",
        ),
        result=(
            "Bot jonli ishlaydi: tezlik cheklovi, majburiy kanal obunasi, admin panel va ommaviy xabar, SSRF himoyasi bilan.",
            "Бот работает: ограничение частоты, обязательная подписка на канал, админ-панель и рассылка, защита от SSRF.",
            "The bot is live with rate limiting, mandatory channel subscription, an admin panel with broadcast, and SSRF protection.",
        ),
        highlights=(
            ["6 ta platforma: YouTube, Instagram, TikTok (suvsiz belgi), X, Facebook, Pinterest", "50 MB chegarasi uchun avtomatik yechimlar", "file_id keshi, tezlik cheklovi, bir vaqtda bitta yuklash", "Domen ruxsat ro'yxati (SSRF himoyasi), vaqtinchalik fayllarni tozalash", "Admin panel, ban, ommaviy xabar"],
            ["6 платформ: YouTube, Instagram, TikTok (без водяного знака), X, Facebook, Pinterest", "Автоматические решения для лимита 50 МБ", "Кэш file_id, ограничение частоты, одна активная загрузка на пользователя", "Белый список доменов (защита от SSRF), очистка временных файлов", "Админ-панель, баны, рассылка"],
            ["6 platforms: YouTube, Instagram, TikTok (no watermark), X, Facebook, Pinterest", "Automatic handling of the 50 MB limit", "file_id cache, rate limit, one active download per user", "Domain allowlist (SSRF protection), temp-file cleanup", "Admin panel, bans, broadcast"],
        ),
    ),
    # ------------------------------------------------------------ MIJOZ / BOSHQALAR
    dict(
        slug='uzstroymarket', title='UzStroyMarket', kind=CLIENT, order=80, featured=True,
        categories='web,bot,backend', year_start=2026, status='live',
        stack='Next.js, TypeScript, Fastify, Prisma, PostgreSQL, grammY (Telegram), npm workspaces',
        role=("Fullstack dasturchi", "Fullstack-разработчик", "Fullstack Developer"),
        short=(
            "Qurilish materiallari marketplace: xaridor sayti, sotuvchi va bosh admin panellari hamda Telegram bot.",
            "Маркетплейс строительных материалов: сайт покупателя, панели продавца и главного администратора и Telegram-бот.",
            "A construction-materials marketplace: customer site, seller and head-admin panels, and a Telegram bot.",
        ),
        problem=(
            "Qurilish materiallarini topish, do'konlar takliflarini solishtirish va buyurtma berish tarqoq kanallarda yuradi.",
            "Поиск стройматериалов, сравнение предложений магазинов и заказ разбросаны по разным каналам.",
            "Finding construction materials, comparing store offers and ordering are scattered across channels.",
        ),
        solution=(
            "Xaridor, sotuvchi va administrator bitta tizimda: katalog, savat va buyurtmalar tarixi; bir nechta do'kondan tuzilgan savat har bir sotuvchi uchun alohida buyurtmaga ajratiladi. Umumiy PostgreSQL API sayt, panellar va botga xizmat qiladi.",
            "Покупатель, продавец и администратор в одной системе: каталог, корзина и история заказов; корзина из нескольких магазинов делится на отдельные заказы для каждого продавца. Общий API на PostgreSQL обслуживает сайт, панели и бота.",
            "Buyer, seller and administrator live in one system: catalog, cart and order history; a cart built from several stores is split into a separate order per seller. A shared PostgreSQL-backed API serves the site, the panels and the bot.",
        ),
        result=(
            "Platforma AWS serverda ishlaydi; uz/ru/en tillari va kunduz/tun rejimi mavjud. Alohida domen hali ulanmagan.",
            "Платформа работает на сервере AWS; доступны uz/ru/en и дневной/ночной режим. Отдельный домен пока не подключён.",
            "The platform runs on an AWS server with uz/ru/en and day/night themes. A dedicated domain is not connected yet.",
        ),
        highlights=(
            ["Uch rol: xaridor, sotuvchi, bosh admin", "Ko'p do'konli savat → sotuvchi bo'yicha alohida buyurtmalar", "Telegram bot orqali ro'yxatdan o'tishni tasdiqlash", "Uch til va kunduz/tun rejimi", "Monorepo: api, web, bot, umumiy db va i18n paketlari"],
            ["Три роли: покупатель, продавец, главный админ", "Корзина из нескольких магазинов → отдельные заказы по продавцам", "Подтверждение регистрации через Telegram-бота", "Три языка и дневной/ночной режим", "Монорепозиторий: api, web, bot, общие пакеты db и i18n"],
            ["Three roles: buyer, seller, head admin", "Multi-store cart → separate orders per seller", "Registration confirmation through a Telegram bot", "Three languages and a day/night theme", "Monorepo: api, web, bot, shared db and i18n packages"],
        ),
    ),
    dict(
        slug='tashkent-3d-residence', title='Tashkent City Residence', kind=PERSONAL, order=90, featured=True,
        categories='3d,web', year_start=2026, status='concept',
        stack='Next.js 16, React 19, React Three Fiber, three.js, zustand, Tailwind CSS 4, Framer Motion, GSAP',
        role=("Fullstack dasturchi", "Fullstack-разработчик", "Fullstack Developer"),
        short=(
            "Turar-joy majmuasi uchun interaktiv 3D konfigurator: bino, qavat va xonadon tanlash, 3D planirovka, narx va rassrochka.",
            "Интерактивный 3D-конфигуратор жилого комплекса: выбор здания, этажа и квартиры, 3D-планировка, цена и рассрочка.",
            "An interactive 3D configurator for a residential complex: building, floor and apartment selection, 3D floor plan, price and installments.",
        ),
        problem=(
            "Xaridorga xonadonni tanlashda tekis rasm va PDF yetarli emas — joylashuv va hajmni his qilish kerak.",
            "Покупателю при выборе квартиры недостаточно плоских картинок и PDF — нужно почувствовать расположение и объём.",
            "Flat images and PDFs are not enough when choosing an apartment — buyers want to feel the layout and volume.",
        ),
        solution=(
            "Mijoz binoni tashqaridan ko'radi, qavatni kesib ko'radi, xonadonning 3D planirovkasiga va xona ichiga (birinchi shaxs) o'tadi, shaxmatkada holatlarni ko'radi, rassrochkani hisoblaydi va ariza qoldiradi.",
            "Клиент осматривает здание снаружи, разрезает этаж, переходит к 3D-планировке квартиры и внутрь комнат (от первого лица), смотрит статусы в шахматке, считает рассрочку и оставляет заявку.",
            "The visitor views the building from outside, slices a floor, moves into the apartment's 3D plan and inside the rooms (first person), checks availability on the grid, calculates installments and submits a request.",
        ),
        result=(
            "Konfigurator ishlaydi (uz/ru/en, USD/UZS); ariza Telegram'ga yuboriladi. Konsept/demo bosqichida.",
            "Конфигуратор работает (uz/ru/en, USD/UZS); заявки уходят в Telegram. Стадия концепта/демо.",
            "The configurator works (uz/ru/en, USD/UZS) and requests go to Telegram. Concept/demo stage.",
        ),
        highlights=(
            ["16 qavatli bino, qavat kesimi va yoritish", "3D planirovka va xona ichi (birinchi shaxs)", "Shaxmatka: sotuvda / band / sotilgan", "Rassrochka kalkulyatori, USD / UZS", "Ariza Telegram'ga, mobil ko'rinishga moslashgan"],
            ["16-этажное здание, срез этажа и подсветка", "3D-планировка и обзор комнат от первого лица", "Шахматка: в продаже / бронь / продано", "Калькулятор рассрочки, USD / UZS", "Заявка в Telegram, адаптация под мобильные"],
            ["16-floor building with floor slicing and highlighting", "3D floor plan and first-person room view", "Availability grid: for sale / reserved / sold", "Installment calculator, USD / UZS", "Requests sent to Telegram, mobile-ready"],
        ),
    ),
    dict(
        slug='bahober', title='Bahober', kind=CLIENT, order=100, featured=False,
        categories='web,backend', year_start=2026, status='live',
        live_url='https://bahober.uz',
        stack='Go, React, Vite, MUI, Redux, Expo (React Native), PostgreSQL, nginx, Docker',
        role=("Fullstack dasturchi (audit va rivojlantirish)", "Fullstack-разработчик (аудит и развитие)", "Fullstack developer (audit and development)"),
        short=(
            "Kafe va restoranlar kabi joylar haqida sharh va reyting platformasi: veb-sayt, admin panel, Go API va mobil ilova.",
            "Платформа отзывов и рейтингов заведений (кафе, рестораны и др.): сайт, админ-панель, Go API и мобильное приложение.",
            "A review and rating platform for venues such as cafés and restaurants: website, admin panel, Go API and a mobile app.",
        ),
        problem=(
            "Mijoz loyihasi kod bazasi bilan davom ettirishni, xatolarni tuzatishni va yangi imkoniyatlar qo'shishni talab qildi.",
            "Клиентский проект требовал продолжить работу с кодовой базой, исправить ошибки и добавить новые возможности.",
            "The client project required continuing work on an existing codebase, fixing defects and adding features.",
        ),
        solution=(
            "Go API (Fiber + gRPC + PostgreSQL), React + Vite + MUI sayt va admin panel hamda Expo mobil ilova bo'yicha ishlar; arxitektura qarorlari ADR sifatida yuritiladi.",
            "Работа над Go API (Fiber + gRPC + PostgreSQL), сайтом и админ-панелью на React + Vite + MUI и мобильным приложением на Expo; архитектурные решения ведутся как ADR.",
            "Work across the Go API (Fiber + gRPC + PostgreSQL), the React + Vite + MUI site and admin panel, and the Expo mobile app; architecture decisions are tracked as ADRs.",
        ),
        result=(
            "Platforma bahober.uz da ishlaydi (uz, ru). Mijoz loyihasi: mualliflik va mulk egasi — mijoz.",
            "Платформа работает на bahober.uz (uz, ru). Клиентский проект: права и владелец — заказчик.",
            "The platform runs at bahober.uz (uz, ru). A client project: ownership belongs to the client.",
        ),
        highlights=(
            ["Go 1.23, Fiber, gRPC, PostgreSQL migratsiyalari", "React + Vite + MUI + Redux sayt, uz/ru (i18next)", "Admin panel va Expo (React Native) mobil ilova", "vitest va Go testlari, ADR hujjatlari"],
            ["Go 1.23, Fiber, gRPC, миграции PostgreSQL", "Сайт на React + Vite + MUI + Redux, uz/ru (i18next)", "Админ-панель и мобильное приложение Expo (React Native)", "Тесты vitest и Go, документы ADR"],
            ["Go 1.23, Fiber, gRPC, PostgreSQL migrations", "React + Vite + MUI + Redux site, uz/ru (i18next)", "Admin panel and an Expo (React Native) mobile app", "vitest and Go tests, ADR documents"],
        ),
    ),
    dict(
        slug='yuridik-yordam', title='YuridikYordam', kind=PERSONAL, order=110, featured=False,
        categories='web,backend', year_start=2026, status='concept',
        stack='Python, Django, SQLite, Django templates',
        role=("Dasturchi (yakka)", "Разработчик (соло)", "Solo developer"),
        short=(
            "Mijozlarni kerakli yuridik xizmat bo'yicha mutaxassis bilan bog'laydigan Django platforma.",
            "Django-платформа, связывающая клиентов со специалистами по нужной юридической услуге.",
            "A Django platform connecting clients with specialists for the legal service they need.",
        ),
        problem=(
            "Mijoz qaysi yuristga murojaat qilishni bilmaydi, yuristlar esa mijoz topishda qiynaladi.",
            "Клиент не знает, к какому юристу обратиться, а юристам сложно находить клиентов.",
            "Clients do not know which lawyer to approach, and lawyers struggle to find clients.",
        ),
        solution=(
            "Xizmat turlari va hududlar bo'yicha mutaxassislar katalogi (filtr bilan), «Yurist sizni topadi» ariza formasi va CRM-ga o'xshash ariza holatlari, blog maqolalari.",
            "Каталог специалистов по видам услуг и регионам (с фильтрами), форма «Юрист найдёт вас», CRM-подобные статусы заявок и блог.",
            "A specialist catalog by service type and region (with filters), a “the lawyer finds you” request form, CRM-like request statuses and a blog.",
        ),
        result=(
            "Ishlaydigan prototip (seed_demo bilan namunaviy ma'lumotlar); konsept bosqichida.",
            "Рабочий прототип (демо-данные через seed_demo); стадия концепта.",
            "A working prototype (sample data via seed_demo); concept stage.",
        ),
        highlights=(
            ["Mijoz va mutaxassis rollari", "Filtrli mutaxassis katalogi", "Ariza formasi va holatlar", "Blog va seed_demo buyrug'i"],
            ["Роли клиента и специалиста", "Каталог специалистов с фильтрами", "Форма заявки и статусы", "Блог и команда seed_demo"],
            ["Client and specialist roles", "Specialist catalog with filters", "Request form and statuses", "Blog and a seed_demo command"],
        ),
    ),
    dict(
        slug='shajara', title='Shajara', kind=PERSONAL, order=120, featured=False,
        categories='web', year_start=2026, status='live',
        stack='JavaScript (vanilla), HTML, CSS, Python (bundle)',
        role=("Dasturchi (yakka)", "Разработчик (соло)", "Solo developer"),
        short=(
            "Internetsiz ishlaydigan oilaviy daraxt ilovasi: tahrirlash, qidiruv, rasm muharriri, PDF va Excel eksport.",
            "Офлайн-приложение семейного древа: редактирование, поиск, редактор фото, экспорт в PDF и Excel.",
            "An offline family-tree app: editing, search, a photo editor, PDF and Excel export.",
        ),
        problem=(
            "Oila tarixini saqlash uchun internet va akkaunt talab qiladigan xizmatlar ishonchsiz va maxfiylikka xavfli.",
            "Сервисы для хранения семейной истории требуют интернет и аккаунт — это ненадёжно и небезопасно для приватности.",
            "Services that store family history require internet and an account, which is unreliable and risky for privacy.",
        ),
        solution=(
            "Hech qanday kutubxonasiz sof HTML/CSS/JS: ma'lumotlar brauzerda saqlanadi, JSON zaxira va tiklash bor, butun ilova bitta Shajara.html fayliga yig'iladi va shunchaki ochiladi.",
            "Чистые HTML/CSS/JS без библиотек: данные хранятся в браузере, есть JSON-резерв и восстановление, всё приложение собирается в один файл Shajara.html и открывается двойным щелчком.",
            "Plain HTML/CSS/JS with no libraries: data lives in the browser, JSON backup and restore are included, and the whole app bundles into one Shajara.html file that simply opens.",
        ),
        result=(
            "Ilova ishlaydi; hozirgi interfeys o'zbek tilida (uz/ru/en lug'atlari tayyor).",
            "Приложение работает; текущий интерфейс на узбекском (словари uz/ru/en готовы).",
            "The app works; the current interface is in Uzbek (uz/ru/en dictionaries are in place).",
        ),
        highlights=(
            ["Ish vaqtida bog'liqliksiz, offline", "JSON zaxira / tiklash", "PDF, Excel va bosma eksport", "Foto muharrir, qidiruv", "tools/bundle.py bilan bitta faylga yig'ish"],
            ["Без зависимостей в рантайме, офлайн", "JSON-резерв / восстановление", "Экспорт в PDF, Excel и печать", "Редактор фото, поиск", "Сборка в один файл через tools/bundle.py"],
            ["No runtime dependencies, offline", "JSON backup / restore", "PDF, Excel and print export", "Photo editor, search", "Bundled into a single file with tools/bundle.py"],
        ),
    ),
    dict(
        slug='language-bot', title="Til o'rganish hamrohi", kind=PERSONAL, order=130, featured=False,
        categories='bot,ai', year_start=2026, status='archived',
        stack='Python, aiogram 3, SQLAlchemy, SQLite, Groq (LLM, Whisper, TTS)',
        role=("Dasturchi (yakka)", "Разработчик (соло)", "Solo developer"),
        short=(
            "AI bilan ingliz va rus tillarini mashq qildiradigan Telegram bot: suhbat, so'zlar, viktorina va progress.",
            "Telegram-бот для практики английского и русского с ИИ: диалог, слова, викторины и прогресс.",
            "A Telegram bot for practising English and Russian with AI: conversation, vocabulary, quizzes and progress.",
        ),
        problem=(
            "Til o'rganuvchi suhbat amaliyotiga va xatolari bo'yicha tezkor tuzatishga muhtoj.",
            "Изучающему язык нужна разговорная практика и быстрая обратная связь по ошибкам.",
            "Language learners need conversation practice and quick feedback on mistakes.",
        ),
        solution=(
            "aiogram FSM bilan til va daraja tanlanadi; bot suhbatda xatolarni yumshoq tuzatadi, so'z va misollar beradi, saqlangan so'zlardan 4 variantli viktorina o'tkazadi va streak'ni kuzatadi. Ovozli xabarlar (Whisper) va ovoz chiqarish (TTS), DOCX/PPTX/PDF yaratish ham bor.",
            "Через aiogram FSM выбираются язык и уровень; бот мягко исправляет ошибки в диалоге, даёт слова и примеры, проводит викторины с 4 вариантами по сохранённым словам и ведёт streak. Есть голосовые сообщения (Whisper), озвучка (TTS), создание DOCX/PPTX/PDF.",
            "Language and level are chosen via an aiogram FSM; the bot gently corrects mistakes in conversation, supplies words and examples, runs 4-option quizzes from saved words and tracks the streak. Voice messages (Whisper), speech output (TTS) and DOCX/PPTX/PDF generation are included.",
        ),
        result=(
            "Ishlaydigan bot (aiogram 3 + Groq); arxiv holatida.",
            "Рабочий бот (aiogram 3 + Groq); в архиве.",
            "A working bot (aiogram 3 + Groq); archived.",
        ),
        highlights=(
            ["Onboarding: til va daraja (FSM)", "Suhbat, so'zlar, viktorina, progress", "Ovozli kiritish (Whisper) va TTS", "DOCX / PPTX / PDF yaratish"],
            ["Онбординг: язык и уровень (FSM)", "Диалог, слова, викторины, прогресс", "Голосовой ввод (Whisper) и TTS", "Создание DOCX / PPTX / PDF"],
            ["Onboarding: language and level (FSM)", "Conversation, vocabulary, quizzes, progress", "Voice input (Whisper) and TTS", "DOCX / PPTX / PDF generation"],
        ),
    ),
    dict(
        slug='buy-a-ticket-bot', title='Buy a Ticket Bot', kind=PERSONAL, order=140, featured=False,
        categories='bot,backend', year_start=2026, status='archived',
        stack='Python, Django, python-telegram-bot, Django Admin, QR',
        role=("Dasturchi (yakka)", "Разработчик (соло)", "Solo developer"),
        short=(
            "Tadbir chiptalarini Telegram orqali sotish: speaker/mavzu tanlash, joy band qilish, to'lov tasdig'i va QR-kodli chipta.",
            "Продажа билетов на мероприятия через Telegram: выбор спикера/темы, бронь места, подтверждение оплаты и билет с QR-кодом.",
            "Event ticket sales through Telegram: pick a speaker/topic, reserve a seat, payment confirmation and a QR-coded ticket.",
        ),
        problem=(
            "Tadbirga joylarni qo'lda ro'yxatga olish va to'lovlarni tekshirish chalkash va xatoga moyil.",
            "Ручная запись на мероприятие и проверка оплат запутана и подвержена ошибкам.",
            "Registering seats by hand and checking payments is confusing and error-prone.",
        ),
        solution=(
            "Foydalanuvchi bot orqali mavzu va joyni tanlaydi, kartaga to'lab chek skrinshotini yuboradi; admin to'lovni tasdiqlaydi yoki sabab bilan rad etadi, so'ng QR-kodli chipta beriladi. Ma'lumotlar Django Admin'da boshqariladi.",
            "Пользователь выбирает тему и место в боте, оплачивает на карту и присылает скриншот чека; админ подтверждает оплату или отклоняет с причиной, после чего выдаётся билет с QR-кодом. Данные управляются в Django Admin.",
            "The user picks a topic and a seat in the bot, pays by card transfer and sends a receipt screenshot; an admin approves the payment or rejects it with a reason, and a QR-coded ticket is issued. Data is managed in Django Admin.",
        ),
        result=(
            "Ishlaydigan tizim (Django + Telegram bot); arxiv holatida.",
            "Рабочая система (Django + Telegram-бот); в архиве.",
            "A working system (Django + Telegram bot); archived.",
        ),
        highlights=(
            ["Speaker, mavzu, sessiya va joy modellari", "To'lov tasdig'i admin orqali (sabab bilan rad etish)", "QR-kodli chipta", "Bot matnlari bir necha tilda"],
            ["Модели спикера, темы, сессии и места", "Подтверждение оплаты админом (отказ с причиной)", "Билет с QR-кодом", "Тексты бота на нескольких языках"],
            ["Speaker, topic, session and seat models", "Payment approval by an admin (rejection with a reason)", "QR-coded ticket", "Bot texts in several languages"],
        ),
    ),
    dict(
        slug='gym-management', title='Gym Management', kind=PERSONAL, order=150, featured=False,
        categories='bot,backend', year_start=2026, status='archived',
        stack='Python, Django, Django REST Framework, aiogram, PostgreSQL, Docker',
        role=("Dasturchi (yakka)", "Разработчик (соло)", "Solo developer"),
        short=(
            "Sportzal boshqaruv tizimi: Django REST API, Telegram bot, trenerlar va zallar jadvali, to'lovlar.",
            "Система управления спортзалом: Django REST API, Telegram-бот, расписание тренеров и залов, платежи.",
            "A gym management system: Django REST API, a Telegram bot, trainer and hall schedules, and payments.",
        ),
        problem=(
            "Zalda jadval, trenerlar va obuna to'lovlari qo'lda yuritiladi.",
            "Расписание, тренеры и оплата абонементов ведутся вручную.",
            "Schedules, trainers and membership payments are handled by hand.",
        ),
        solution=(
            "Trener, zal va jadval modellari, to'lovlar moduli va ruxsatlar bilan REST API; a'zolar uchun aiogram boti. Loyiha Docker orqali ishga tushadi.",
            "REST API с моделями тренеров, залов и расписания, модулем платежей и правами доступа; бот на aiogram для участников. Проект запускается через Docker.",
            "A REST API with trainer, hall and schedule models, a payments module and permissions; an aiogram bot for members. The project runs through Docker.",
        ),
        result=(
            "Servis qatlami va API/bot testlari bilan ishlaydigan tizim; arxiv holatida.",
            "Рабочая система с сервисным слоем и тестами API/бота; в архиве.",
            "A working system with a service layer and API/bot tests; archived.",
        ),
        highlights=(
            ["DRF API: trenerlar, zallar, jadval, to'lovlar", "aiogram bot (FSM, middleware, klaviaturalar)", "Ruxsatlar va validatorlar", "Docker Compose, testlar"],
            ["DRF API: тренеры, залы, расписание, платежи", "Бот на aiogram (FSM, middleware, клавиатуры)", "Права доступа и валидаторы", "Docker Compose, тесты"],
            ["DRF API: trainers, halls, schedules, payments", "aiogram bot (FSM, middleware, keyboards)", "Permissions and validators", "Docker Compose, tests"],
        ),
    ),
    dict(
        slug='hunarmandlar-tarmogi', title="Hunarmandlar tarmog'i", kind=PERSONAL, order=160, featured=False,
        categories='web,backend', year_start=2026, status='archived',
        stack='Python, Flask, SQLite',
        role=("Dasturchi (yakka)", "Разработчик (соло)", "Solo developer"),
        short=(
            "Flask va SQLite'da qurilgan hamjamiyat platformasi: sohalar bo'yicha mutaxassis profillari va xizmat narxlari.",
            "Платформа-сообщество на Flask и SQLite: профили специалистов по сферам и цены на услуги.",
            "A community platform built with Flask and SQLite: specialist profiles by field and service prices.",
        ),
        problem=(
            "Turli sohadagi hunarmandlar o'z xizmatlarini bir joyda ko'rsatadigan joy topa olmaydi.",
            "Мастера разных сфер не находят единого места, чтобы показать свои услуги.",
            "Craftspeople from different fields lack a single place to present their services.",
        ),
        solution=(
            "Bitta umumiy ro'yxatdan o'tish, kabinet, sohalar bo'limi: foydalanuvchi bir yoki bir nechta sohaga qo'shilib, har biri uchun alohida profil (sarlavha, bio, ko'nikma, hudud, xizmat va narx) to'ldiradi.",
            "Единая регистрация, кабинет, раздел сфер: пользователь вступает в одну или несколько сфер и заполняет отдельный профиль для каждой (заголовок, био, навыки, регион, услуги и цены).",
            "A single registration, a dashboard and a fields section: a user joins one or more fields and fills a separate profile for each (headline, bio, skills, region, services and prices).",
        ),
        result=(
            "Ma'lumotlar serverda SQLite faylida saqlanadigan ishlaydigan versiya; arxiv holatida.",
            "Рабочая версия с хранением данных на сервере в файле SQLite; в архиве.",
            "A working version that stores data on the server in a SQLite file; archived.",
        ),
        highlights=(
            ["Bir akkaunt — bir nechta soha profili", "Xizmatlar va narxlar", "Profil rasmi yuklash", "Faqat Flask bilan, qo'shimcha sozlashsiz"],
            ["Один аккаунт — несколько профилей по сферам", "Услуги и цены", "Загрузка фото профиля", "Только Flask, без дополнительной настройки"],
            ["One account — several field profiles", "Services and prices", "Profile picture upload", "Flask only, no extra setup"],
        ),
    ),
    dict(
        slug='umumiy-sayt', title='Umumiy sayt (hub)', kind=PERSONAL, order=170, featured=False,
        categories='web,backend', year_start=2026, status='concept',
        stack='Python, Flask, Nginx, systemd',
        role=("Dasturchi (yakka)", "Разработчик (соло)", "Solo developer"),
        short=(
            "Bitta domen ostida bir nechta mustaqil loyihani yig'adigan hub sayt: Nginx yo'l bo'yicha trafikni yo'naltiradi.",
            "Хаб-сайт, объединяющий несколько независимых проектов под одним доменом: Nginx направляет трафик по путям.",
            "A hub site that brings several independent projects under one domain: Nginx routes traffic by path.",
        ),
        problem=(
            "Har bir kichik loyiha uchun alohida domen va server ajratish ortiqcha xarajat.",
            "Отдельный домен и сервер для каждого небольшого проекта — лишние расходы.",
            "A separate domain and server for every small project is wasteful.",
        ),
        solution=(
            "Hub menyu sahifasi va mustaqil Python ilovalar (har biri o'z virtual muhiti va portida), Nginx konfiguratsiyasi va systemd xizmat fayllari bilan.",
            "Страница-меню хаба и независимые Python-приложения (каждое со своим venv и портом), конфигурация Nginx и юниты systemd.",
            "A hub menu page and independent Python apps (each with its own virtualenv and port), plus an Nginx config and systemd unit files.",
        ),
        result=(
            "Shablon va deploy fayllari tayyor; yangi loyiha shablondan nusxa olish bilan qo'shiladi.",
            "Шаблон и deploy-файлы готовы; новый проект добавляется копированием шаблона.",
            "The template and deploy files are ready; a new project is added by copying the template.",
        ),
        highlights=(
            ["Hub + mustaqil ilovalar", "Nginx yo'l bo'yicha proxy", "systemd xizmat fayllari"],
            ["Хаб + независимые приложения", "Прокси Nginx по путям", "Юниты systemd"],
            ["Hub + independent apps", "Nginx path-based proxy", "systemd unit files"],
        ),
    ),
    dict(
        slug='online-book-store', title='Online Book Store', kind=LEARNING, order=300, featured=False,
        categories='backend', year_start=2026, status='archived',
        stack='Python, Django, DRF, PostgreSQL',
        role=("O'quv loyiha", "Учебный проект", "Learning project"),
        short=(
            "Onlayn kitob do'koni uchun backend API: kitoblar katalogi bo'yicha CRUD, PostgreSQL sxemasi.",
            "Backend API онлайн-магазина книг: CRUD для каталога книг, схема PostgreSQL.",
            "A backend API for an online book store: CRUD for the book catalog, a PostgreSQL schema.",
        ),
        highlights=(["DRF orqali CRUD", "PostgreSQL sxemasi"], ["CRUD через DRF", "Схема PostgreSQL"], ["CRUD with DRF", "PostgreSQL schema"]),
    ),
    dict(
        slug='u13-task-manager', title='Task Manager API', kind=LEARNING, order=310, featured=False,
        categories='backend', year_start=2026, status='archived',
        github_url='https://github.com/dostonbeksuyunov/U13_task_manager',
        stack='Python, Django, DRF',
        role=("O'quv loyiha", "Учебный проект", "Learning project"),
        short=(
            "Django REST Framework asosidagi vazifalar menejeri API (kurs mashqi).",
            "API менеджера задач на Django REST Framework (учебное задание).",
            "A task manager API built with Django REST Framework (course exercise).",
        ),
        highlights=(["DRF API", "Ochiq kod GitHub'da"], ["DRF API", "Открытый код на GitHub"], ["DRF API", "Open source on GitHub"]),
    ),
    dict(
        slug='normativ-drf', title='Normativ API', kind=LEARNING, order=320, featured=False,
        categories='backend', year_start=2026, status='archived',
        github_url='https://github.com/dostonbeksuyunov/DRF-normativ',
        stack='Python, Django, DRF',
        role=("O'quv loyiha", "Учебный проект", "Learning project"),
        short=(
            "Django REST Framework'da serializer, view va testlar bilan yozilgan normativ API (kurs mashqi).",
            "API на Django REST Framework с сериализаторами, представлениями и тестами (учебное задание).",
            "An API on Django REST Framework with serializers, views and tests (course exercise).",
        ),
        highlights=(["Serializer va view'lar", "Testlar", "Ochiq kod GitHub'da"], ["Сериализаторы и представления", "Тесты", "Открытый код на GitHub"], ["Serializers and views", "Tests", "Open source on GitHub"]),
    ),
    dict(
        slug='stadium-booking', title='Stadium Booking', kind=LEARNING, order=330, featured=False,
        categories='web,backend', year_start=2026, status='archived',
        stack='Python, Django',
        role=("O'quv loyiha", "Учебный проект", "Learning project"),
        short=(
            "Futbol maydonlarini band qilish: foydalanuvchi, maydon, maydon rasmlari va bron modellari.",
            "Бронирование футбольных полей: модели пользователя, поля, фото поля и брони.",
            "Football pitch booking: user, pitch, pitch image and booking models.",
        ),
        highlights=(["Django modellari va admin", "Bron mantiqi"], ["Модели Django и админка", "Логика бронирования"], ["Django models and admin", "Booking logic"]),
    ),
    dict(
        slug='taxi-trips', title='Taxi Trips', kind=LEARNING, order=340, featured=False,
        categories='backend', year_start=2026, status='archived',
        stack='Python, Django',
        role=("O'quv loyiha", "Учебный проект", "Learning project"),
        short=(
            "Taksi safarlari ma'lumotlarini Django'da saqlash va tahlil qilish bo'yicha mashq.",
            "Учебное упражнение по хранению и анализу данных о поездках такси в Django.",
            "An exercise in storing and analysing taxi-trip data in Django.",
        ),
        highlights=(["TaxiTrip modeli", "Ma'lumotlar bilan ishlash"], ["Модель TaxiTrip", "Работа с данными"], ["TaxiTrip model", "Working with data"]),
    ),
]
