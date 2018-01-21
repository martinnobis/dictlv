from django.apps import apps
from django.test import TestCase
from translations.models import English, Latvian, Enlv
from translations.utils import (get_translation, get_object_from_text)

class DBFixtureTest(TestCase):
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
        # Just in case, test for non existant object
        self.assertIsNone(get_object_from_text(English, 'hello!'))

    def test_finds_latvian_object(self):
        self.assertIsNotNone(get_object_from_text(Latvian, 'sveiki'))
        # Just in case, test for non existant object
        self.assertIsNone(get_object_from_text(Latvian, 'sveaikiu'))

    def test_finds_one_to_one_translation(self):
        self.assertIn("sveiki", get_translation(English, Latvian, 'hello'))

    def test_finds_one_to_many_translations(self):
        translations = get_translation(Latvian, English, 'sveiki')
        self.assertIn("hello", translations)
        self.assertIn("hi", translations)

    def test_cannot_find_search_term(self):
        pass

    def test_finds_no_translations(self):
        pass
