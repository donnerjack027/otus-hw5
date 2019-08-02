#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-
"""
Simple test mock
"""
from requests_lib import test_check
from unittest.mock import patch
import unittest


class TestApi(unittest.TestCase):
    @patch('requests.get')
    def test_status(self, mock):
        mock.return_value.status_code = 200
        responce = test_check()
        self.assertEqual(responce.status_code, 200)

    @patch('requests.get')
    def test_reason_check(self, mock):
        mock.return_value.reason = 'OK'
        responce = test_check()
        self.assertEqual(responce.reason, 'OK')

    @patch('requests.get')
    def test_ok_check(self, mock):
        mock.return_value.ok = True
        responce = test_check()
        self.assertTrue(responce.ok)

    @patch('requests.get')
    def test_apache_check(self, mock):
        mock.return_value.headers = 'Apache/2.4.29 (Ubuntu)'
        responce = test_check()
        self.assertIn(responce.headers, 'Apache/2.4.29 (Ubuntu)')

    @patch('requests.get')
    def test_url(self, mock):
        mock.return_value.url = 'http://192.168.110.60/opencart/'
        responce = test_check()
        self.assertEqual(responce.url, 'http://192.168.110.60/opencart/')

    @patch('requests.get')
    def test_text_check(self, mock):
        mock.return_value.text = 'test'
        responce = test_check()
        self.assertIsInstance(responce.text, str)
        self.assertEqual(responce.text, 'test')


if __name__ == "__main__":
    unittest.main()
