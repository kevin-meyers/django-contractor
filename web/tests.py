from django.urls import resolve
from django.test import TestCase, Client
from django.http import HttpRequest


from .views import Home

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, Home)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = Home(request)
        html = response.content.decode('utf8')
        #self.assertTrue(html.startswith("{% extends 'base.html' %}"))
        #self.assertIn("{% include 'web/partials'", html)
        self.assertTrue(html.endswith('</html>'))
