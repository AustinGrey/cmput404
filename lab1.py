#!/usr/bin/env python

import requests
print(requests.__version__)

input()

print(requests.get("http://www.google.com/teapot"))

