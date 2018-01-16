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
class SearchViewMockTest(unittest.TestCase):

    def setUp(self):
        self.request = HttpRequest()
        self.request.method = 'POST'
        self.request.POST['text'] = 'hello'

    def test_passes_POST_data_to_SearchForm(self, mockSearchForm):
        search(self.request)
        mockSearchForm.assert_called_once_with(self.request.POST)

class SearchViewTest(TestCase):

    def test_redirects_after_POST(self):
        response = self.client.post('/tr/k/srch', data={'text': 'hi'})
        self.assertRedirects(response, '/tr/Hi/')

    def test_POST_uses_result_template(self):
        response = self.client.post('/tr/k/srch', data={'text': 'hi'},
            follow=True)
        self.assertTemplateUsed(response, 'result.html')

class ResultViewTest(TestCase):

    def test_uses_result_template(self):
        response = self.client.get('/tr/hello/')
        self.assertTemplateUsed(response, 'result.html')

    # TODO: These should check for the EXACT string in the EXACT spot

    def test_displays_searched_text(self):
        response = self.client.get('/tr/hello/')
        self.assertContains(response, 'hello')

    def test_displays_searched_text_with_special_characters(self):
        response = self.client.get('/tr/labrīt/')
        self.assertContains(response, 'labrīt')

    def test_searching_for_search_still_works(self):
        response = self.client.get('/tr/search/')
        self.assertContains(response, 'search')