#!/usr/bin/env python3
"""Module: test client.py file"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """"test client module"""

    @parameterized.expand([
        "google",
        "abc"
    ]
    )
    @patch('utils.get_json')
    def test_org(self, org, mock_get_json):
        """test the org function"""
        url = GithubOrgClient.ORG_URL.format(org=org)
        mock_get_json(url)
        mock_get_json.assert_called_once_with(url)

    def test_public_repos_url(self):
        """test the public_repos function"""

        with patch.object(
                        GithubOrgClient,
                        'org',
                        new_callable=PropertyMock) as mock_org:
            mock_org.return_value = True



    @patch('utils.get_json')
    def test_public_repos(self, mock_get_json):
        """test the public_repos function"""

        mock_get_json.return_value = "mockity mock"

        with patch.object(
                    GithubOrgClient,
                    '_public_repos_url',
                    new_callable=PropertyMock) as mock_org:

            mock_org.return_value = "dockity dock"
            mock_org().assert_called_once()

        mock_get_json().assert_called_once()




