from django.test import TestCase, override_settings


@override_settings(SECURE_SSL_REDIRECT=False, STORAGES={
    'default': {'BACKEND': 'django.core.files.storage.FileSystemStorage'},
    'staticfiles': {'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage'},
})
class HomeViewTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_default_language_is_uzbek(self):
        response = self.client.get('/')
        self.assertEqual(response.context['current_lang'], 'uz')

    def test_language_switch_is_saved_in_session(self):
        response = self.client.get('/?lang=en')
        self.assertEqual(response.context['current_lang'], 'en')
        response = self.client.get('/')
        self.assertEqual(response.context['current_lang'], 'en')

    def test_invalid_language_falls_back_to_session_value(self):
        self.client.get('/?lang=ru')
        response = self.client.get('/?lang=xx')
        self.assertEqual(response.context['current_lang'], 'ru')

    def test_empty_timeline_description_is_hidden(self):
        response = self.client.get('/')
        self.assertNotContains(response, '<p class="timeline-desc"></p>')
