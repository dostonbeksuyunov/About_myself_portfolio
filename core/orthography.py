"""O'zbek tilidagi matnlarni yangilangan lotin imlosiga keltirish.

Yangilangan lotin alifbosida:
  * oʻ va gʻ harflari "oʻ" (U+02BB) belgisi bilan yoziladi: oʻzbek, gʻoya, toʻlov;
  * tutuq belgisi "ʼ" (U+02BC) bilan yoziladi: maʼlumot, taʼlim, sunʼiy.

Manba matnlarni oddiy klaviaturada (') bilan yozish mumkin, chiqishda avtomatik almashtiriladi.
Funksiya idempotent: allaqachon yangi imlodagi matnga tegmaydi.
"""
import re

OKG = 'ʻ'      # ʻ — oʻ, gʻ
TUTUQ = 'ʼ'    # ʼ — tutuq belgisi

# Barcha turdagi apostrof va tirnoqlarni bitta ko'rinishga keltirish uchun
_VARIANTS = re.compile("[‘’ʻʼ`´]")
# o' / g' (harfdan oldin) -> ʻ. Django kabi xorijiy nomlar qo'shimchasi bundan mustasno.
_OKG = re.compile(r"(?<!Django)(?<=[oOgG])'(?=[A-Za-z])")


def uz_latin(text):
    if not text:
        return text
    text = _VARIANTS.sub("'", text)
    text = _OKG.sub(OKG, text)
    return text.replace("'", TUTUQ)


def uz_latin_deep(value):
    """str, list, tuple va dict ichidagi barcha matnlarga qo'llaydi."""
    if isinstance(value, str):
        return uz_latin(value)
    if isinstance(value, dict):
        return {k: uz_latin_deep(v) for k, v in value.items()}
    if isinstance(value, list):
        return [uz_latin_deep(v) for v in value]
    if isinstance(value, tuple):
        return tuple(uz_latin_deep(v) for v in value)
    return value
