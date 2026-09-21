from django.test import TestCase
from django.urls import reverse

class PortfolioViewsTest(TestCase):
    def test_home_page_status_code(self):
        # Bosh sahifa status kodi 200 (OK) qaytarishini tekshirish
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
