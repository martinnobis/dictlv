import string
from django.apps import apps
from django.test import TestCase
from translations.models import English, Latvian
from translations.tests.fixture_test import FixtureTest
from translations.utils import (get_translation, get_object_from_text, 
                                special_chars)

class RetrieveTest(FixtureTest):
    fixtures = ['translations.json']

    def set_model_management(self, setting):
        unmanaged_models = [m for m in apps.get_models() if not m._meta.managed]
        for m in unmanaged_models:
            m._meta.managed = setting 

    def setUp(self):
        self.set_model_management(True)

    def tearDown(self):
        self.set_model_management(False)

    def test_finds_english_object(self):
        self.assertIsNotNone(get_object_from_text(English, 'hello'))

    def test_finds_latvian_object(self):
        self.assertIsNotNone(get_object_from_text(Latvian, 'sveiki'))

    def test_finds_one_to_one_translation(self):
        translation = get_translation(English, Latvian, 'town')
        self.assertIn("pilsēta", translation)

    def test_finds_one_to_many_translations(self):
        translations = get_translation(Latvian, English, 'sveiki')
        self.assertIn("hello", translations)
        self.assertIn("hi", translations)

    def test_cannot_find_search_term(self):
        self.assertIsNone(get_object_from_text(Latvian, 'sveaikiu'))
        self.assertIsNone(get_object_from_text(English, 'helloooo'))

    def test_finds_no_translations(self):
        self.assertFalse(get_translation(Latvian, English, 'suns'))
        self.assertFalse(get_translation(Latvian, English, 'ar labu nakti'))
        self.assertFalse(get_translation(English, Latvian, 'browser'))

    def test_translation_handles_punctuation(self):
        translation = get_translation(Latvian, English, "Cik ir pulkstenis?")
        self.assertIn("What is the time?", translation)

class SpecialCharacterTest(TestCase):

    def test_all_special_characters_removed_from_text(self):
        text = "ēeāaīiūučcģgķkļlņnšsžz"
        expected = "eeaaiiuuccggkkllnnsszz"
        modified_text = text.translate(text.maketrans(special_chars))
        self.assertEqual(expected, modified_text)