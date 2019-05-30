from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ContactAtsushiTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super().setUp()

    def tearDown(self):
        self.selenium.quit()
        super().tearDown()

    # def test_test(self):
    #     s = self.selenium

    #     s.get('http://localhost:8000')
    #     self.fail('Test over!')
