import json
from datetime import date

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.templatetags.static import static
from django.utils.safestring import mark_safe

from .content import (
    CONTACT,
    LANGUAGES,
    SERVICES,
    SKILL_CATEGORY_LABELS,
    SKILLS,
    TEXT,
    TIMELINE,
)
from .context_processors import resolve_language
from .models import Project

CATEGORY_KEYS = [key for key, _ in Project.CATEGORIES]
KIND_KEYS = [key for key, _ in Project.Kind.choices]
EXPERIENCE_SINCE = 2025  # Ustudy dasturi boshlangan yil


def _abs_static(path):
    return f'{settings.SITE_URL}{static(path)}'


def _jsonld(data):
    # <script> ichida xavfsiz bo'lishi uchun '<' ni escape qilamiz
    return mark_safe(json.dumps(data, ensure_ascii=False).replace('<', '\\u003c'))


def _card(project, lang):
    return {
        'obj': project,
        'slug': project.slug,
        'title': project.title,
        'short': project.text('short', lang),
        'role': project.text('role', lang),
        'kind': project.kind,
        'status': project.status,
        'cover': project.cover,
        'stack': project.stack_list[:5],
        'categories': project.category_list,
        'year': project.year_start,
        'ongoing': project.ongoing,
    }


def home(request):
    lang = resolve_language(request)
    published = Project.objects.filter(is_published=True)
    work = [_card(p, lang) for p in published.filter(kind=Project.Kind.WORK)]
    others = [
        _card(p, lang)
        for p in published.filter(is_featured=True).exclude(kind__in=[Project.Kind.WORK, Project.Kind.LEARNING])
    ]

    timeline = []
    for item in TIMELINE:
        timeline.append({
            'kind': item['kind'],
            'title': item['title'][lang],
            'org': item['org'][lang],
            'period': item['period'][lang],
            'desc': item['desc'][lang],
            'projects': work if item.get('with_projects') else [],
        })

    all_skills = [s for items in SKILLS.values() for s in items]
    stats = {
        'projects': published.count(),
        'live': published.filter(status=Project.Status.LIVE).exclude(kind=Project.Kind.LEARNING).count(),
        'tech': len(all_skills),
        'years': max(date.today().year - EXPERIENCE_SINCE, 1),
    }

    skills = {SKILL_CATEGORY_LABELS[lang][key]: items for key, items in SKILLS.items()}
    services = [{'icon': s['icon'], 'title': s['title'][lang], 'desc': s['desc'][lang]} for s in SERVICES]

    t = TEXT[lang]
    person = {
        '@context': 'https://schema.org',
        '@type': 'Person',
        'name': f"{t['name_first']} {t['name_last']}",
        'jobTitle': t['hero_role'],
        'url': settings.SITE_URL + '/',
        'email': CONTACT['email'],
        'telephone': CONTACT['phone'],
        'sameAs': [CONTACT['github'], CONTACT['linkedin'], CONTACT['telegram']],
        'alumniOf': 'National University of Uzbekistan',
        'worksFor': {'@type': 'Organization', 'name': 'Lumarc'},
        'knowsAbout': ['Python', 'Django', 'TypeScript', 'Next.js', 'React', 'NestJS', 'PostgreSQL'],
    }

    return render(request, 'core/home.html', {
        'page_title': f"{t['name_first']} {t['name_last']} — {t['hero_role']}",
        'meta_description': t['meta_desc'],
        'og_image': _abs_static('core/og-default.jpg'),
        'jsonld': _jsonld(person),
        'work_projects': work,
        'other_projects': others,
        'timeline': timeline,
        'skills': skills,
        'all_skills': all_skills,
        'services': services,
        'stats': stats,
    })


