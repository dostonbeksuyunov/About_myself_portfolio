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
        pk=2, slug='lumarcos', title='Lumarcos', kind=LUMARC, order=20, featured=True,
        categories='ai,web,backend', year_start=2026, ongoing=True, status='live',
        live_url='https://lumarcos.uz',
        stack='Next.js 16, React 19, NestJS 11, Prisma, PostgreSQL, BullMQ, Redis, MinIO, Docker Compose, Caddy, Gemini / Vertex AI, Kie.ai',
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
            ["pnpm monorepo: NestJS API, Next.js web va umumiy paket", "Gemini / Vertex AI va Kie.ai integratsiyasi", "BullMQ navbati, MinIO (S3) ombor, sharp bilan rasm ishlov", "Kredit va to'lov (Payme, Click), admin panel", "Docker Compose + Caddy (HTTPS), deploy skripti; Playwright e2e smoke"],
            ["pnpm-монорепо: NestJS API, Next.js web и общий пакет", "Интеграция Gemini / Vertex AI и Kie.ai", "Очередь BullMQ, хранилище MinIO (S3), обработка изображений sharp", "Кредиты и оплата (Payme, Click), админ-панель", "Docker Compose + Caddy (HTTPS), скрипт деплоя; Playwright e2e smoke"],
            ["pnpm monorepo: NestJS API, Next.js web and a shared package", "Gemini / Vertex AI and Kie.ai integration", "BullMQ queue, MinIO (S3) storage, image processing with sharp", "Credits and payments (Payme, Click), admin panel", "Docker Compose + Caddy (HTTPS), deploy script; Playwright e2e smoke"],
        ),
    ),
    dict(
        pk=3, slug='e-auksion-radar', title="E-auksion lot radari", kind=LUMARC, order=30, featured=True,
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
        pk=4, slug='lumarcode', title='Lumarcode', kind=LUMARC, order=40, featured=True,
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
        pk=5, slug='akromind', title='Akromind', kind=LUMARC, order=50, featured=True,
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
        pk=6, slug='moneyflow', title='MoneyFlow', kind=PERSONAL, order=60, featured=True,
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
        pk=7, slug='saveclip', title='SaveClip', kind=PERSONAL, order=70, featured=True,
        categories='bot,automation', year_start=2026, status='live',
        telegram_url='https://t.me/saveclipuz_bot',
        stack='Python, python-telegram-bot, yt-dlp, ffmpeg, SQLite, APScheduler, Docker',
        role=("Dasturchi (yakka)", "Разработчик (соло)", "Solo developer"),
        short=(
            "Instagram, TikTok, Twitter/X va Pinterest havolalaridan video va rasmlarni sifatini buzmasdan yuklab beruvchi Telegram bot.",
            "Telegram-бот, скачивающий видео и изображения по ссылкам Instagram, TikTok, Twitter/X и Pinterest без потери качества.",
            "A Telegram bot that downloads videos and images from Instagram, TikTok, Twitter/X and Pinterest links without losing quality.",
        ),
        problem=(
            "Video yuklash uchun saytlar reklamaga to'la, katta videolar esa sifati tushirilib yoki bo'laklab yuboriladi.",
            "Сайты для скачивания видео забиты рекламой, а большие видео приходят в сниженном качестве или по частям.",
            "Video download sites are full of ads, and large videos arrive in reduced quality or in pieces.",
        ),
        solution=(
            "Havola yuboriladi — bot uni yuklab, HD / 2K / 4K sifatlarda yuboradi; 50 MB dan katta videolar ham sifati buzilmasdan keladi. Har bir videoga «Qo'shiqni yuklab olish» (MP3) tugmasi qo'shiladi. Botni guruhga qo'shsangiz, tashlangan havolani o'zi yuklab beradi.",
            "Отправляете ссылку — бот скачивает и присылает видео в HD / 2K / 4K; большие видео, включая файлы больше 50 МБ, приходят без потери качества. К каждому видео добавляется кнопка «Скачать песню» (MP3). Если добавить бота в группу, он сам скачивает присланные ссылки.",
            "Send a link and the bot downloads it and returns the video in HD / 2K / 4K; large videos, including files over 50 MB, arrive without quality loss. Every video gets a “Download the song” (MP3) button. Add the bot to a group and it downloads any link posted there.",
        ),
        result=(
            "Bot jonli ishlaydi: tezlik cheklovi, majburiy kanal obunasi, admin panel va ommaviy xabar, SSRF himoyasi bilan; uz, ru va en tillarida.",
            "Бот работает: ограничение частоты, обязательная подписка на канал, админ-панель и рассылка, защита от SSRF; интерфейс на uz, ru и en.",
            "The bot is live with rate limiting, mandatory channel subscription, an admin panel with broadcast and SSRF protection; the interface is available in uz, ru and en.",
        ),
        highlights=(
            ["Instagram (Reels, post, karusel), TikTok (suv belgisiz), Twitter/X, Pinterest (rasmlar asl sifatda)", "50 MB dan katta videolar ham sifati buzilmasdan yuboriladi", "HD / 2K / 4K sifatlar va har videoga MP3 («Qo'shiqni yuklab olish») tugmasi", "Guruhga qo'shib ishlatish: havola tashlansa bot o'zi yuklab beradi", "Tezroq ishlaydi; uz / ru / en tillari"],
            ["Instagram (Reels, пост, карусель), TikTok (без водяного знака), Twitter/X, Pinterest (изображения в оригинальном качестве)", "Большие видео, в том числе больше 50 МБ, приходят без потери качества", "Качество HD / 2K / 4K и кнопка MP3 («Скачать песню») у каждого видео", "Работа в группе: бот сам скачивает присланные ссылки", "Быстрее работает; языки uz / ru / en"],
            ["Instagram (Reels, posts, carousels), TikTok (no watermark), Twitter/X, Pinterest (images in original quality)", "Large videos, including files over 50 MB, arrive without quality loss", "HD / 2K / 4K quality and an MP3 (“Download the song”) button on every video", "Group mode: the bot downloads links posted in the chat", "Runs faster; uz / ru / en languages"],
        ),
    ),
    dict(
        pk=8, slug='uzstroymarket', title='UzStroyMarket', kind=PERSONAL, order=55, featured=True,
        categories='web,backend', year_start=2026, status='live',
        live_url='https://uzstroymarket.uz',
        stack='Next.js 15, React 19, TypeScript, Fastify 5, Prisma, PostgreSQL, grammY, AWS',
        role=("Fullstack dasturchi", "Fullstack-разработчик", "Fullstack Developer"),
        short=(
            "Qurilish materiallari uchun ko'p sotuvchili marketplace: xaridor sayti, sotuvchi va bosh admin panellari hamda Telegram orqali telefonni tasdiqlash boti.",
            "Мультивендорный маркетплейс строительных материалов: сайт покупателя, панели продавца и главного администратора и Telegram-бот подтверждения телефона.",
            "A multi-vendor marketplace for construction materials: customer site, seller and head-admin panels, and a Telegram bot that verifies phone numbers.",
        ),
        problem=(
            "Qurilish materiallarini topish, do'konlar takliflarini solishtirish va buyurtma berish tarqoq kanallarda yuradi; bir nechta sotuvchi bilan ishlaganda qoldiq va buyurtmalarni to'g'ri yuritish qiyin.",
            "Поиск стройматериалов, сравнение предложений магазинов и заказ разбросаны по разным каналам; при работе с несколькими продавцами сложно корректно вести остатки и заказы.",
            "Finding construction materials, comparing store offers and ordering are scattered across channels, and keeping stock and orders correct across several sellers is hard.",
        ),
        solution=(
            "Xaridor, sotuvchi va administrator bitta tizimda ishlaydi. Checkout'da qoldiq tranzaksiya ichida tekshiriladi va band qilinadi, takroriy so'rov bir xil kalit bilan yangi buyurtma yaratmaydi, bir nechta do'kondan tuzilgan savat har bir sotuvchi uchun alohida buyurtmaga ajratiladi. Admin o'zgarishlari audit yozuvlari bilan saqlanadi.",
            "Покупатель, продавец и администратор работают в одной системе. При оформлении заказа остаток проверяется и резервируется внутри транзакции, повторный запрос с тем же ключом не создаёт новый заказ, корзина из нескольких магазинов делится на отдельные заказы по продавцам. Изменения администратора сохраняются в журнале аудита.",
            "Buyer, seller and administrator work in one system. At checkout, stock is checked and reserved inside a transaction, a repeated request with the same key does not create a new order, and a cart built from several stores is split into a separate order per seller. Admin changes are kept in audit records.",
        ),
        result=(
            "Platforma uzstroymarket.uz da jonli ishlaydi (uz / ru / en, kunduz va tun rejimi). Ro'yxatdan o'tishda telefon raqami Telegram boti orqali olti xonali kod bilan tasdiqlanadi.",
            "Платформа работает на uzstroymarket.uz (uz / ru / en, дневной и ночной режим). При регистрации телефон подтверждается через Telegram-бота шестизначным кодом.",
            "The platform runs live at uzstroymarket.uz (uz / ru / en, day and night themes). During sign-up the phone number is verified through a Telegram bot with a six-digit code.",
        ),
        highlights=(
            ["Uch rol: xaridor, sotuvchi (alohida kabinet), bosh admin", "Tranzaksiyada qoldiqni band qilish va idempotent checkout", "Ko'p do'konli savat → sotuvchi bo'yicha alohida buyurtmalar", "Admin o'zgarishlari uchun audit yozuvlari", "Telegram boti orqali telefonni tasdiqlash, uz/ru/en, kunduz/tun rejimi"],
            ["Три роли: покупатель, продавец (отдельный кабинет), главный админ", "Резервирование остатка в транзакции и идемпотентный checkout", "Корзина из нескольких магазинов → отдельные заказы по продавцам", "Журнал аудита изменений администратора", "Подтверждение телефона через Telegram-бота, uz/ru/en, дневной/ночной режим"],
            ["Three roles: buyer, seller (own dashboard), head admin", "Stock reservation in a transaction and idempotent checkout", "Multi-store cart → separate orders per seller", "Audit records for admin changes", "Telegram phone verification, uz/ru/en, day/night theme"],
        ),
    ),
]
