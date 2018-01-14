from django.test import TestCase
from translations.forms import TranslationForm

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_uses_translation_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], TranslationForm)
