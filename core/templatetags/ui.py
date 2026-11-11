from django import template

register = template.Library()


@register.simple_tag
def ui(t, prefix, key):
    """UI matnini prefiks + kalit bo'yicha olish: {% ui t "kind_" project.kind %}"""
    return t.get(f'{prefix}{key}', key)


@register.simple_tag
def project_period(project_year, ongoing, present, year_end=None):
    if ongoing:
        return f'{project_year} — {present}'
    if year_end and year_end != project_year:
        return f'{project_year} — {year_end}'
    return str(project_year)
