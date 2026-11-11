from pathlib import Path

from django.core.management import call_command
from django.test import TestCase, override_settings

from .models import Project

LANGS = ('uz', 'ru', 'en')

TEST_SETTINGS = dict(
    SECURE_SSL_REDIRECT=False,
    SITE_URL='https://example.test',
    STORAGES={
        'default': {'BACKEND': 'django.core.files.storage.FileSystemStorage'},
        'staticfiles': {'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage'},
    },
)


@override_settings(**TEST_SETTINGS)
class PortfolioTestCase(TestCase):
    fixtures = ['projects']


class HomeViewTests(PortfolioTestCase):
    def test_home_page_status_code(self):
        self.assertEqual(self.client.get('/').status_code, 200)

    def test_default_language_is_uzbek(self):
        self.assertEqual(self.client.get('/').context['current_lang'], 'uz')

    def test_language_switch_is_saved_in_session(self):
        self.assertEqual(self.client.get('/?lang=en').context['current_lang'], 'en')
        self.assertEqual(self.client.get('/').context['current_lang'], 'en')

    def test_invalid_language_falls_back_to_session_value(self):
        self.client.get('/?lang=ru')
        self.assertEqual(self.client.get('/?lang=xx').context['current_lang'], 'ru')

    def test_home_renders_in_every_language(self):
        for lang in LANGS:
            with self.subTest(lang=lang):
                response = self.client.get(f'/?lang={lang}')
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, f'<html lang="{lang}"')

    def test_role_is_fullstack(self):
        response = self.client.get('/?lang=en')
        self.assertContains(response, 'Fullstack Developer')
        self.assertNotContains(response, 'vibe coding')

    def test_empty_timeline_description_is_hidden(self):
        self.assertNotContains(self.client.get('/'), '<p class="timeline-desc"></p>')

    def test_work_projects_are_listed_under_current_job(self):
        response = self.client.get('/')
        self.assertContains(response, '2026-sentyabr — hozirgacha')
        for slug in ('lumarc-sayt', 'lumarcos', 'e-auksion-radar', 'lumarcode', 'akromind'):
            self.assertContains(response, f'/projects/{slug}/')

    def test_ustudy_program_is_marked_completed_not_ongoing(self):
        response = self.client.get('/?lang=en')
        self.assertContains(response, 'September 2025 – September 2026')
        self.assertContains(response, 'Completed.')

    def test_contract_details_are_not_published(self):
        body = self.client.get('/').content.decode().lower()
        for word in ('shartnoma', 'sinov muddati', 'part-time', 'full-time', 'probation'):
            self.assertNotIn(word, body)

    def test_stats_come_from_database(self):
        response = self.client.get('/')
        self.assertEqual(response.context['stats']['projects'], Project.objects.filter(is_published=True).count())

    def test_services_section_and_group_link_are_rendered(self):
        response = self.client.get('/')
        self.assertContains(response, 'id="services"')
        self.assertContains(response, 'https://t.me/IT_vs_AI_XIZMATLAR_Uz')

    def test_services_are_translated(self):
        self.assertContains(self.client.get('/?lang=en'), 'AI integration')

    def test_hire_menu_offers_personal_and_group_links(self):
        response = self.client.get('/')
        self.assertContains(response, 'id="hire-menu"')
        self.assertNotContains(response, 'TELEGRAM GROUP')

    def test_single_theme_toggle_with_two_themes(self):
        response = self.client.get('/')
        self.assertContains(response, 'id="theme-toggle"')
        self.assertContains(response, 'aria-pressed')
        self.assertNotContains(response, 'cosmic')

    def test_resume_is_downloadable(self):
        self.assertContains(self.client.get('/'), 'download="Dostonbek_Suyunov_CV.pdf"')


