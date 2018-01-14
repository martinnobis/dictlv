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
        self.fail('Finish the test!')

        # He's invited to enter a word to translate, either English or Latvian

        # He hits enter, and a translation appears!

