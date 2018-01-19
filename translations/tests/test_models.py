from django.apps import apps
from django.test import TestCase
from translations.models import English, Latvian, Enlv
from .base import (get_latvian_from_id, get_latvian_from_text,
                   get_english_from_text, get_english_from_id,
                   get_intersect_from_english_id, get_intersect_from_latvian_id)

class DBFixtureTest(TestCase):
    fixtures = ['translations.json']

    def setUp(self):
        unmanaged_models = [m for m in apps.get_models() if not m._meta.managed]
        for m in unmanaged_models:
            m._meta.managed = True

    def tearDown(self):
        unmanaged_models = [m for m in apps.get_models() if m._meta.managed]
        for m in unmanaged_models:
            m._meta.managed = False

    def test_finds_one_to_one_translation(self):
        self.assertIsNotNone(get_english_from_text(text='hello'))

    def test_finds_one_to_many_translations(self):
        pass

    def test_cannot_find_search_term(self):
        pass

    def test_finds_no_translations(self):
        pass
