#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup


g = requests.get('http://bash.im/').content


g = BeautifulSoup(g, "html.parser")


samples = g.find_all("div", "quote")


for i in range(5):
    a = samples[i].find_all('div', 'text')[0]
    print a.contents[0]




