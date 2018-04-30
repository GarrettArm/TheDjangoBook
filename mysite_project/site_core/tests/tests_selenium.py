#!/usr/bin/env python3

import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    dev_url = 'http://127.0.0.1:8000'
    prod_url = 'https://gaularmstrong.com'

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.close()

    def test_prod_server_loads_main_page(self):
        self.browser.get(self.prod_url)
        expected_title_text = 'Base Title'
        self.assertIn(expected_title_text, self.browser.title)

    def test_dev_server_loads_main_page(self):
        self.browser.get(self.dev_url)
        expected_title_text = 'Base Title'
        self.assertIn(expected_title_text, self.browser.title)

    def test_css_loads_dev(self):
        self.browser.get(self.dev_url)
        header = self.browser.find_element_by_tag_name('h1')
        title_color = header.value_of_css_property('color')
        self.assertEqual('rgb(117, 76, 76)', title_color,
                         'Dev css not loaded, title expected to be brown')

    def test_css_loads_prod(self):
        self.browser.get(self.prod_url)
        header = self.browser.find_element_by_tag_name('h1')
        title_color = header.value_of_css_property('color')
        self.assertEqual('rgb(117, 76, 76)', title_color,
                         'Production css not loaded, title expected to be brown')