class SeoTests(PortfolioTestCase):
    def test_meta_tags_and_canonical(self):
        response = self.client.get('/?lang=ru')
        self.assertContains(response, '<meta name="description"')
        self.assertContains(response, 'rel="canonical" href="https://example.test/?lang=ru"')
        self.assertContains(response, 'hreflang="uz"')
        self.assertContains(response, 'hreflang="x-default"')
        self.assertContains(response, 'property="og:image"')
        self.assertContains(response, 'name="twitter:card"')

    def test_home_has_person_json_ld(self):
        self.assertContains(self.client.get('/'), '"@type": "Person"')

    def test_project_page_has_own_og_image_and_json_ld(self):
        response = self.client.get('/projects/lumarcos/')
        self.assertContains(response, 'projects/lumarcos/og.jpg')
        self.assertContains(response, 'SoftwareApplication')

    def test_robots_txt(self):
        response = self.client.get('/robots.txt')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sitemap: https://example.test/sitemap.xml')

    def test_sitemap_lists_all_languages_and_projects(self):
        response = self.client.get('/sitemap.xml')
        self.assertEqual(response['Content-Type'].split(';')[0], 'application/xml')
        for lang in LANGS:
            self.assertContains(response, f'https://example.test/projects/lumarcos/?lang={lang}')
        self.assertContains(response, 'https://example.test/projects/?lang=uz')

    def test_sitemap_skips_unpublished(self):
        Project.objects.filter(slug='saveclip').update(is_published=False)
        self.assertNotContains(self.client.get('/sitemap.xml'), '/projects/saveclip/')


class ProjectListTests(PortfolioTestCase):
    def test_list_renders_in_every_language(self):
        for lang in LANGS:
            with self.subTest(lang=lang):
                self.assertEqual(self.client.get(f'/projects/?lang={lang}').status_code, 200)

    def test_list_contains_all_published_non_learning_projects(self):
        response = self.client.get('/projects/')
        for project in Project.objects.exclude(kind='learning'):
            self.assertContains(response, f'/projects/{project.slug}/')

    def test_learning_block_and_filters_only_show_what_exists(self):
        response = self.client.get('/projects/')
        self.assertNotContains(response, 'learning-list')
        self.assertNotContains(response, 'kind=learning')
        self.assertNotContains(response, 'kind=client')
        self.assertContains(response, 'kind=work')
        self.assertContains(response, 'cat=automation')

    def test_learning_projects_still_render_in_separate_block_when_present(self):
        Project.objects.filter(slug='moneyflow').update(kind='learning')
        response = self.client.get('/projects/')
        self.assertContains(response, 'learning-list')
        self.assertContains(response, 'kind=learning')

    def test_kind_filter(self):
        response = self.client.get('/projects/?kind=work')
        self.assertContains(response, '/projects/lumarcos/')
        self.assertNotContains(response, '/projects/moneyflow/')

    def test_category_filter(self):
        response = self.client.get('/projects/?cat=ai')
        self.assertContains(response, '/projects/lumarcos/')
        self.assertNotContains(response, '/projects/moneyflow/')

    def test_combined_filter(self):
        response = self.client.get('/projects/?kind=work&cat=bot')
        self.assertContains(response, '/projects/e-auksion-radar/')
        self.assertNotContains(response, '/projects/lumarcos/')

    def test_unknown_filter_values_are_ignored(self):
        response = self.client.get('/projects/?kind=hack&cat=zzz')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '/projects/lumarcos/')

    def test_filter_without_matches_shows_message(self):
        response = self.client.get('/projects/?kind=learning&cat=3d')
        self.assertContains(response, 'class="empty"')

    def test_unpublished_project_is_hidden(self):
        Project.objects.filter(slug='moneyflow').update(is_published=False)
        self.assertNotContains(self.client.get('/projects/'), '/projects/moneyflow/')
        self.assertNotContains(self.client.get('/'), '/projects/moneyflow/')


