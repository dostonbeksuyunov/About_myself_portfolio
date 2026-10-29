from django.shortcuts import render

from .content import (
    CONTACT,
    PROJECTS,
    SERVICES,
    SKILLS,
    SKILL_CATEGORY_LABELS,
    TEXT,
    TIMELINE,
)

LANGUAGES = tuple(TEXT)
DEFAULT_LANGUAGE = 'uz'


def home(request):
    lang = request.GET.get('lang')
    if lang not in LANGUAGES:
        lang = request.session.get('lang', DEFAULT_LANGUAGE)
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

    services = [
        {'icon': s['icon'], 'title': s['title'][lang], 'desc': s['desc'][lang]}
        for s in SERVICES
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
        'services': services,
        'contact': CONTACT,
        'timeline': timeline,
    }
    return render(request, 'core/home.html', context)
