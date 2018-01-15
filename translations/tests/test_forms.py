from django.test import TestCase
from translations.forms import SearchForm

class SearchFormTest(TestCase):

    def test_form_text_input_has_placeholder(self):
        form = SearchForm()
        # What is form.as_p()??
        self.assertIn('placeholder="Enter a word to translate"', form.as_p())