class ProjectDetailTests(PortfolioTestCase):
    def test_every_published_slug_renders_in_three_languages(self):
        for project in Project.objects.filter(is_published=True):
            for lang in LANGS:
                with self.subTest(slug=project.slug, lang=lang):
                    response = self.client.get(f'/projects/{project.slug}/?lang={lang}')
                    self.assertEqual(response.status_code, 200)
                    self.assertContains(response, project.title)

    def test_unknown_slug_is_404(self):
        self.assertEqual(self.client.get('/projects/yoq-loyiha/').status_code, 404)

    def test_unpublished_slug_is_404(self):
        Project.objects.filter(slug='saveclip').update(is_published=False)
        self.assertEqual(self.client.get('/projects/saveclip/').status_code, 404)

    def test_case_study_sections_are_translated(self):
        self.assertContains(self.client.get('/projects/lumarcos/?lang=en'), 'Problem')
        self.assertContains(self.client.get('/projects/lumarcos/?lang=ru'), 'Проблема')
        self.assertContains(self.client.get('/projects/lumarcos/?lang=uz'), 'Muammo')

    def test_links_are_shown_for_normal_project(self):
        response = self.client.get('/projects/saveclip/')
        self.assertContains(response, 'https://t.me/saveclipuz_bot')
        self.assertContains(response, 'rel="noopener noreferrer"')

    def test_confidential_project_hides_links_and_gallery(self):
        Project.objects.filter(slug='lumarcos').update(confidential=True)
        response = self.client.get('/projects/lumarcos/')
        self.assertNotContains(response, 'https://lumarcos.uz')
        self.assertNotContains(response, 'data-lightbox')
        self.assertContains(response, 'NDA')

    def test_no_github_links_on_project_pages(self):
        for project in Project.objects.all():
            page = self.client.get(f'/projects/{project.slug}/').content.decode()
            self.assertNotIn('github.com/dostonbeksuyunov/', page)
            self.assertIn('Kod yopiq', page)

    def test_prev_next_navigation(self):
        self.assertContains(self.client.get('/projects/lumarcos/'), 'case-nav-next')

    def test_ongoing_project_shows_present(self):
        self.assertContains(self.client.get('/projects/lumarcos/?lang=en'), '2026 — present')


class ErrorPageTests(PortfolioTestCase):
    def test_404_page_uses_site_template(self):
        response = self.client.get('/yoq-sahifa/')
        self.assertContains(response, 'Sahifa topilmadi', status_code=404)

    def test_404_is_translated(self):
        self.client.get('/?lang=en')
        self.assertContains(self.client.get('/yoq-sahifa/'), 'Page not found', status_code=404)


class FixtureTests(PortfolioTestCase):
    def test_fixture_is_idempotent(self):
        before = Project.objects.count()
        call_command('loaddata', 'projects', verbosity=0)
        self.assertEqual(Project.objects.count(), before)

    def test_every_project_has_all_three_languages(self):
        for project in Project.objects.all():
            for lang in LANGS:
                with self.subTest(slug=project.slug, lang=lang):
                    self.assertTrue(getattr(project, f'short_{lang}'))
                    self.assertTrue(project.lines('highlights', lang))

    def test_no_forbidden_wording(self):
        for project in Project.objects.all():
            blob = ' '.join(str(v) for v in vars(project).values()).lower()
            self.assertNotIn('vibe coding', blob)

    def test_github_urls_only_for_known_public_repos(self):
        allowed = set()  # ish loyihalari uchun GitHub havolasi qo'yilmaydi
        urls = set(Project.objects.exclude(github_url='').values_list('github_url', flat=True))
        self.assertTrue(urls <= allowed)

    def test_cover_and_gallery_files_exist(self):
        static_root = Path(__file__).resolve().parent / 'static'
        for project in Project.objects.all():
            for path in ([project.cover] if project.cover else []) + project.gallery_list:
                self.assertTrue((static_root / path).exists(), path)


class AdminTests(PortfolioTestCase):
    def setUp(self):
        from django.contrib.auth import get_user_model
        user = get_user_model().objects.create_superuser('admin', 'a@example.test', 'pass-12345')
        self.client.force_login(user)

    def test_changelist_with_filters(self):
        for query in ('', '?kind=work', '?category=bot', '?status=live', '?is_featured__exact=1'):
            with self.subTest(query=query):
                self.assertEqual(self.client.get(f'/admin/core/project/{query}').status_code, 200)

    def test_category_filter_matches_only_exact_tokens(self):
        response = self.client.get('/admin/core/project/?category=bot')
        self.assertContains(response, 'SaveClip')
        self.assertNotContains(response, 'Lumarcos')

    def test_change_form_renders(self):
        project = Project.objects.get(slug='lumarcos')
        self.assertEqual(self.client.get(f'/admin/core/project/{project.pk}/change/').status_code, 200)


