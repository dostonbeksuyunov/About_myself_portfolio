"""Sayt matnlari (uz / ru / en). Loyihalar bu yerda emas — ular Project modelida
(core/fixtures/projects.json, admin orqali tahrirlanadi)."""

LANGUAGES = ('uz', 'ru', 'en')

CONTACT = {
    'email': 'dostonbeksuyunov444@gmail.com',
    'phone': '+998775353104',
    'phone_display': '+998 77 535 31 04',
    'github': 'https://github.com/dostonbeksuyunov',
    'github_handle': '@dostonbeksuyunov',
    'linkedin': 'https://linkedin.com/in/dostonbek-suyunov',
    'linkedin_handle': 'dostonbek-suyunov',
    'telegram': 'https://t.me/Dostonbek_Suyunov',
    'telegram_handle': '@Dostonbek_Suyunov',
    'instagram': 'https://www.instagram.com/suyunov.dev_',
    'instagram_handle': '@suyunov.dev_',
    'group': 'https://t.me/IT_vs_AI_XIZMATLAR_Uz',
    'group_handle': '@IT_vs_AI_XIZMATLAR_Uz',
}

# Ko'nikmalar: (kalit, [elementlar]) — tartib saqlanadi
SKILLS = {
    'languages': ['Python', 'TypeScript', 'JavaScript', 'SQL'],
    'frontend': ['React', 'Next.js (App Router)', 'Tailwind CSS', 'Framer Motion', 'GSAP',
                 'Three.js / React Three Fiber', 'i18next / next-intl'],
    'backend': ['Django', 'DRF', 'FastAPI', 'NestJS', 'Prisma', 'SQLAlchemy', 'REST API', 'JWT',
                'Celery', 'BullMQ', 'WebSockets', 'python-telegram-bot', 'aiogram'],
    'data': ['PostgreSQL', 'Redis', 'SQLite'],
    'devops': ['Docker', 'Docker Compose', 'Nginx', 'Caddy', 'Linux', 'Git / GitHub', 'CI/CD',
               'pytest', 'Jest', 'Vitest', 'Playwright'],
    'ai': ['AI-assisted development (Claude Code)', 'Generativ AI API integratsiyasi',
           'Gemini / Vertex AI', 'Kie.ai', 'Claude API', 'Prompt engineering'],
}

SKILL_CATEGORY_LABELS = {
    'uz': {'languages': 'Tillar', 'frontend': 'Frontend', 'backend': 'Backend',
           'data': "Ma'lumotlar", 'devops': 'DevOps va test', 'ai': 'AI'},
    'ru': {'languages': 'Языки', 'frontend': 'Frontend', 'backend': 'Backend',
           'data': 'Данные', 'devops': 'DevOps и тесты', 'ai': 'AI'},
    'en': {'languages': 'Languages', 'frontend': 'Frontend', 'backend': 'Backend',
           'data': 'Data', 'devops': 'DevOps & testing', 'ai': 'AI'},
}

SERVICES = [
    {
        'icon': 'bot',
        'title': {'uz': 'Telegram botlar', 'ru': 'Telegram-боты', 'en': 'Telegram bots'},
        'desc': {
            'uz': "Mijozlar bilan ishlash, buyurtma va to'lov jarayonlari, admin panel hamda mini-ilovalar.",
            'ru': "Работа с клиентами, заказы и оплата, админ-панель и мини-приложения.",
            'en': "Customer service, orders and payments, admin panels and mini apps.",
        },
    },
    {
        'icon': 'web',
        'title': {'uz': 'Veb-saytlar', 'ru': 'Веб-сайты', 'en': 'Websites'},
        'desc': {
            'uz': "Landing page, korporativ sayt va onlayn-do'kon: tezkor, SEO talablariga mos, ko'p tilli.",
            'ru': "Лендинги, корпоративные сайты и интернет-магазины: быстрые, с SEO и поддержкой нескольких языков.",
            'en': "Landing pages, corporate sites and online stores: fast, SEO-ready and multilingual.",
        },
    },
    {
        'icon': 'ai',
        'title': {'uz': 'AI integratsiya va avtomatlashtirish', 'ru': 'AI-интеграция и автоматизация', 'en': 'AI integration & automation'},
        'desc': {
            'uz': "Generativ AI'ni mahsulotga ulash, jarayonlarni avtomatlashtirish va ichki AI vositalarini yaratish.",
            'ru': "Подключение генеративного ИИ к продукту, автоматизация процессов и создание внутренних AI-инструментов.",
            'en': "Connecting generative AI to your product, process automation and internal AI tools.",
        },
    },
    {
        'icon': 'student',
        'title': {'uz': 'Talabalar uchun', 'ru': 'Для студентов', 'en': 'For students'},
        'desc': {
            'uz': "Taqdimot, diplom va kurs ishlari bo'yicha texnik yordam.",
            'ru': "Техническая помощь с презентациями, дипломными и курсовыми работами.",
            'en': "Technical help with presentations, diploma and coursework projects.",
        },
    },
    {
        'icon': 'rocket',
        'title': {'uz': 'Mavjud loyihalar', 'ru': 'Существующие проекты', 'en': 'Existing projects'},
        'desc': {
            'uz': "Audit, xatolarni bartaraf etish, qo'llab-quvvatlash va yangilash.",
            'ru': "Аудит, исправление ошибок, поддержка и обновление.",
            'en': "Audit, bug fixing, maintenance and updates.",
        },
    },
]

