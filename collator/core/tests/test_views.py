from django.urls import resolve

from collator.core.views import home_page

from test_plus.test import TestCase

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
