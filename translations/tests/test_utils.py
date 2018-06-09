import string
from django.apps import apps
from django.test import TestCase
from translations.models import English, Latvian
from translations.utils import (get_translations, get_object_from_text, 
                                special_chars, get_similar_latvian_words,
                                translation_exists)

class RetrieveTest(TestCase):
    fixtures = ['translations.json']

    def test_finds_english_object(self):
        self.assertIsNotNone(get_object_from_text(English, 'hello'))

    def test_finds_latvian_object(self):
        self.assertIsNotNone(get_object_from_text(Latvian, 'sveiki'))

    def test_finds_one_to_one_translation(self):
        translation = get_translations(English, Latvian, 'town')
        self.assertIn("pilsēta", translation)

    def test_finds_one_to_many_translations(self):
        translations = get_translations(Latvian, English, 'sveiki')
        self.assertIn("hello", translations)
        self.assertIn("hi", translations)

    def test_cannot_find_search_term(self):
        self.assertFalse(get_object_from_text(Latvian, 'sveaikiu'))
        self.assertFalse(get_object_from_text(English, 'helloooo'))

    def test_finds_no_translations(self):
        self.assertFalse(get_translations(Latvian, English, 'suns'))
        self.assertFalse(get_translations(Latvian, English, 'ar labu nakti'))
        self.assertFalse(get_translations(English, Latvian, 'browser'))

    def test_translation_handles_punctuation(self):
        translation = get_translations(Latvian, English, "Cik ir pulkstenis?")
        self.assertIn("What is the time?", translation)

    def test_translation_exists(self):
        text = 'hi'
        self.assertTrue(translation_exists(English, text))
        text = 'asdwer'
        self.assertFalse(translation_exists(English, text))

class SpecialCharacterTest(TestCase):
    fixtures = ['translations.json']

    def test_all_special_characters_removed_from_text(self):
        text = "ēeāaīiūučcģgķkļlņnšsžz"
        expected = "eeaaiiuuccggkkllnnsszz"
        modified_text = text.translate(text.maketrans(special_chars))
        self.assertEqual(expected, modified_text)
    
    def test_returns_correct_candidate_with_missing_special_chars(self):
        text = "pilseta"
        candidates = get_similar_latvian_words(text)
        self.assertIn("pilsēta", candidates)

    def test_returns_correct_candidate_with_missing_some_special_chars(self):
        text = "meklešana"
        candidates = get_similar_latvian_words(text)
        self.assertIn("meklēšana", candidates)
