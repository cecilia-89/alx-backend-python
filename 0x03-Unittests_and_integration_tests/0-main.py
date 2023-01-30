#!/usr/bin/env python3

from client import GithubOrgClient

github = GithubOrgClient('google')
print(github.has_license({"license": {"key": "my_license"}}, "my_license"))
