from django.db import models

from .orthography import uz_latin

LANGS = ('uz', 'ru', 'en')


class Project(models.Model):
    class Kind(models.TextChoices):
        WORK = 'work', 'Ish (Lumarc)'
        CLIENT = 'client', 'Mijoz'
        PERSONAL = 'personal', 'Shaxsiy'
        LEARNING = 'learning', "O'quv"

    class Status(models.TextChoices):
        LIVE = 'live', 'Live'
        IN_DEVELOPMENT = 'in_development', 'Ishlab chiqilmoqda'
        ARCHIVED = 'archived', 'Arxiv'
        CONCEPT = 'concept', 'Konsept'

    CATEGORIES = (
        ('web', 'Web'),
        ('bot', 'Bot'),
        ('ai', 'AI'),
        ('backend', 'Backend'),
        ('3d', '3D'),
        ('automation', 'Avtomatlashtirish'),
    )

    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(default=100, help_text="Kichik raqam — yuqorida")
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    kind = models.CharField(max_length=10, choices=Kind.choices, default=Kind.PERSONAL)
    categories = models.CharField(
        max_length=80, blank=True,
        help_text="Vergul bilan: web, bot, ai, backend, 3d, automation",
    )
    year_start = models.PositiveSmallIntegerField()
    year_end = models.PositiveSmallIntegerField(null=True, blank=True)
    ongoing = models.BooleanField(default=False)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.LIVE)
    confidential = models.BooleanField(
        default=False,
        help_text="Belgilansa havolalar va ichki skrinshotlar ko'rsatilmaydi",
    )

    title = models.CharField(max_length=120)
    role_uz = models.CharField(max_length=160, blank=True)
    role_ru = models.CharField(max_length=160, blank=True)
    role_en = models.CharField(max_length=160, blank=True)
    short_uz = models.TextField()
    short_ru = models.TextField()
    short_en = models.TextField()
    problem_uz = models.TextField(blank=True)
    problem_ru = models.TextField(blank=True)
    problem_en = models.TextField(blank=True)
    solution_uz = models.TextField(blank=True)
    solution_ru = models.TextField(blank=True)
    solution_en = models.TextField(blank=True)
    result_uz = models.TextField(blank=True)
    result_ru = models.TextField(blank=True)
    result_en = models.TextField(blank=True)
    highlights_uz = models.TextField(blank=True, help_text="Har qator — bitta band")
    highlights_ru = models.TextField(blank=True, help_text="Har qator — bitta band")
    highlights_en = models.TextField(blank=True, help_text="Har qator — bitta band")

    stack = models.CharField(max_length=300, blank=True, help_text="Vergul bilan")
    live_url = models.URLField(blank=True)
    telegram_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)

    cover = models.CharField(
        max_length=200, blank=True,
        help_text="Static yo'l, masalan core/projects/<slug>/cover.webp",
    )
    gallery = models.TextField(blank=True, help_text="Har qatorda bitta static yo'l")

    class Meta:
        ordering = ('order', 'id')

    def __str__(self):
        return self.title

    def text(self, field, lang):
        value = getattr(self, f'{field}_{lang}', '')
        if lang != 'uz' and value:
            return value
        # o'zbekcha matn (yoki boshqa tilda bo'sh bo'lsa, shunga qaytish) yangi lotin imlosida chiqariladi
        return uz_latin(value or getattr(self, f'{field}_uz', ''))

    def lines(self, field, lang):
        return [ln.strip() for ln in self.text(field, lang).splitlines() if ln.strip()]

    @staticmethod
    def _split(value):
        return [part.strip() for part in value.split(',') if part.strip()]

    @property
    def category_list(self):
        return self._split(self.categories)

    @property
    def stack_list(self):
        return self._split(self.stack)

    @property
    def gallery_list(self):
        return [ln.strip() for ln in self.gallery.splitlines() if ln.strip()]

    @property
    def cover_small(self):
        return self.cover.replace('cover.webp', 'cover-800.webp')

    @property
    def og_image(self):
        return f'core/projects/{self.slug}/og.jpg'

    @property
    def code_is_closed(self):
        return self.kind != self.Kind.LEARNING and not self.github_url

    @property
    def show_links(self):
        return not self.confidential
