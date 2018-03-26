#!/usr/bin/env python3

import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.close()

    def test_prod_server_loads_main_page(self):
        url = 'http://127.0.0.1:8088'
        self.browser.get(url)
        expected_title_text = 'Base Title'
        self.assertIn(expected_title_text, self.browser.title)

    def test_dev_server_loads_main_page(self):
        url = 'http://127.0.0.1:8000'
        self.browser.get(url)
        expected_title_text = 'Base Title'
        self.assertIn(expected_title_text, self.browser.title)