# Tajriba va ta'lim. 'projects' — Lumarc'da qilingan ishlar (DB'dan, kind=work)
TIMELINE = [
    {
        'kind': 'work',
        'title': {'uz': 'Fullstack Developer', 'ru': 'Fullstack Developer', 'en': 'Fullstack Developer'},
        'org': {'uz': "Lumarc — arxitektura va dizayn studiyasi, Toshkent",
                'ru': 'Lumarc — архитектурно-дизайнерская студия, Ташкент',
                'en': 'Lumarc — architecture and design studio, Tashkent'},
        'period': {'uz': '2026-yil sentabr — hozirgacha', 'ru': 'сентябрь 2026 — по настоящее время',
                   'en': 'September 2026 – present'},
        'desc': {
            'uz': "Veb-sayt, AI platforma, avtomatlashtirish boti va ichki AI vositasini ishlab chiqish: dizayndan ishga tushirishgacha.",
            'ru': "Разработка сайта, AI-платформы, бота автоматизации и внутреннего AI-инструмента: от дизайна до запуска.",
            'en': "Development of the website, AI platform, automation bot and an internal AI tool, from design to launch.",
        },
        'with_projects': True,
    },
    {
        'kind': 'study',
        'title': {'uz': 'Python Backend Development Program', 'ru': 'Python Backend Development Program', 'en': 'Python Backend Development Program'},
        'org': {'uz': 'Ustudy Academy, IT Park Uzbekistan', 'ru': 'Ustudy Academy, IT Park Uzbekistan', 'en': 'Ustudy Academy, IT Park Uzbekistan'},
        'period': {'uz': '2025-yil sentabr — 2026-yil sentabr', 'ru': 'сентябрь 2025 — сентябрь 2026', 'en': 'September 2025 – September 2026'},
        'desc': {
            'uz': "Python, PostgreSQL, Django/DRF, Celery/Channels va Docker/CI-CD bo'yicha 12 modulli intensiv dastur. Yakunlangan.",
            'ru': "Интенсивная программа из 12 модулей: Python, PostgreSQL, Django/DRF, Celery/Channels и Docker/CI-CD. Завершена.",
            'en': "Intensive 12-module program covering Python, PostgreSQL, Django/DRF, Celery/Channels and Docker/CI-CD. Completed.",
        },
    },
    {
        'kind': 'study',
        'title': {'uz': 'Prompt Engineering for AI Systems', 'ru': 'Prompt Engineering for AI Systems', 'en': 'Prompt Engineering for AI Systems'},
        'org': {'uz': "Five Million AI Leaders (O'zbekiston va BAA)", 'ru': 'Five Million AI Leaders (Узбекистан и ОАЭ)', 'en': 'Five Million AI Leaders (Uzbekistan & UAE)'},
        'period': {'uz': '2026-yil mart', 'ru': 'март 2026', 'en': 'March 2026'},
        'desc': {'uz': '', 'ru': '', 'en': ''},
    },
    {
        'kind': 'study',
        'title': {'uz': 'Meta Back-End Developer Professional Certificate', 'ru': 'Meta Back-End Developer Professional Certificate', 'en': 'Meta Back-End Developer Professional Certificate'},
        'org': {'uz': 'Coursera (Meta)', 'ru': 'Coursera (Meta)', 'en': 'Coursera (Meta)'},
        'period': {'uz': '2025-yil iyun', 'ru': 'июнь 2025', 'en': 'June 2025'},
        'desc': {
            'uz': "Python, Django, REST API va ma'lumotlar bazalari bo'yicha 9 kursdan iborat dastur.",
            'ru': "Программа из 9 курсов по Python, Django, REST API и базам данных.",
            'en': "A 9-course program covering Python, Django, REST APIs and databases.",
        },
    },
    {
        'kind': 'study',
        'title': {'uz': 'Computer Science and Programming Technologies — Bakalavr', 'ru': 'Computer Science and Programming Technologies — бакалавр', 'en': "Computer Science and Programming Technologies — Bachelor's Degree"},
        'org': {'uz': "O'zbekiston Milliy Universiteti", 'ru': 'Национальный университет Узбекистана', 'en': 'National University of Uzbekistan'},
        'period': {'uz': '2022 — 2026', 'ru': '2022 — 2026', 'en': '2022 — 2026'},
        'desc': {'uz': '', 'ru': '', 'en': ''},
    },
]