class ProjectUpdateTests(PortfolioTestCase):
    """Qo'shimcha o'zgarishlar: kitob do'koni olib tashlandi, UzStroyMarket, SaveClip, Ustudy modullari."""

    def test_online_book_store_is_gone_everywhere(self):
        self.assertFalse(Project.objects.filter(slug='online-book-store').exists())
        self.assertEqual(self.client.get('/projects/online-book-store/').status_code, 404)
        for url in ('/', '/projects/', '/sitemap.xml'):
            body = self.client.get(url).content.decode().lower()
            self.assertNotIn('book store', body)
            self.assertNotIn('online-book-store', body)
        static_root = Path(__file__).resolve().parent / 'static' / 'core' / 'projects'
        self.assertFalse((static_root / 'online-book-store').exists())

    def test_uzstroymarket_is_first_among_personal_and_client_projects(self):
        project = Project.objects.get(slug='uzstroymarket')
        self.assertEqual(project.kind, 'personal')
        self.assertTrue(project.is_featured)
        self.assertEqual(project.status, 'live')
        self.assertEqual(project.live_url, 'https://uzstroymarket.uz')
        self.assertEqual(sorted(project.category_list), ['backend', 'web'])
        others = Project.objects.filter(kind__in=('personal', 'client'), is_featured=True).exclude(pk=project.pk)
        self.assertTrue(all(project.order < o.order for o in others))
        home = self.client.get('/').context['other_projects']
        self.assertEqual(home[0]['slug'], 'uzstroymarket')

    def test_uzstroymarket_page_content(self):
        response = self.client.get('/projects/uzstroymarket/?lang=en')
        self.assertContains(response, 'https://uzstroymarket.uz')
        for fact in ('idempotent', 'audit', 'Fastify 5', 'grammY', 'Next.js 15', 'AWS'):
            self.assertContains(response, fact)
        self.assertNotContains(response, 'github.com/dostonbeksuyunov/stroymarkett')
        self.assertContains(response, 'Code is private')

    def test_server_ip_is_never_published(self):
        for url in ('/', '/projects/', '/projects/uzstroymarket/', '/sitemap.xml'):
            self.assertNotContains(self.client.get(url), '13.48.135.120')
        for project in Project.objects.all():
            self.assertNotIn('13.48.135.120', ' '.join(str(v) for v in vars(project).values()))

    def test_saveclip_description_is_up_to_date(self):
        for lang in LANGS:
            body = self.client.get(f'/projects/saveclip/?lang={lang}').content.decode().lower()
            for forbidden in ('youtube', 'facebook', 'siqish', 'сжат', 'compress', 'lower the quality'):
                with self.subTest(lang=lang, word=forbidden):
                    self.assertNotIn(forbidden, body)
        page = self.client.get('/projects/saveclip/?lang=en')
        for fact in ('Instagram', 'TikTok', 'Twitter/X', 'Pinterest', '4K', 'MP3', 'group'):
            self.assertContains(page, fact)

    def test_saveclip_gallery_and_stack_do_not_mention_removed_platforms(self):
        project = Project.objects.get(slug='saveclip')
        blob = ' '.join(str(v) for v in vars(project).values()).lower()
        self.assertNotIn('youtube', blob)
        self.assertNotIn('facebook', blob)

    def test_ustudy_course_has_twelve_modules_everywhere(self):
        self.assertContains(self.client.get('/?lang=uz'), '12 modulli')
        self.assertContains(self.client.get('/?lang=ru'), '12 модулей')
        self.assertContains(self.client.get('/?lang=en'), '12-module')
        for lang in LANGS:
            body = self.client.get(f'/?lang={lang}').content.decode()
            self.assertNotIn('10 modul', body)
            self.assertNotIn('10-module', body)
            self.assertNotIn('10 модул', body)

    def test_resume_file_matches_source_and_is_hashed_for_download(self):
        resume = Path(__file__).resolve().parent / 'static' / 'core' / 'resume.pdf'
        self.assertTrue(resume.exists())
        self.assertTrue(resume.read_bytes().startswith(b'%PDF'))
        self.assertContains(self.client.get('/'), 'download="Dostonbek_Suyunov_CV.pdf"')

    def test_removal_migration_deletes_existing_row(self):
        from importlib import import_module
        from django.apps import apps
        Project.objects.create(slug='online-book-store', title='x', year_start=2026, short_uz='a', short_ru='a', short_en='a')
        migration = import_module('core.migrations.0002_remove_online_book_store')
        migration.remove_book_store(apps, None)
        self.assertFalse(Project.objects.filter(slug='online-book-store').exists())


