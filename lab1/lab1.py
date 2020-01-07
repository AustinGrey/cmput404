#!/usr/bin/env python
# This script was originally submitted when I looked at this course over a year ago - I have modified it to match the current version of the lab and resubmitted for this semester.

import requests
#print(requests.__version__)

#input()

#google = requests.get("http://www.google.com")
#print(google)


print(requests.get("https://raw.githubusercontent.com/AustinGrey/cmput404/master/lab1.py").text)
