#!/usr/bin/env python

import requests
#print(requests.__version__)

#input()

#print(requests.get("http://www.google.com/teapot"))
print(requests.get("https://raw.githubusercontent.com/AustinGrey/cmput404/master/lab1.py").text)
