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
        pk=1, slug='lumarc-sayt', title='Lumarc', kind=LUMARC, order=10, featured=True,
        categories='web,3d', year_start=2026, ongoing=True, status='live',
        live_url='https://lumarc.uz',
        stack='Next.js 16, React 19, TypeScript, NestJS 11, Prisma, PostgreSQL, Three.js, Photo Sphere Viewer',
        role=("Fullstack dasturchi", "Fullstack-разработчик", "Fullstack Developer"),
        short=(
            "Arxitektura va dizayn studiyasining rasmiy veb-sayti: loyihalar katalogi, 360° virtual turlar va boshqaruv paneli.",
            "Официальный сайт архитектурно-дизайнерской студии: каталог проектов, виртуальные туры 360° и панель управления.",
            "Official website of an architecture and design studio: project catalog, 360° virtual tours and an admin panel.",
        ),
        problem=(
            "Studiya o'z loyihalarini zamonaviy ko'rinishda taqdim etishi va kontentni mustaqil yangilab borishi zarur edi.",
            "Студии требовалось современно представлять свои проекты и самостоятельно обновлять контент.",
            "The studio needed to present its projects in a modern way and update content independently.",
        ),
        solution=(
            "Sayt Next.js ilovasi va NestJS API ko'rinishida ishlab chiqilgan. Katalog faol loyihalarni API'dan oladi; boshqaruv paneli orqali loyihalar, blog, jamoa va murojaatlar boshqariladi. Loyiha sahifalarida 360° tur va 3D sahnalar mavjud.",
            "Сайт реализован как приложение Next.js с API на NestJS. Каталог получает активные проекты из API, через панель управления редактируются проекты, блог, команда и обращения. На страницах проектов доступны туры 360° и 3D-сцены.",
            "The site is a Next.js application backed by a NestJS API. The catalog reads active projects from the API; the admin panel manages projects, the blog, the team and inquiries. Project pages include 360° tours and 3D scenes.",
        ),
        result=(
            "Sayt faol ishlamoqda; yangi dizayn ustida ish olib borilmoqda.",
            "Сайт работает; ведётся работа над новым дизайном.",
            "The site is live; a new design is in progress.",
        ),
        highlights=(
            ["Uch tilda: o'zbek, rus, ingliz", "360° virtual tur va Three.js sahnalari", "Boshqaruv paneli: loyihalar, blog, jamoa, murojaatlar", "SEO: sitemap, robots, JSON-LD"],
            ["Три языка: узбекский, русский, английский", "Виртуальные туры 360° и сцены Three.js", "Панель управления: проекты, блог, команда, обращения", "SEO: sitemap, robots, JSON-LD"],
            ["Three languages: Uzbek, Russian, English", "360° virtual tours and Three.js scenes", "Admin panel: projects, blog, team, inquiries", "SEO: sitemap, robots, JSON-LD"],
        ),
    ),
    dict(
        pk=2, slug='lumarcos', title='Lumarcos', kind=LUMARC, order=20, featured=True,
        categories='ai,web,backend', year_start=2026, ongoing=True, status='live',
        live_url='https://lumarcos.uz',
        stack='Next.js 16, React 19, NestJS 11, Prisma, PostgreSQL, BullMQ, Redis, MinIO, Docker Compose, Caddy, Gemini / Vertex AI, Kie.ai',
        role=("Fullstack dasturchi", "Fullstack-разработчик", "Fullstack Developer"),
        short=(
            "Arxitektorlar uchun AI platforma: renderlarni qayta ishlash, Image Studio hamda rasm va video generatsiyasi.",
            "AI-платформа для архитекторов: обработка рендеров, Image Studio, генерация изображений и видео.",
            "An AI platform for architects: render processing, Image Studio and image and video generation.",
        ),
        problem=(
            "Arxitektorlar render natijalarini qo'lda qayta ishlashga ko'p vaqt sarflaydi, generativ AI vositalari esa bir joyga jamlanmagan.",
            "Архитекторы тратят много времени на ручную обработку рендеров, а инструменты генеративного ИИ разрознены.",
            "Architects spend a lot of time retouching renders by hand, and generative AI tools are scattered.",
        ),
        solution=(
            "Platforma Post-Pro (render ishlovi), Image Studio va Generate bo'limlaridan iborat. AI so'rovlari navbat orqali (BullMQ, Redis) bajariladi, fayllar S3 bilan mos omborda saqlanadi, foydalanish kredit tizimi va onlayn to'lov orqali boshqariladi.",
            "Платформа включает разделы Post-Pro (обработка рендеров), Image Studio и Generate. AI-запросы выполняются через очередь (BullMQ, Redis), файлы хранятся в S3-совместимом хранилище, использование регулируется кредитами и онлайн-оплатой.",
            "The platform consists of Post-Pro (render processing), Image Studio and Generate. AI requests run through a queue (BullMQ, Redis), files are stored in S3-compatible storage, and usage is governed by credits and online payments.",
        ),
        result=(
            "Platforma lumarcos.uz manzilida ishlamoqda: OTP va email orqali kirish, kredit va to'lov (Payme, Click), boshqaruv paneli, CI jarayoni.",
            "Платформа работает на lumarcos.uz: вход по OTP и email, кредиты и оплата (Payme, Click), панель управления, CI.",
            "The platform runs at lumarcos.uz with OTP and email sign-in, credits and payments (Payme, Click), an admin panel and CI.",
        ),
        highlights=(
            ["Monorepo: NestJS API, Next.js veb-ilova, umumiy paket", "Gemini / Vertex AI va Kie.ai integratsiyasi", "BullMQ navbati, MinIO (S3) ombori", "Kredit va to'lov tizimi, boshqaruv paneli", "Docker Compose va Caddy (HTTPS), e2e testlar"],
            ["Монорепозиторий: NestJS API, веб-приложение Next.js, общий пакет", "Интеграция Gemini / Vertex AI и Kie.ai", "Очередь BullMQ, хранилище MinIO (S3)", "Кредиты и оплата, панель управления", "Docker Compose и Caddy (HTTPS), e2e-тесты"],
            ["Monorepo: NestJS API, Next.js web app and a shared package", "Gemini / Vertex AI and Kie.ai integration", "BullMQ queue and MinIO (S3) storage", "Credit and payment system, admin panel", "Docker Compose and Caddy (HTTPS), e2e tests"],
        ),
    ),
    dict(
        pk=3, slug='e-auksion-radar', title="E-auksion lot radari", kind=LUMARC, order=30, featured=True,
        categories='bot,automation,backend', year_start=2026, ongoing=True, status='live',
        stack='Python (standart kutubxona), SQLite, Telegram Bot API, unittest',
        role=("Fullstack dasturchi", "Fullstack-разработчик", "Fullstack Developer"),
        short=(
            "e-auksion.uz platformasidagi Toshkent lotlarini avtomatik to'plab, saralaydigan va eng yaxshi 10 tasini Telegram'ga yuboradigan dastur.",
            "Программа, которая автоматически собирает лоты Ташкента с e-auksion.uz, отбирает их и отправляет лучшие 10 в Telegram.",
            "A program that automatically collects Tashkent lots from e-auksion.uz, screens them and sends the best 10 to Telegram.",
        ),
        problem=(
            "Auksion platformasida minglab lot mavjud; mos keladiganlarini qo'lda kuzatish ko'p vaqt talab qiladi.",
            "На аукционной площадке тысячи лотов; отслеживать подходящие вручную слишком долго.",
            "The auction platform lists thousands of lots; watching for suitable ones by hand takes too long.",
        ),
        solution=(
            "Dastur haftada ikki marta lotlarni to'playdi, mezonlar fayli bo'yicha saralaydi, narxlarni solishtiradi va ball beradi. Eng yaxshi 10 ta lot tahlili bilan Telegram'ga yuboriladi; yuborilgan lot narxi pasaymaguncha takrorlanmaydi.",
            "Программа дважды в неделю собирает лоты, отбирает их по файлу критериев, сравнивает цены и начисляет баллы. ТОП-10 с анализом отправляется в Telegram; отправленный лот не повторяется, пока не снизится цена.",
            "Twice a week the program collects lots, screens them against a criteria file, compares prices and assigns scores. The TOP-10 with analysis is sent to Telegram; a lot already sent is not repeated unless its price drops.",
        ),
        result=(
            "Dastur serverda jadval asosida ishlamoqda. Kod faqat Python standart kutubxonasiga tayanadi va 200 dan ortiq avtomatik test bilan qoplangan.",
            "Программа работает на сервере по расписанию. Код использует только стандартную библиотеку Python и покрыт более чем 200 автоматическими тестами.",
            "The program runs on a server on a schedule. The code relies only on the Python standard library and is covered by 200+ automated tests.",
        ),
        highlights=(
            ["Mezonlar JSON faylida belgilanadi", "Narxlarni solishtirish va ball tizimi", "Takroriy lotlarni SQLite orqali filtrlash", "Sinov (dry-run) rejimi va jurnal; tashqi bog'liqliklarsiz"],
            ["Критерии задаются в JSON-файле", "Сравнение цен и система баллов", "Фильтрация повторных лотов через SQLite", "Режим проверки (dry-run) и журнал; без внешних зависимостей"],
            ["Criteria defined in a JSON file", "Price comparison and a scoring system", "Duplicate-lot filtering through SQLite", "Dry-run mode and logging; no external dependencies"],
        ),
    ),
    dict(
        pk=4, slug='lumarcode', title='Lumarcode', kind=LUMARC, order=40, featured=True,
        categories='ai,backend,automation', year_start=2026, ongoing=True, status='live',
        live_url='https://akromin.uz',
        stack='Claude, Docker, Caddy, Telegram bot, Linux',
        role=("Fullstack dasturchi", "Fullstack-разработчик", "Fullstack Developer"),
        short=(
            "Jamoa uchun Claude asosidagi ichki AI ish muhiti: chat va kod rejimlari, Telegram bot hamda veb-interfeys.",
            "Внутренняя AI-среда для команды на базе Claude: режимы чата и кода, Telegram-бот и веб-интерфейс.",
            "An internal Claude-based AI workspace for the team: chat and code modes, a Telegram bot and a web interface.",
        ),
        problem=(
            "Jamoa AI vositasidan xavfsiz va yagona nuqtadan foydalanishi, boshqa xizmatlarga ta'sir ko'rsatmasligi zarur edi.",
            "Команде требовался безопасный единый доступ к AI-инструменту без влияния на другие сервисы.",
            "The team needed secure, single-point access to an AI tool without affecting other services.",
        ),
        solution=(
            "Ilova production serverda alohida Docker konteynerida izolyatsiya qilingan holda ishga tushirilgan. Maxfiy kalitlar tasvirdan tashqarida saqlanadi, tashqi kirish Caddy orqali HTTPS bilan ta'minlanadi, joriy etish qarorlari ADR hujjatlarida qayd etilgan.",
            "Приложение запущено на продакшн-сервере в отдельном Docker-контейнере в изоляции. Секреты хранятся вне образа, внешний доступ предоставляется через Caddy по HTTPS, решения по запуску и эксплуатации задокументированы в виде ADR.",
            "The application runs on the production server in its own isolated Docker container. Secrets are kept outside the image, external access goes through Caddy over HTTPS, and launch and operations decisions are documented as ADRs.",
        ),
        result=(
            "Platforma ishlamoqda. Kirish faqat xodimlar uchun ochiq, shu sababli ichki sahifalar ko'rsatilmaydi.",
            "Платформа работает. Доступ открыт только сотрудникам, поэтому внутренние страницы не показываются.",
            "The platform is running. Access is limited to staff, so internal pages are not shown.",
        ),
        highlights=(
            ["Chat va kod rejimlari, Telegram bot va veb-interfeys", "Alohida Docker konteyner, boshqa xizmatlarga ta'sirsiz", "Maxfiy kalitlar tasvirdan tashqarida, HTTPS orqali kirish", "Arxitektura qarorlari ADR sifatida hujjatlashtirilgan"],
            ["Режимы чата и кода, Telegram-бот и веб-интерфейс", "Отдельный Docker-контейнер без влияния на другие сервисы", "Секреты вне образа, доступ по HTTPS", "Архитектурные решения оформлены как ADR"],
            ["Chat and code modes, Telegram bot and web interface", "Separate Docker container with no impact on other services", "Secrets kept outside the image, access over HTTPS", "Architecture decisions documented as ADRs"],
        ),
    ),
    dict(
        pk=5, slug='akromind', title='Akromind', kind=LUMARC, order=50, featured=True,
        categories='web', year_start=2026, ongoing=True, status='in_development',
        live_url='https://akromind.uz',
        stack='Next.js, React, TypeScript, Tailwind CSS, Docker',
        role=("Fullstack dasturchi", "Fullstack-разработчик", "Fullstack Developer"),
        short=(
            "IT va AI yechimlari kompaniyasining veb-sayti: xizmatlar, portfolio, maqolalar va aloqa.",
            "Сайт компании IT- и AI-решений: услуги, портфолио, статьи и контакты.",
            "Website of an IT and AI solutions company: services, portfolio, articles and contact.",
        ),
        problem=(
            "Kompaniyaga xizmat va loyihalarini bir joyda taqdim etuvchi, oson kengaytiriladigan sayt kerak edi.",
            "Компании требовался легко расширяемый сайт, который представляет услуги и проекты в одном месте.",
            "The company needed an easily extendable site presenting its services and projects in one place.",
        ),
        solution=(
            "Sayt Next.js va TypeScript asosida ishlab chiqilgan. Xizmatlar: veb va mobil ilovalar, AI/LLM integratsiyasi, Telegram botlar, IT konsalting. Yangi loyiha bitta ma'lumot faylidagi yozuv orqali qo'shiladi.",
            "Сайт разработан на Next.js и TypeScript. Услуги: веб- и мобильные приложения, интеграция AI/LLM, Telegram-боты, IT-консалтинг. Новый проект добавляется одной записью в файле данных.",
            "The site is built with Next.js and TypeScript. Services: web and mobile apps, AI/LLM integration, Telegram bots, IT consulting. A new project is added with a single entry in a data file.",
        ),
        result=(
            "Sayt ishlab chiqilmoqda va akromind.uz manzilida mavjud.",
            "Сайт находится в разработке и доступен по адресу akromind.uz.",
            "The site is in development and available at akromind.uz.",
        ),
        highlights=(
            ["Next.js, TypeScript, Tailwind CSS", "Portfolio va xizmatlar ma'lumot fayllaridan shakllanadi", "Loyiha sahifalari /loyihalar/<slug> manzilida", "Docker orqali ishga tushiriladi"],
            ["Next.js, TypeScript, Tailwind CSS", "Портфолио и услуги формируются из файлов данных", "Страницы проектов по адресу /loyihalar/<slug>", "Запуск через Docker"],
            ["Next.js, TypeScript, Tailwind CSS", "Portfolio and services are generated from data files", "Project pages at /loyihalar/<slug>", "Runs through Docker"],
        ),
    ),
    # ------------------------------------------------------------ BOTLAR (shaxsiy)
    dict(
        pk=6, slug='moneyflow', title='MoneyFlow', kind=PERSONAL, order=60, featured=True,
        categories='bot,backend', year_start=2026, status='live',
        telegram_url='https://t.me/moneyflow_uz_bot',
        stack='Python, python-telegram-bot, PostgreSQL, SQLAlchemy, Alembic, pandas, openpyxl, ReportLab, Docker',
        role=("Dasturchi (yakka)", "Разработчик (соло)", "Solo developer"),
        short=(
            "Shaxsiy va biznes daromad hamda xarajatlarini yuritish uchun Telegram bot: 6 tilda, Excel va PDF hisobotlari bilan.",
            "Telegram-бот для учёта личных и бизнес-доходов и расходов: 6 языков, отчёты в Excel и PDF.",
            "A Telegram bot for tracking personal and business income and expenses: 6 languages, Excel and PDF reports.",
        ),
        problem=(
            "Murakkab ilovalar tufayli kundalik xarajatlarni yuritish ko'pincha to'xtab qoladi.",
            "Из-за сложных приложений ведение ежедневных расходов часто прекращается.",
            "Tracking daily spending is often abandoned because of overly complex apps.",
        ),
        solution=(
            "Yozuvlar oddiy matn bilan kiritiladi (masalan, «taksi 15 ming»). Bot kunlik, haftalik, oylik va yillik hisobotlarni oldingi davr bilan solishtirib beradi, yozuvlarni sahifalab ko'rsatadi va o'chirish imkonini beradi.",
            "Записи вводятся обычным текстом (например, «такси 15 тыс»). Бот формирует отчёты за день, неделю, месяц и год со сравнением с предыдущим периодом, показывает записи постранично и позволяет их удалять.",
            "Entries are typed as plain text (for example, “taksi 15 ming”). The bot builds daily, weekly, monthly and yearly reports compared with the previous period, lists records with pagination and allows deletion.",
        ),
        result=(
            "Bot faol ishlamoqda; interfeys 6 tilda (uz, ru, en, fr, tr, ar), Excel va PDF eksporti mavjud.",
            "Бот работает; интерфейс на 6 языках (uz, ru, en, fr, tr, ar), доступен экспорт в Excel и PDF.",
            "The bot is live; the interface supports 6 languages (uz, ru, en, fr, tr, ar) with Excel and PDF export.",
        ),
        highlights=(
            ["6 ta interfeys tili", "Yozuvlarni erkin matn orqali kiritish", "Davriy hisobotlar va oldingi davr bilan taqqoslash", "Excel va PDF eksport", "Alembic migratsiyalari, pytest testlari, Docker"],
            ["6 языков интерфейса", "Ввод записей свободным текстом", "Отчёты по периодам со сравнением с предыдущим", "Экспорт в Excel и PDF", "Миграции Alembic, тесты pytest, Docker"],
            ["6 interface languages", "Free-text entry input", "Period reports compared with the previous period", "Excel and PDF export", "Alembic migrations, pytest tests, Docker"],
        ),
    ),
    dict(
        pk=7, slug='saveclip', title='SaveClip', kind=PERSONAL, order=70, featured=True,
        categories='bot,automation', year_start=2026, status='live',
        telegram_url='https://t.me/saveclipuz_bot',
        stack='Python, python-telegram-bot, yt-dlp, ffmpeg, SQLite, APScheduler, Docker',
        role=("Dasturchi (yakka)", "Разработчик (соло)", "Solo developer"),
        short=(
            "Instagram, TikTok, Twitter/X va Pinterest havolalaridan video va rasmlarni sifatini saqlagan holda yuklab beruvchi Telegram bot.",
            "Telegram-бот, скачивающий видео и изображения по ссылкам Instagram, TikTok, Twitter/X и Pinterest без потери качества.",
            "A Telegram bot that downloads videos and images from Instagram, TikTok, Twitter/X and Pinterest links without losing quality.",
        ),
        problem=(
            "Yuklash saytlari reklamaga to'la, katta videolar esa sifati pasaytirilgan yoki bo'laklarga bo'lingan holda yetib keladi.",
            "Сайты для скачивания забиты рекламой, а большие видео приходят в сниженном качестве или по частям.",
            "Download sites are full of ads, and large videos arrive in reduced quality or in pieces.",
        ),
        solution=(
            "Foydalanuvchi havola yuboradi, bot videoni HD, 2K yoki 4K sifatda qaytaradi; 50 MB dan katta fayllar ham sifatini yo'qotmaydi. Har bir videoga «Qo'shiqni yuklab olish» (MP3) tugmasi qo'shiladi. Bot guruhga qo'shilsa, yuborilgan havolalarni o'zi yuklab beradi.",
            "Пользователь отправляет ссылку, бот возвращает видео в HD, 2K или 4K; крупные файлы, в том числе больше 50 МБ, приходят без потери качества. К каждому видео добавляется кнопка «Скачать песню» (MP3). Если добавить бота в группу, он сам скачивает присланные ссылки.",
            "The user sends a link and the bot returns the video in HD, 2K or 4K; large files, including those over 50 MB, arrive without quality loss. Every video gets a “Download the song” (MP3) button. Add the bot to a group and it downloads links posted there.",
        ),
        result=(
            "Bot faol ishlamoqda: so'rovlar chastotasi cheklovi, majburiy kanal obunasi, boshqaruv paneli va ommaviy xabar yuborish, SSRF himoyasi mavjud; interfeys uz, ru va en tillarida.",
            "Бот работает: ограничение частоты запросов, обязательная подписка на канал, админ-панель и рассылка, защита от SSRF; интерфейс на uz, ru и en.",
            "The bot is live with rate limiting, mandatory channel subscription, an admin panel with broadcast and SSRF protection; the interface is available in uz, ru and en.",
        ),
        highlights=(
            ["Instagram (Reels, post, karusel), TikTok (suv belgisiz), Twitter/X, Pinterest (rasmlar asl sifatida)", "50 MB dan katta videolar sifatini yo'qotmasdan yuboriladi", "HD, 2K, 4K sifatlar va MP3 yuklab olish tugmasi", "Guruhlarda ishlash: yuborilgan havola avtomatik yuklanadi", "Tezkor ishlash; uz, ru, en tillari"],
            ["Instagram (Reels, посты, карусели), TikTok (без водяного знака), Twitter/X, Pinterest (изображения в оригинальном качестве)", "Крупные видео, включая файлы больше 50 МБ, приходят без потери качества", "Качество HD, 2K, 4K и кнопка MP3 («Скачать песню»)", "Работа в группах: присланные ссылки скачиваются автоматически", "Быстрая работа; языки uz, ru, en"],
            ["Instagram (Reels, posts, carousels), TikTok (no watermark), Twitter/X, Pinterest (images in original quality)", "Large videos, including files over 50 MB, arrive without quality loss", "HD, 2K and 4K quality and an MP3 (“Download the song”) button", "Group mode: links posted in the chat are downloaded automatically", "Fast performance; uz, ru, en languages"],
        ),
    ),
    dict(
        pk=8, slug='uzstroymarket', title='UzStroyMarket', kind=PERSONAL, order=55, featured=True,
        categories='web,backend', year_start=2026, status='live',
        live_url='https://uzstroymarket.uz',
        stack='Next.js 15, React 19, TypeScript, Fastify 5, Prisma, PostgreSQL, grammY, AWS',
        role=("Fullstack dasturchi", "Fullstack-разработчик", "Fullstack Developer"),
        short=(
            "Qurilish materiallari uchun ko'p sotuvchili marketplace: xaridor sayti, sotuvchi va bosh administrator panellari hamda Telegram orqali telefon raqamini tasdiqlash boti.",
            "Мультивендорный маркетплейс стройматериалов: сайт покупателя, панели продавца и главного администратора и Telegram-бот подтверждения телефона.",
            "A multi-vendor marketplace for construction materials: customer site, seller and head-admin panels, and a Telegram bot that verifies phone numbers.",
        ),
        problem=(
            "Qurilish materiallarini qidirish, takliflarni solishtirish va buyurtma berish turli kanallarga tarqoq; bir nechta sotuvchi bilan ishlaganda qoldiq va buyurtmalarni to'g'ri yuritish murakkab.",
            "Поиск стройматериалов, сравнение предложений и оформление заказа разбросаны по разным каналам; при работе с несколькими продавцами сложно корректно вести остатки и заказы.",
            "Finding construction materials, comparing offers and ordering are scattered across channels, and keeping stock and orders correct across several sellers is hard.",
        ),
        solution=(
            "Xaridor, sotuvchi va administrator yagona tizimda ishlaydi. Buyurtma rasmiylashtirilganda qoldiq tranzaksiya ichida tekshirilib band qilinadi, bir xil kalit bilan takroriy so'rov yangi buyurtma yaratmaydi, bir nechta do'kondan iborat savat sotuvchilar bo'yicha alohida buyurtmalarga ajratiladi. Administrator o'zgarishlari audit yozuvlarida saqlanadi.",
            "Покупатель, продавец и администратор работают в единой системе. При оформлении заказа остаток проверяется и резервируется внутри транзакции, повторный запрос с тем же ключом не создаёт новый заказ, корзина из нескольких магазинов делится на отдельные заказы по продавцам. Изменения администратора сохраняются в журнале аудита.",
            "Buyer, seller and administrator work in one system. At checkout, stock is checked and reserved inside a transaction, a repeated request with the same key does not create a new order, and a cart from several stores is split into a separate order per seller. Admin changes are kept in audit records.",
        ),
        result=(
            "Platforma uzstroymarket.uz manzilida ishlamoqda (uz, ru, en; kunduzgi va tungi rejim). Ro'yxatdan o'tishda telefon raqami Telegram bot orqali olti xonali kod bilan tasdiqlanadi.",
            "Платформа работает на uzstroymarket.uz (uz, ru, en; дневной и ночной режим). При регистрации телефон подтверждается через Telegram-бота шестизначным кодом.",
            "The platform runs at uzstroymarket.uz (uz, ru, en; day and night themes). During sign-up the phone number is verified through a Telegram bot with a six-digit code.",
        ),
        highlights=(
            ["Uch rol: xaridor, sotuvchi (alohida kabinet), bosh administrator", "Qoldiqni tranzaksiyada band qilish va idempotent checkout", "Ko'p do'konli savat sotuvchilar bo'yicha alohida buyurtmalarga ajratiladi", "Administrator o'zgarishlari uchun audit yozuvlari", "Telegram orqali telefonni tasdiqlash, uch til, kunduzgi va tungi rejim"],
            ["Три роли: покупатель, продавец (отдельный кабинет), главный администратор", "Резервирование остатка в транзакции и идемпотентный checkout", "Корзина из нескольких магазинов делится на заказы по продавцам", "Журнал аудита изменений администратора", "Подтверждение телефона через Telegram, три языка, дневной и ночной режим"],
            ["Three roles: buyer, seller (own dashboard), head administrator", "Stock reservation in a transaction and idempotent checkout", "A multi-store cart is split into orders per seller", "Audit records for admin changes", "Telegram phone verification, three languages, day and night theme"],
        ),
    ),
]
