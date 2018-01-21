from selenium import webdriver
from django.apps import apps
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest

class NewVisitorTest(FunctionalTest):
    fixtures = ['translations.json']

    def set_model_management(self, setting):
        unmanaged_models = [m for m in apps.get_models() if not m._meta.managed]
        for m in unmanaged_models:
            m._meta.managed = setting 

    def setUp(self):
        self.set_model_management(True)
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.set_model_management(False)
        self.browser.quit()

    def test_can_translate_a_word(self):
        # Karlis has heard of this cool new translator. He checks it out on his
        # browser.
        self.browser.get(self.live_server_url)

        # He notices the page title and header mention an English/Latvian
        # translator.
        self.assertIn('EN ⇆ LV', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('DictLV', header_text)

        # He's invited to enter a word to translate. 
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a word to translate'
        )

        # He decides to put a word in English, "hello".
        inputbox.send_keys('hello')

        # When he hits enter he sees that his search term is returned
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_results_table('hello')

        # And a translation appears underneath it!
        self.wait_for_row_in_results_table('sveiki')

        # He checks if a Latvian word will work, he puts it in and hits enter.
        self.fail('Finish the test!')

        # Again a translation appears!

