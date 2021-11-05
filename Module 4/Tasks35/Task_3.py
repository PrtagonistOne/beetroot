import threading
import requests
from bs4 import BeautifulSoup
import sys
import io

new_stdout = io.StringIO()
sys.stdout = new_stdout


class SubredditThread(threading.Thread):

    def __init__(self, params):
        threading.Thread.__init__(self)
        self.params = params

    def run(self):
        r = requests.get('https://api.pushshift.io/reddit/comment/search/', self.params)
        print(BeautifulSoup(r.text, 'lxml'))


thread1 = SubredditThread({'subreddit': 'threads', 'sort': 'desc', 'sort_type': 'created_utc', 'size': 2})
thread1.start()
thread1.join()
data = new_stdout.getvalue()
with open('task_3.txt', 'w') as f:
    f.write(str(data))
