#!/usr/bin/env python3

import unittest
from django.test import Client


class LoginWorks(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_root_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_post_login(self):
        response = self.client.post('/accounts/login/', {'admin': 'admin', })
        self.assertEqual(response.status_code, 200)
