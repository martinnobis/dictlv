from django.test import TestCase
from django.apps import apps

class FixtureTest(TestCase):
    fixtures = ['translations.json']

    def set_model_management(self, setting):
        unmanaged_models = [m for m in apps.get_models() if not m._meta.managed]
        for m in unmanaged_models:
            m._meta.managed = setting 

    def setUp(self):
        self.set_model_management(True)

    def tearDown(self):
        self.set_model_management(False)