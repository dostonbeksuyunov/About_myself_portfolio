from urllib.parse import urlencode

from django.conf import settings

from .content import CONTACT, LANGUAGES, TEXT

DEFAULT_LANGUAGE = 'uz'


def resolve_language(request):
    """?lang= > sessiya > standart. Tanlov sessiyada saqlanadi."""
    lang = request.GET.get('lang')
    if lang in LANGUAGES:
        if hasattr(request, 'session'):
            request.session['lang'] = lang
        return lang
    if hasattr(request, 'session'):
        saved = request.session.get('lang')
        if saved in LANGUAGES:
            return saved
    return DEFAULT_LANGUAGE


def _url_with(request, lang):
    params = request.GET.copy()
    params['lang'] = lang
    return f'{request.path}?{urlencode(params, doseq=True)}'


def site(request):
    lang = resolve_language(request)
    base = settings.SITE_URL
    return {
        'current_lang': lang,
        't': TEXT[lang],
        'contact': CONTACT,
        'site_url': base,
        'lang_urls': {code: _url_with(request, code) for code in LANGUAGES},
        'canonical_url': f'{base}{request.path}?lang={lang}',
        'alternates': [(code, f'{base}{request.path}?lang={code}') for code in LANGUAGES],
        'x_default_url': f'{base}{request.path}?lang={DEFAULT_LANGUAGE}',
        'og_locale': {'uz': 'uz_UZ', 'ru': 'ru_RU', 'en': 'en_US'}[lang],
    }
