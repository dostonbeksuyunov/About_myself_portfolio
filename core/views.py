from django.shortcuts import render

SKILLS = {
    'core': ['Python', 'SQL', 'Django', 'Django REST Framework', 'FastAPI'],
    'data': ['PostgreSQL', 'SQLite', 'Redis'],
    'practices': ['Celery & Celery Beat', 'Django Channels (WebSockets)', 'JWT Authentication', 'REST API Design'],
    'tools': ['Docker', 'Docker Compose', 'Git & GitHub', 'Postman', 'Linux', 'CI/CD'],
}

SKILL_CATEGORY_LABELS = {
    'uz': {'core': 'Tillar va freymvorklar', 'data': "Ma'lumotlar bazasi va keshlash", 'practices': 'Backend amaliyotlari', 'tools': 'Vositalar va DevOps'},
    'ru': {'core': 'Языки и фреймворки', 'data': 'Базы данных и кэширование', 'practices': 'Backend-практики', 'tools': 'Инструменты и DevOps'},
    'en': {'core': 'Languages & Frameworks', 'data': 'Databases & Caching', 'practices': 'Backend Practices', 'tools': 'Tools & DevOps'},
}

PROJECTS = [
    {
        'method': 'GET', 'endpoint': '/api/books',
        'name': 'Online Book Store',
        'stack': ['Python', 'Django', 'DRF', 'PostgreSQL'],
        'description': {
            'uz': "Onlayn kitob do'koni uchun backend API — Django REST Framework yordamida kitoblar katalogi uchun asosiy CRUD amallari (yaratish, o'qish, yangilash, o'chirish) amalga oshirilgan, PostgreSQL sxemasi bilan.",
            'ru': "Backend API для онлайн-магазина книг — реализованы основные CRUD-операции (создание, чтение, обновление, удаление) для каталога книг с помощью Django REST Framework и схемы PostgreSQL.",
            'en': "Backend API for an online book store — implemented core CRUD operations (create, read, update, delete) for the book catalog using Django REST Framework, with a PostgreSQL schema.",
        },
    },
    {
        'method': 'POST', 'endpoint': '/api/tickets',
        'name': 'Buy a Ticket Bot',
        'stack': ['Python', 'python-telegram-bot', 'Django Admin', 'Click/Payme'],
        'description': {
            'uz': "Telegram orqali tadbir chiptalarini sotish tizimi — speaker/mavzu tanlash, joy band qilish, Click/Payme orqali to'lov va QR-kodli chipta.",
            'ru': "Система продажи билетов на мероприятия через Telegram — выбор спикера/темы, бронирование места, оплата через Click/Payme и билет с QR-кодом.",
            'en': "Telegram-based event ticket sales system — choose a speaker/topic, reserve a seat, pay via Click/Payme, and get a QR-coded ticket.",
        },
    },
    {
        'method': 'GET', 'endpoint': '/api/gym',
        'name': 'Gym Management Bot',
        'stack': ['Python', 'python-telegram-bot', 'Django Admin'],
        'description': {
            'uz': "Sportzal a'zolari uchun Telegram bot — jadval ko'rish, mashqlarni kuzatish, obunani boshqarish.",
            'ru': "Telegram-бот для участников тренажёрного зала — просмотр расписания, отслеживание тренировок, управление абонементом.",
            'en': "Telegram bot for gym members — view schedules, track workouts, and manage subscriptions.",
        },
    },
    {
        'method': 'GET', 'endpoint': '/api/lessons',
        'name': 'Language Learning Bot',
        'stack': ['Python', 'python-telegram-bot', 'Django Admin'],
        'description': {
            'uz': "Lug'at va grammatikani interaktiv viktorina orqali mashq qildiruvchi Telegram bot, har bir foydalanuvchi progressi kuzatiladi.",
            'ru': "Telegram-бот для практики словарного запаса и грамматики через интерактивные квизы, с отслеживанием прогресса каждого пользователя.",
            'en': "Telegram bot for practicing vocabulary and grammar through interactive quizzes, with per-user progress tracking.",
        },
    },
]

