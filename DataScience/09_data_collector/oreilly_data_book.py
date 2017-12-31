# _*_ coding: utf-8 _*_
from bs4 import BeautifulSoup
import requests

html = requests.get("http://shop.oreilly.com/category/browser-subjects/data.do?sortby=publicationDate&page=1").text
soup = BeautifulSoup(html, 'html5lib')

print soup