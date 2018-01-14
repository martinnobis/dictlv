from django.test import TestCase
from translations.forms import TranslationForm

class TranslationFormTest(TestCase):

    def test_form_word_input_has_placeholder(self):
        form = TranslationForm()
        # What is form.as_p()??
        self.assertIn('placeholder="Enter a word to translate"', form.as_p())

