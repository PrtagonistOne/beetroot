import threading
import requests
from bs4 import BeautifulSoup


class SubredditThread(threading.Thread):

    def __init__(self, params):
        threading.Thread.__init__(self)
        self.params = params

    def run_request(self):
        r = requests.get('https://api.pushshift.io/reddit/comment/search/', self.params)
        return BeautifulSoup(r.text, 'lxml')


thread1 = SubredditThread({'subreddit': 'threads', 'sort': 'desc', 'sort_type': 'created_utc', 'size': 2})
thread1.start()
data = thread1.run_request()
thread1.join()

with open('task_3.txt', 'w') as f:
    f.write(str(data))