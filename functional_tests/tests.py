from selenium import webdriver
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
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
        inputbox = self.browser.find_element_by_id('id_translate_word')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a word to translate'
        )

        # He decides to put a word in English, "hello".

        # When he hits enter a translation appears!

        # He checks if a Latvian word will work, he puts it in and hits enter.

        # Again a translation appears!