TIMELINE = [
    {
        'title': 'Python Backend Development Program',
        'org': 'Ustudy Academy, IT Park Uzbekistan',
        'period': {'uz': '2025-sentyabr — 2026-sentyabr', 'ru': 'сентябрь 2025 — сентябрь 2026', 'en': 'September 2025 – September 2026'},
        'desc': {
            'uz': "Python, PostgreSQL, Django/DRF, Celery/Channels, Docker/CI-CD bo'yicha 12-modulli intensiv kurs.",
            'ru': "Интенсивный курс из 12 модулей: Python, PostgreSQL, Django/DRF, Celery/Channels, Docker/CI-CD.",
            'en': "Intensive 12-module course covering Python, PostgreSQL, Django/DRF, Celery/Channels, and Docker/CI-CD.",
        },
    },
    {
        'title': 'Meta Back-End Developer Professional Certificate',
        'org': 'Coursera (Meta)',
        'period': {'uz': '2025-iyun', 'ru': 'июнь 2025', 'en': 'June 2025'},
        'desc': {
            'uz': "Python, Django, REST API va bazalar bo'yicha 9 kurslik dastur.",
            'ru': "Программа из 9 курсов по Python, Django, REST API и базам данных.",
            'en': "A 9-course program covering Python, Django, REST APIs, and databases.",
        },
    },
    {
        'title': 'Prompt Engineering for AI Systems',
        'org': "Five Million AI Leaders (O'zbekiston & BAA)",
        'period': {'uz': '2026-mart', 'ru': 'март 2026', 'en': 'March 2026'},
        'desc': {'uz': '', 'ru': '', 'en': ''},
    },
    {
        'title': {'uz': 'Computer Science and Programming Technologies — Bakalavr', 'ru': 'Computer Science and Programming Technologies — бакалавр', 'en': "Computer Science and Programming Technologies — Bachelor's Degree"},
        'org': {'uz': "O'zbekiston Milliy Universiteti", 'ru': 'Национальный университет Узбекистана', 'en': 'National University of Uzbekistan'},
        'period': {'uz': '2022 — 2026', 'ru': '2022 — 2026', 'en': '2022 — 2026'},
        'desc': {'uz': '', 'ru': '', 'en': ''},
    },
]