def project_list(request):
    lang = resolve_language(request)
    kind = request.GET.get('kind', '')
    cat = request.GET.get('cat', '')
    kind = kind if kind in KIND_KEYS else ''
    cat = cat if cat in CATEGORY_KEYS else ''

    projects = Project.objects.filter(is_published=True)
    if kind:
        projects = projects.filter(kind=kind)
    if cat:
        projects = [p for p in projects if cat in p.category_list]
    else:
        projects = list(projects)

    main = [_card(p, lang) for p in projects if p.kind != Project.Kind.LEARNING]
    learning = [_card(p, lang) for p in projects if p.kind == Project.Kind.LEARNING]

    t = TEXT[lang]
    return render(request, 'core/project_list.html', {
        'page_title': f"{t['projects_title']} — {t['name_first']} {t['name_last']}",
        'meta_description': t['projects_meta_desc'],
        'og_image': _abs_static('core/og-default.jpg'),
        'main_projects': main,
        'learning_projects': learning,
        'kind': kind,
        'cat': cat,
        'kinds': Project.Kind.values,
        'categories': CATEGORY_KEYS,
        'total': len(main) + len(learning),
        'canonical_override': f'{settings.SITE_URL}{request.path}?lang={lang}',
    })


def project_detail(request, slug):
    lang = resolve_language(request)
    project = get_object_or_404(Project, slug=slug, is_published=True)
    siblings = list(Project.objects.filter(is_published=True).values_list('slug', 'title'))
    index = next((i for i, (s, _) in enumerate(siblings) if s == slug), None)
    prev_p = siblings[index - 1] if index not in (None, 0) else None
    next_p = siblings[index + 1] if index is not None and index + 1 < len(siblings) else None

    t = TEXT[lang]
    short = project.text('short', lang)
    og_path = project.og_image
    jsonld = {
        '@context': 'https://schema.org',
        '@type': 'SoftwareApplication' if project.kind != Project.Kind.LEARNING else 'CreativeWork',
        'name': project.title,
        'description': short,
        'dateCreated': str(project.year_start),
        'inLanguage': lang,
        'author': {'@type': 'Person', 'name': f"{t['name_first']} {t['name_last']}"},
        'keywords': ', '.join(project.stack_list),
    }
    if project.kind != Project.Kind.LEARNING:
        jsonld['applicationCategory'] = 'WebApplication'
    if project.show_links and project.live_url:
        jsonld['url'] = project.live_url

    return render(request, 'core/project_detail.html', {
        'project': project,
        'role': project.text('role', lang),
        'short': short,
        'problem': project.text('problem', lang),
        'solution': project.text('solution', lang),
        'result': project.text('result', lang),
        'highlights': project.lines('highlights', lang),
        'gallery': project.gallery_list if project.show_links else [],
        'categories': project.category_list,
        'stack': project.stack_list,
        'prev_project': prev_p,
        'next_project': next_p,
        'page_title': f"{project.title} — {t['name_first']} {t['name_last']}",
        'meta_description': short,
        'og_image': _abs_static(og_path),
        'og_type': 'article',
        'jsonld': _jsonld(jsonld),
    })


def robots_txt(request):
    body = (
        'User-agent: *\n'
        'Disallow: /admin/\n'
        f'Sitemap: {settings.SITE_URL}/sitemap.xml\n'
    )
    return HttpResponse(body, content_type='text/plain; charset=utf-8')


def sitemap_xml(request):
    base = settings.SITE_URL
    paths = ['/', '/projects/'] + [
        f'/projects/{slug}/'
        for slug in Project.objects.filter(is_published=True).values_list('slug', flat=True)
    ]
    entries = []
    for path in paths:
        for lang in LANGUAGES:
            loc = f'{base}{path}?lang={lang}'.replace('&', '&amp;')
            entries.append(f'  <url><loc>{loc}</loc></url>')
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + '\n'.join(entries) + '\n</urlset>\n'
    )
    return HttpResponse(xml, content_type='application/xml; charset=utf-8')


def _error_context(request, key):
    lang = resolve_language(request)
    t = TEXT[lang]
    return {
        'page_title': f"{t[key + '_title']} — {t['name_first']} {t['name_last']}",
        'meta_description': t[key + '_text'],
        'og_image': _abs_static('core/og-default.jpg'),
    }


def page_not_found(request, exception=None):
    return render(request, '404.html', _error_context(request, 'e404'), status=404)


def server_error(request):
    try:
        return render(request, '500.html', _error_context(request, 'e500'), status=500)
    except Exception:  # shablon yoki kontekst ham sinsa — eng oddiy javob
        return HttpResponse('Server error', status=500, content_type='text/plain')
