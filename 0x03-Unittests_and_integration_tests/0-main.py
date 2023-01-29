#!/usr/bin/env python3

from utils import access_nested_map
from typing import Mapping

nested_map = {"i": {"h": {}}}
access_nested_map(nested_map, ["i", "h", "k"])
print(isinstance(nested_map, Mapping))