TEXT = {
    'uz': {
        'initials': 'DS.',
        'name_first': 'Dostonbek',
        'name_last': 'Suyunov',
        'badge_location': "TOSHKENT, O'ZBEKISTON",
        'hero_role': 'Python Backend dasturchi',
        'hero_tagline': "Django va DRF bilan ishonchli, tez va toza REST API'lar quraman.",
        'btn_projects': "Loyihalarni ko'rish",
        'btn_contact': "Bog'lanish",
        'btn_hire': "Menga yozing",
        'scroll_label': 'PASTGA',
        'nav': {'about': 'Men haqimda', 'skills': "Ko'nikmalar", 'projects': 'Loyihalar', 'experience': 'Tajriba'},
        'about_title': 'Men haqimda',
        'about_text': "Computer Science yo'nalishi bo'yicha bakalavriatni tugatgan, backend rivojlantirishga chuqur qiziqqan dasturchiman. IT Park O'zbekiston qoshidagi Ustudy Academy'da intensiv Python Backend Development dasturini tugatdim — Django, DRF, FastAPI, PostgreSQL, Redis va Docker bilan chuqur ishladim. Meta'ning Back-End Developer sertifikatiga ham egaman.",
        'edu_label': "Ta'lim",
        'edu_degree': 'Computer Science and Programming Technologies — Bakalavr',
        'edu_org': "O'zbekiston Milliy Universiteti · 2022–2026",
        'skills_title': "Ko'nikmalar",
        'skills_soft_label': 'Soft skills:',
        'skills_soft_value': 'Muloqot · Jamoada ishlash · Muammolarni yechish · Vaqtni boshqarish',
        'projects_title': 'Loyihalar',
        'experience_title': 'Tayyorgarlik va sertifikatlar',
        'contact_headline_pre': 'Kelinglar, birga',
        'contact_headline_em': 'quraylik',
        'contact_headline_post': '.',
        'contact_desc': "Loyiha yoki hamkorlik bo'yicha taklif bormi? Yozib qoling — albatta javob beraman.",
    },
    'ru': {
        'initials': 'ДС.',
        'name_first': 'Достонбек',
        'name_last': 'Суюнов',
        'badge_location': "ТАШКЕНТ, УЗБЕКИСТАН",
        'hero_role': 'Python Backend-разработчик',
        'hero_tagline': "Создаю надёжные, быстрые и чистые REST API с помощью Django и DRF.",
        'btn_projects': "Смотреть проекты",
        'btn_contact': "Связаться",
        'btn_hire': "Написать мне",
        'scroll_label': 'ВНИЗ',
        'nav': {'about': 'Обо мне', 'skills': 'Навыки', 'projects': 'Проекты', 'experience': 'Опыт'},
        'about_title': 'Обо мне',
        'about_text': "Я дипломированный специалист по направлению Computer Science, глубоко увлечён backend-разработкой. Прошёл интенсивную программу Python Backend Development в Ustudy Academy при IT Park Uzbekistan — на практике освоил Django, DRF, FastAPI, PostgreSQL, Redis и Docker. Также имею сертификат Meta Back-End Developer.",
        'edu_label': 'Образование',
        'edu_degree': 'Computer Science and Programming Technologies — бакалавр',
        'edu_org': 'Национальный университет Узбекистана · 2022–2026',
        'skills_title': 'Навыки',
        'skills_soft_label': 'Гибкие навыки:',
        'skills_soft_value': 'Коммуникация · Работа в команде · Решение проблем · Тайм-менеджмент',
        'projects_title': 'Проекты',
        'experience_title': 'Обучение и сертификаты',
        'contact_headline_pre': 'Давайте создадим что-то',
        'contact_headline_em': 'вместе',
        'contact_headline_post': '.',
        'contact_desc': "Есть предложение по проекту или сотрудничеству? Напишите — обязательно отвечу.",
    },
    'en': {
        'initials': 'DS.',
        'name_first': 'Dostonbek',
        'name_last': 'Suyunov',
        'badge_location': "TASHKENT, UZBEKISTAN",
        'hero_role': 'Python Backend Developer',
        'hero_tagline': "I build reliable, fast, and clean REST APIs with Django and DRF.",
        'btn_projects': 'View projects',
        'btn_contact': 'Contact',
        'btn_hire': 'Message me',
        'scroll_label': 'SCROLL',
        'nav': {'about': 'About', 'skills': 'Skills', 'projects': 'Projects', 'experience': 'Experience'},
        'about_title': 'About me',
        'about_text': "I hold a Bachelor's degree in Computer Science, with a deep interest in backend development. I completed the intensive Python Backend Development program at Ustudy Academy, IT Park Uzbekistan — building hands-on experience with Django, DRF, FastAPI, PostgreSQL, Redis, and Docker. I also hold the Meta Back-End Developer certificate.",
        'edu_label': 'Education',
        'edu_degree': "Computer Science and Programming Technologies — Bachelor's Degree",
        'edu_org': 'National University of Uzbekistan · 2022–2026',
        'skills_title': 'Skills',
        'skills_soft_label': 'Soft skills:',
        'skills_soft_value': 'Communication · Teamwork · Problem-Solving · Time Management',
        'projects_title': 'Projects',
        'experience_title': 'Training & Certifications',
        'contact_headline_pre': "Let's build something",
        'contact_headline_em': 'together',
        'contact_headline_post': '.',
        'contact_desc': "Got a project or collaboration in mind? Reach out — I'll get back to you.",
    },
}


def home(request):
    lang = request.GET.get('lang')
    if lang not in ('uz', 'ru', 'en'):
        lang = request.session.get('lang', 'uz')
    else:
        request.session['lang'] = lang

    projects = [
        {
            'method': p['method'],
            'endpoint': p['endpoint'],
            'name': p['name'],
            'stack': p['stack'],
            'description': p['description'][lang],
        }
        for p in PROJECTS
    ]

    timeline = [
        {
            'title': t['title'] if isinstance(t['title'], str) else t['title'][lang],
            'org': t['org'] if isinstance(t['org'], str) else t['org'][lang],
            'period': t['period'][lang],
            'desc': t['desc'][lang],
        }
        for t in TIMELINE
    ]

    skills = {
        SKILL_CATEGORY_LABELS[lang][key]: items
        for key, items in SKILLS.items()
    }

    all_skills = [item for items in SKILLS.values() for item in items]

    context = {
        'current_lang': lang,
        't': TEXT[lang],
        'skills': skills,
        'all_skills': all_skills,
        'projects': projects,
        'timeline': timeline,
    }
    return render(request, 'core/home.html', context)
