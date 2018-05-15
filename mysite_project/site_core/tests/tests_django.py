#!/usr/bin/env python3

from django.test import TestCase


class LoginWorks(TestCase):

    def test_get_root_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_template_loads(self):
        response = self.client.get('/')
        template_names = [i.name for i in response.templates]
        self.assertIn('mysite/frontpage.html', template_names)
        self.assertIn('base.html', template_names)
        self.assertTemplateUsed(response, 'base.html')

    def test_post_login(self):
        response = self.client.post('/accounts/login/', {'admin': 'admin', })
        self.assertEqual(response.status_code, 200)
