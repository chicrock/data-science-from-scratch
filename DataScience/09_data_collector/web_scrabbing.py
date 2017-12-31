# _*_ coding: utf-8 _*_
from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.gabia.com").text
soup = BeautifulSoup(html, 'html5lib')


# print soup('div', {'class':'borderBoxbot'})
print soup('div', 'borderBoxbot')