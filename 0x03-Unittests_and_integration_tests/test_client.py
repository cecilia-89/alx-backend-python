#!/usr/bin/env python3
"""Module: test client.py file"""
import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient


@parameterized_class(('org'), [
        "google",
        "abc"
    ])
class TestGithubOrgClient(unittest.TestCase):
    """"test client module"""

    @patch('utils.get_json')
    def test_org(self, mock_get_json):
        """test the org function"""
        url = GithubOrgClient.ORG_URL.format(org=self.org)
        mock_get_json(url)
        mock_get_json.assert_called_once_with(url)

