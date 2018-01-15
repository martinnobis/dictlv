from django.test import TestCase
from translations.forms import TranslationForm

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_uses_translation_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], TranslationForm)

class ResultViewTest(TestCase):

    def test_uses_result_template(self):
        response = self.client.get('/translations/hello')
        self.assertTemplateUsed(response, 'result.html')

    def test_displays_searched_text(self):
        response = self.client.get('/translations/hello')
        self.assertContains(response, 'hello')

    def test_displays_searched_text_with_special_characters(self):
        response = self.client.get('/translations/labrīt')
        self.assertContains(response, 'labrīt')
