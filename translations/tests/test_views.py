import unittest
from unittest.mock import patch
from django.http import HttpRequest
from django.urls import reverse 
from django.test import TestCase
from translations.forms import SearchForm
from translations.views import search

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_uses_search_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], SearchForm)

@patch('translations.views.SearchForm')
class SearchViewMockTest(unittest.TestCase):

    def setUp(self):
        self.request = HttpRequest()
        self.request.method = 'GET'
        self.request.GET['text'] = 'hello'

    # TODO: This test isn't very useful now since SearchForm() is called twice,
    # but the previous assert didn't notice. Could clear the form using
    # Javascript on the client side instead of passing a new form.
    def test_passes_GET_data_to_SearchForm(self, mockSearchForm):
        search(self.request)
        mockSearchForm.assert_called()

class SearchViewTest(TestCase):
    fixtures = ['translations.json']

    def test_uses_result_template(self):
        response = self.client.get(reverse('view_search'), data={'text': 'hi'})
        self.assertTemplateUsed(response, 'result.html')

    def test_displays_searched_text(self):
        response = self.client.get(reverse('view_search'), data={'text': 'hello'})
        self.assertContains(response, 'hello')

    def test_displays_searched_text_with_special_characters(self):
        response = self.client.get(reverse('view_search'), data={'text': 'labrīt'})
        self.assertContains(response, 'labrīt')

    def test_wrong_special_characters_uses_did_you_mean_template(self):
        response = self.client.get(reverse('view_search'), data={'text': 'pilseta'})
        self.assertTemplateUsed(response, 'didyoumean.html')

