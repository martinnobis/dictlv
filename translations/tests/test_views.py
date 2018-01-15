import unittest
from unittest.mock import patch
from django.http import HttpRequest
from django.test import TestCase
from translations.forms import SearchForm
from translations.views import search

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_uses_translation_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], SearchForm)

@patch('translations.views.SearchForm')
class SearchViewTest(unittest.TestCase):

    def setUp(self):
        self.request = HttpRequest()
        self.request.method = 'POST'
        self.request.POST['text'] = 'hello'

    def test_passes_POST_data_to_SearchForm(self, mockSearchForm):
        search(self.request)
        mockSearchForm.assert_called_once_with(self.request.POST)

class ResultViewTest(TestCase):

    def test_uses_result_template(self):
        response = self.client.get('/tr/hello/')
        self.assertTemplateUsed(response, 'result.html')

    def test_displays_searched_text(self):
        response = self.client.get('/tr/hello/')
        self.assertContains(response, 'hello')

    def test_displays_searched_text_with_special_characters(self):
        response = self.client.get('/tr/labrīt/')
        self.assertContains(response, 'labrīt')
