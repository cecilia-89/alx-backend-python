#!/usr/bin/env python3

from client import GithubOrgClient

github = GithubOrgClient('pinterest')
for repo in github.repos_payload:
    print(repo["name"])