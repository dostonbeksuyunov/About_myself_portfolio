from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Project


class CategoryFilter(admin.SimpleListFilter):
    title = 'yo\'nalish'
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        return Project.CATEGORIES

    def queryset(self, request, queryset):
        value = self.value()
        if not value:
            return queryset
        return queryset.filter(categories__regex=rf'(^|,)\s*{value}\s*(,|$)')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'kind', 'status', 'is_featured', 'is_published', 'order', 'preview')
    list_editable = ('order', 'is_featured', 'is_published')
    list_filter = ('kind', CategoryFilter, 'status', 'is_featured', 'is_published')
    search_fields = ('title', 'slug', 'short_uz', 'stack')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'order', 'is_featured', 'is_published')}),
        ('Tasnif', {'fields': ('kind', 'categories', 'status', 'confidential',
                               'year_start', 'year_end', 'ongoing')}),
        ('Uz', {'fields': ('role_uz', 'short_uz', 'problem_uz', 'solution_uz', 'result_uz', 'highlights_uz')}),
        ('Ru', {'fields': ('role_ru', 'short_ru', 'problem_ru', 'solution_ru', 'result_ru', 'highlights_ru')}),
        ('En', {'fields': ('role_en', 'short_en', 'problem_en', 'solution_en', 'result_en', 'highlights_en')}),
        ('Texnologiya va havolalar', {'fields': ('stack', 'live_url', 'telegram_url', 'github_url')}),
        ('Media', {'fields': ('cover', 'gallery')}),
    )

    @admin.display(description='Sahifa')
    def preview(self, obj):
        return format_html('<a href="{}" target="_blank" rel="noopener">ochish ↗</a>',
                           reverse('project_detail', args=[obj.slug]))
