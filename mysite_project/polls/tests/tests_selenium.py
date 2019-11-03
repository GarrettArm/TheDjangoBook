#! /usr/bin/env python3

# import time
import unittest
from urllib.parse import urlsplit

from selenium import webdriver

# from selenium.webdriver.common.keys import Keys


class ObservingQuestionItem(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_layout_looks_normal(self):
        self.browser.get("http://127.0.0.1:8000/polls/")
        self.assertIn("Polls", self.browser.title)

        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertEqual("Poll Options", header_text)


class RedirectAfterClickQuestionItem(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_first_question_item(self):
        self.browser.get("http://127.0.0.1:8000/polls/")
        first_question = self.browser.find_element_by_id("question 1")
        first_question.click()
        third_to_last, next_to_last = urlsplit(self.browser.current_url).path.split(
            "/"
        )[-3:-1]
        self.assertEqual(third_to_last, "polls")
        self.assertTrue(next_to_last.isnumeric())