# --- UI matnlari: kalit -> (uz, ru, en)
_STRINGS = {
    'name_first': ('Dostonbek', 'Достонбек', 'Dostonbek'),
    'name_last': ('Suyunov', 'Суюнов', 'Suyunov'),
    'initials': ('DS.', 'ДС.', 'DS.'),
    'badge_location': ("TOSHKENT, O'ZBEKISTON", 'ТАШКЕНТ, УЗБЕКИСТАН', 'TASHKENT, UZBEKISTAN'),
    'hero_role': ('Fullstack dasturchi', 'Fullstack-разработчик', 'Fullstack Developer'),
    'hero_tagline': (
        "Python/Django va Next.js asosida veb-mahsulotlarni g'oyadan ishga tushirishgacha to'liq ishlab chiqaman.",
        "Разрабатываю веб-продукты на Python/Django и Next.js — от идеи до запуска.",
        "I build web products with Python/Django and Next.js — from idea to launch.",
    ),
    'btn_projects': ("Loyihalarni ko'rish", 'Смотреть проекты', 'View projects'),
    'btn_contact': (
        "Aloqa",
        "Контакты",
        "Contact",
    ),
    'btn_resume': (
        "Rezyumeni yuklab olish",
        "Скачать резюме",
        "Download résumé",
    ),
    'btn_hire': (
        "Murojaat qilish",
        "Обратиться",
        "Get in touch",
    ),
    'hire_personal': ('Shaxsiy Telegram', 'Личный Telegram', 'Personal Telegram'),
    'hire_group': ('Guruh', 'Группа', 'Group'),
    'theme_to_dark': ('Tungi rejim', 'Ночной режим', 'Dark mode'),
    'theme_to_light': ('Kunduzgi rejim', 'Дневной режим', 'Light mode'),
    'scroll_label': ('PASTGA', 'ВНИЗ', 'SCROLL'),
    'skip_link': (
        "Asosiy mazmunga o'tish",
        "Перейти к содержимому",
        "Skip to content",
    ),
    'menu_label': ('Menyu', 'Меню', 'Menu'),
    'nav_home': ('Bosh sahifa', 'Главная', 'Home'),
    'nav_about': ('Men haqimda', 'Обо мне', 'About'),
    'nav_projects': ('Loyihalar', 'Проекты', 'Projects'),
    'nav_skills': ("Ko'nikmalar", 'Навыки', 'Skills'),
    'nav_services': ('Xizmatlar', 'Услуги', 'Services'),
    'nav_experience': ('Tajriba', 'Опыт', 'Experience'),
    'nav_contact': ("Aloqa", 'Контакты', 'Contact'),
    'about_title': ('Men haqimda', 'Обо мне', 'About me'),
    'about_text': (
        "Python/Django texnologiyalari asosida backend dasturlash, shuningdek, Next.js, React va TypeScript texnologiyalaridan foydalangan holda frontend ishlab chiqish yo'nalishlarida faoliyat yurituvchi Fullstack dasturchiman.\n\n2026-yil sentabr oyidan buyon Lumarc studiyasida faoliyat yuritib kelmoqdaman. Faoliyatim davomida kompaniyaning rasmiy veb-sayti, sun'iy intellekt asosidagi platformasi, biznes jarayonlarini avtomatlashtirish boti hamda ichki foydalanish uchun mo'ljallangan AI vositasini ishlab chiqishda ishtirok etganman.\n\nMa'lumotim bo'yicha Computer Science yo'nalishi bakalavr darajasiga egaman. Shuningdek, Ustudy Academy (IT Park) tomonidan tashkil etilgan Python Backend dasturini tamomlaganman hamda Meta Back-End Developer professional sertifikatiga egaman.",
        "Я Fullstack-разработчик: занимаюсь backend-разработкой на технологиях Python/Django, а также frontend-разработкой на Next.js, React и TypeScript.\n\nС сентября 2026 года работаю в студии Lumarc. За это время принимал участие в разработке официального сайта компании, платформы на основе искусственного интеллекта, бота для автоматизации бизнес-процессов и внутреннего AI-инструмента.\n\nИмею степень бакалавра по направлению Computer Science. Также окончил программу Python Backend, организованную Ustudy Academy (IT Park), и являюсь обладателем профессионального сертификата Meta Back-End Developer.",
        "I am a Fullstack developer working on backend development with Python/Django and on frontend development with Next.js, React and TypeScript.\n\nI have been working at the Lumarc studio since September 2026. During this time I have taken part in building the company's official website, an artificial-intelligence-based platform, a bot for automating business processes and an AI tool for internal use.\n\nI hold a Bachelor's degree in Computer Science. I have also completed the Python Backend program organised by Ustudy Academy (IT Park) and hold the Meta Back-End Developer professional certificate.",
    ),
    'edu_label': ("Ta'lim", 'Образование', 'Education'),
    'edu_degree': ('Computer Science and Programming Technologies — Bakalavr', 'Computer Science and Programming Technologies — бакалавр', "Computer Science and Programming Technologies — Bachelor's Degree"),
    'edu_org': ("O'zbekiston Milliy Universiteti · 2022–2026", 'Национальный университет Узбекистана · 2022–2026', 'National University of Uzbekistan · 2022–2026'),
    'stat_projects': ('loyiha', 'проектов', 'projects'),
    'stat_live': (
        "faol mahsulot",
        "работающих продуктов",
        "live products",
    ),
    'stat_tech': ('texnologiya', 'технологий', 'technologies'),
    'stat_years': ('yil amaliy tajriba', 'года практики', 'years hands-on'),
    'projects_title': ('Loyihalar', 'Проекты', 'Projects'),
    'projects_intro': (
        "Ish joyida va shaxsan bajarilgan loyihalar. Har bir loyiha uchun muammo, yechim va natija bayon etilgan.",
        "Проекты, выполненные по месту работы и самостоятельно. Для каждого проекта описаны проблема, решение и результат.",
        "Projects delivered at work and independently. Each one describes the problem, the solution and the result.",
    ),
    'work_block_title': (
        "Lumarc'da bajarilgan loyihalar",
        "Проекты, выполненные в Lumarc",
        "Delivered at Lumarc",
    ),
    'other_block_title': (
        "Boshqa loyihalar",
        "Другие проекты",
        "Other projects",
    ),
    'all_projects': ('Barcha loyihalar', 'Все проекты', 'All projects'),
    'open_case': (
        "Batafsil",
        "Подробнее",
        "View details",
    ),
    'learning_title': ("O'quv va mashqlar", 'Учебные проекты', 'Learning & practice'),
    'filter_kind': ('Turi', 'Тип', 'Type'),
    'filter_category': ("Yo'nalish", 'Направление', 'Category'),
    'filter_all': ('Hammasi', 'Все', 'All'),
    'filter_empty': (
        "Tanlangan filtr bo'yicha loyiha topilmadi.",
        "По выбранному фильтру проектов нет.",
        "No projects match the selected filter.",
    ),
    'kind_work': ('Ish', 'Работа', 'Work'),
    'kind_client': ('Mijoz', 'Клиент', 'Client'),
    'kind_personal': ('Shaxsiy', 'Личный', 'Personal'),
    'kind_learning': ("O'quv", 'Учебный', 'Learning'),
    'status_live': (
        "Faol",
        "Работает",
        "Live",
    ),
    'status_in_development': ('Ishlab chiqilmoqda', 'В разработке', 'In development'),
    'status_archived': ('Arxiv', 'Архив', 'Archived'),
    'status_concept': ('Konsept', 'Концепт', 'Concept'),
    'cat_web': ('Web', 'Web', 'Web'),
    'cat_bot': ('Bot', 'Боты', 'Bots'),
    'cat_ai': ('AI', 'AI', 'AI'),
    'cat_backend': ('Backend', 'Backend', 'Backend'),
    'cat_3d': ('3D', '3D', '3D'),
    'cat_automation': ('Avtomatlashtirish', 'Автоматизация', 'Automation'),
    'case_problem': ('Muammo', 'Проблема', 'Problem'),
    'case_solution': ('Yechim', 'Решение', 'Solution'),
    'case_result': ('Natija', 'Результат', 'Result'),
    'case_highlights': ('Asosiy jihatlar', 'Ключевые моменты', 'Highlights'),
    'case_stack': ('Texnologiyalar', 'Технологии', 'Tech stack'),
    'case_gallery': ('Galereya', 'Галерея', 'Gallery'),
    'case_role': ('Rol', 'Роль', 'Role'),
    'case_year': ('Yil', 'Год', 'Year'),
    'case_status': ('Holat', 'Статус', 'Status'),
    'case_type': ('Turi', 'Тип', 'Type'),
    'case_back': ('← Barcha loyihalar', '← Все проекты', '← All projects'),
    'case_prev': ('Oldingi', 'Предыдущий', 'Previous'),
    'case_next': ('Keyingi', 'Следующий', 'Next'),
    'link_live': (
        "Saytga o'tish",
        "Открыть сайт",
        "Visit site",
    ),
    'link_telegram': (
        "Telegram botga o'tish",
        "Открыть Telegram-бота",
        "Open Telegram bot",
    ),
    'link_github': ("Kodni ko'rish", 'Смотреть код', 'View code'),
    'code_closed': (
        "Kod yopiq (tijorat loyihasi)",
        "Код закрыт (коммерческий проект)",
        "Code is private (commercial project)",
    ),
    'nda_note': (
        "Loyiha maxfiylik kelishuvi (NDA) doirasida bajarilgan; batafsil ma'lumot shaxsan taqdim etiladi.",
        "Проект выполнен в рамках соглашения о неразглашении (NDA); подробности предоставляются лично.",
        "This project is covered by an NDA; details are provided in person.",
    ),
    'contact_phone': ('Telefon', 'Телефон', 'Phone'),
    'contact_resume': (
        "Rezyume",
        "Резюме",
        "Résumé",
    ),
    'footer_about': (
        "Fullstack dasturchi. Python/Django, Next.js va AI integratsiya. Toshkent, O'zbekiston.",
        "Fullstack-разработчик. Python/Django, Next.js и AI-интеграция. Ташкент, Узбекистан.",
        "Fullstack developer. Python/Django, Next.js and AI integration. Tashkent, Uzbekistan.",
    ),
    'footer_links': ('Havolalar', 'Ссылки', 'Links'),
    'footer_contact': ('Aloqa', 'Контакты', 'Contact'),
    'footer_social': ('Ijtimoiy tarmoqlar', 'Соцсети', 'Social'),
    'footer_personal': ('Telegram (shaxsiy)', 'Telegram (личный)', 'Telegram (personal)'),
    'footer_group': ('Telegram guruh', 'Telegram-группа', 'Telegram group'),
    'about_links_title': (
        "Rezyume va kod",
        "Резюме и код",
        "Résumé & code",
    ),
    'cta_label_phone': ('Qo\'ng\'iroq qiling', 'Позвоните', 'Call me'),
    'cta_label_telegram': ('Telegramda yozing', 'Напишите в Telegram', 'Message on Telegram'),
    'cta_label_instagram': ('Instagram', 'Instagram', 'Instagram'),
    'cta_label_email': ('Email yuboring', 'Напишите на email', 'Send an email'),
    'present': ('hozirgacha', 'по настоящее время', 'present'),
    'lightbox_close': ('Yopish', 'Закрыть', 'Close'),
    'lightbox_prev': ('Oldingi rasm', 'Предыдущее фото', 'Previous image'),
    'lightbox_next': ('Keyingi rasm', 'Следующее фото', 'Next image'),
    'skills_title': ("Ko'nikmalar", 'Навыки', 'Skills'),
    'skills_soft_label': (
        "Shaxsiy ko'nikmalar:",
        "Гибкие навыки:",
        "Soft skills:",
    ),
    'skills_soft_value': (
        "Muloqot · Jamoada ishlash · Muammolarni hal etish · Vaqtni boshqarish",
        "Коммуникация · Работа в команде · Решение проблем · Тайм-менеджмент",
        "Communication · Teamwork · Problem-solving · Time management",
    ),
    'services_title': ('Xizmatlar', 'Услуги', 'Services'),
    'services_desc': (
        "Telegram botlar, veb-saytlar, AI integratsiya va talabalar uchun loyihalar. Xizmat narxi loyihaning hajmi va murakkabligiga qarab belgilanadi.",
        "Telegram-боты, сайты, AI-интеграция и проекты для студентов. Стоимость определяется объёмом и сложностью проекта.",
        "Telegram bots, websites, AI integration and student projects. Pricing depends on the scope and complexity of the project.",
    ),
    'group_title': ('IT VA AI XIZMATLAR guruhi', 'Группа «IT VA AI XIZMATLAR»', 'IT VA AI XIZMATLAR community'),
    'group_desc': (
        "Savol berish, buyurtma qoldirish va yangiliklarni kuzatib borish uchun Telegram guruhimizga qo'shiling.",
        "Присоединяйтесь к нашей Telegram-группе, чтобы задать вопрос, оставить заявку и следить за новостями.",
        "Join our Telegram group to ask questions, place an order and follow the news.",
    ),
    'group_btn': ("Guruhga qo'shilish", 'Вступить в группу', 'Join the group'),
    'experience_title': ("Tajriba va ta'lim", 'Опыт и образование', 'Experience & education'),
    'experience_projects': (
        "Bajarilgan loyihalar",
        "Выполненные проекты",
        "Delivered projects",
    ),
    'contact_headline_pre': (
        "Keling,",
        "Давайте",
        "Let's",
    ),
    'contact_headline_em': (
        "hamkorlik qilaylik",
        "сотрудничать",
        "work together",
    ),
    'contact_headline_post': ('.', '.', '.'),
    'contact_desc': (
        "Loyiha yoki hamkorlik bo'yicha takliflaringiz bo'lsa, murojaat qiling. Tez orada javob beraman.",
        "Если у вас есть предложение по проекту или сотрудничеству, свяжитесь со мной. Отвечу в ближайшее время.",
        "If you have a project or collaboration proposal, get in touch. I will reply shortly.",
    ),
    'footer_rights': ('Barcha huquqlar himoyalangan', 'Все права защищены', 'All rights reserved'),
    'meta_desc': (
        "Dostonbek Suyunov — Fullstack dasturchi (Python, Django, Next.js, TypeScript). Telegram botlar, veb-saytlar va AI integratsiya.",
        "Достонбек Суюнов — Fullstack-разработчик (Python, Django, Next.js, TypeScript). Telegram-боты, сайты и AI-интеграция.",
        "Dostonbek Suyunov — Fullstack Developer (Python, Django, Next.js, TypeScript). Telegram bots, websites and AI integration.",
    ),
    'projects_meta_desc': (
        "Dostonbek Suyunov loyihalari: Lumarc'da bajarilgan ishlar, Telegram botlar, veb-saytlar va AI loyihalari.",
        "Проекты Достонбека Суюнова: работы в Lumarc, Telegram-боты, сайты и AI-проекты.",
        "Dostonbek Suyunov's projects: work at Lumarc, Telegram bots, websites and AI projects.",
    ),
    'e404_title': ('Sahifa topilmadi', 'Страница не найдена', 'Page not found'),
    'e404_text': (
        "Siz izlagan sahifa mavjud emas yoki boshqa manzilga ko'chirilgan.",
        "Запрошенная страница не существует или была перемещена.",
        "The page you are looking for does not exist or has been moved.",
    ),
    'e500_title': ('Serverda xatolik', 'Ошибка сервера', 'Server error'),
    'e500_text': (
        "Xatolik yuz berdi. Iltimos, birozdan so'ng qayta urinib ko'ring.",
        "Произошла ошибка. Пожалуйста, повторите попытку чуть позже.",
        "An error occurred. Please try again in a moment.",
    ),
    'back_home': ('Bosh sahifaga qaytish', 'На главную', 'Back to home'),
}

TEXT = {
    lang: {key: values[i] for key, values in _STRINGS.items()}
    for i, lang in enumerate(LANGUAGES)
}


# --- Yangilangan lotin imlosi (oʻ, gʻ va tutuq belgisi): barcha o'zbekcha matnga qo'llanadi
from .orthography import uz_latin, uz_latin_deep  # noqa: E402

TEXT['uz'] = uz_latin_deep(TEXT['uz'])
SKILL_CATEGORY_LABELS['uz'] = uz_latin_deep(SKILL_CATEGORY_LABELS['uz'])
for _service in SERVICES:
    _service['title']['uz'] = uz_latin(_service['title']['uz'])
    _service['desc']['uz'] = uz_latin(_service['desc']['uz'])
for _item in TIMELINE:
    for _key in ('title', 'org', 'period', 'desc'):
        _item[_key]['uz'] = uz_latin(_item[_key]['uz'])