class ScopeTests(PortfolioTestCase):
    """Saytda faqat tasdiqlangan loyihalar bo'ladi."""

    ALLOWED = {'lumarc-sayt', 'lumarcos', 'e-auksion-radar', 'lumarcode', 'akromind', 'moneyflow', 'saveclip',
               'uzstroymarket'}
    REMOVED = ('tashkent-3d-residence', 'bahober', 'yuridik-yordam', 'shajara', 'language-bot', 'buy-a-ticket-bot',
               'gym-management', 'hunarmandlar-tarmogi', 'umumiy-sayt', 'u13-task-manager', 'normativ-drf',
               'stadium-booking', 'taxi-trips', 'online-book-store')

    def test_only_approved_projects_exist(self):
        self.assertEqual(set(Project.objects.values_list('slug', flat=True)), self.ALLOWED)

    def test_removed_projects_return_404_and_have_no_media(self):
        media = Path(__file__).resolve().parent / 'static' / 'core' / 'projects'
        for slug in self.REMOVED:
            with self.subTest(slug=slug):
                self.assertEqual(self.client.get(f'/projects/{slug}/').status_code, 404)
                self.assertFalse((media / slug).exists())

    def test_3d_project_is_not_shown_anywhere(self):
        for url in ('/', '/projects/', '/sitemap.xml'):
            body = self.client.get(url).content.decode().lower()
            self.assertNotIn('tashkent city residence', body)
            self.assertNotIn('tashkent-3d', body)

    def test_lumarc_site_has_live_link(self):
        self.assertContains(self.client.get('/projects/lumarc-sayt/'), 'https://lumarc.uz')
        self.assertEqual(Project.objects.get(slug='lumarc-sayt').status, 'live')

    def test_trim_migration_removes_rows(self):
        from importlib import import_module
        from django.apps import apps
        Project.objects.create(slug='shajara', title='x', year_start=2026, short_uz='a', short_ru='a', short_en='a')
        import_module('core.migrations.0003_trim_projects').remove_projects(apps, None)
        self.assertFalse(Project.objects.filter(slug='shajara').exists())
        self.assertEqual(Project.objects.count(), len(self.ALLOWED))


class ContactListTests(PortfolioTestCase):
    def test_instagram_is_in_contact_list_and_footer(self):
        response = self.client.get('/')
        self.assertContains(response, 'href="https://www.instagram.com/suyunov.dev_"', count=2)
        self.assertContains(response, '@suyunov.dev_')

    def test_contact_section_is_a_clickable_link_list(self):
        response = self.client.get('/')
        self.assertContains(response, 'class="link-list"')
        self.assertContains(response, 'link-row-arrow', count=7)
        self.assertNotContains(response, 'contact-card')

    def test_contact_list_has_all_channels(self):
        response = self.client.get('/?lang=en')
        for label in ('Email', 'Phone', 'Résumé', 'GitHub', 'LinkedIn', 'Telegram', 'Instagram'):
            self.assertContains(response, f'<span class="link-row-name">{label}</span>')
