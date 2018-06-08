import unittest
from unittest.mock import patch
from unittest import skip
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpRequest
from django.urls import reverse 
from django.test import TestCase
from translations.forms import SearchForm
from translations.views import show_translation, search

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_uses_search_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], SearchForm)

class SearchViewTest(TestCase):
    fixtures = ['translations.json']

    def test_uses_result_template(self):
        response = self.client.get(reverse('view_search'), data={'text': 'hi'})
        self.assertTemplateUsed(response, 'result.html')

    def test_final_url_has_search_term_in_it(self):
        pass
        # TODO: Test redirection here
        #form = SearchForm()
        #form.text = 'table'
        #response = self.client.get(reverse('view_search'), data={'form': form})
        #print(response)
        #url = reverse('view_search', kwargs={'term': 'table'})
        #self.assertIn('table', url)

    def test_displays_searched_text(self):
        request = HttpRequest()
        request.GET['text'] = 'chair'
        response = search(request)
        self.assertContains(response, 'chair')

    def test_displays_searched_text_with_special_characters(self):
        request = HttpRequest()
        request.GET['text'] = 'labrīt'
        response = search(request)
        self.assertContains(response, 'labrīt')

    def test_wrong_special_characters_uses_did_you_mean_template(self):
        response = self.client.get(reverse('view_search'), data={'text': 'pilseta'})
        self.assertTemplateUsed(response, 'didyoumean.html')

    def test_special_char_term_without_translation_returns_no_result(self):
        response = self.client.get(reverse('view_search'), data={'text': 'meklesana'})
        self.assertTemplateUsed(response, 'noresult.html')

    def test_cannot_search_correctly_with_term_which_has_spaces(self):
        pass
        #request = HttpRequest()
        #request.GET['text'] = 'train station'
        #response = search(request)
        #self.assertNotContains(response, 'train station')

    def test_search_term_cannot_match_just_the_beginning_part_of_text(self):
        response = self.client.get(reverse('view_search'), data={'text': 'what i'})
        self.assertTemplateUsed(response, 'noresult.html')

    def test_search_term_cannot_match_just_the_end_part_of_text(self):
        response = self.client.get(reverse('view_search'), data={'text': 'ime'})
        self.assertTemplateUsed(response, 'noresult.html')


@patch('translations.views.SearchForm')
class SearchViewMockTest(unittest.TestCase):
    fixtures = ['translations.json']

    def setUp(self):
        self.request = HttpRequest()
        self.request.GET['text'] = 'hello'

    @skip('This test doesnt work, mock raises exception')
    def test_passes_GET_data_to_SearchForm(self, mockSearchForm):
        search(self.request)
        #mockSearchForm.assert_called_once_with(data=self.request.GET)
