import requests

from bs4 import BeautifulSoup

base_url = 'https://api.pushshift.io/reddit/comment/search/'


def get_data(url, parametrs):
    r = requests.get(url, parametrs)
    return BeautifulSoup(r.text, 'lxml')


params = {'subreddit': 'python', 'sort': 'desc', 'sort_type': 'created_utc', 'size': 4}

data = get_data(base_url, params)

with open('task_2.txt', 'w') as f:
    f.write(str(data))
