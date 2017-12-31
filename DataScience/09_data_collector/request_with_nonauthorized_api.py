# _*_ coding: utf-8 _*_
import requests, json
from dateutil.parser import parser
from collections import Counter

url = "https://api.github.com/users/jsrjsr0040/repos"

repos = json.loads(requests.get(url).text)
dates = [parser(repo['created_at']) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)

print weekday_counts