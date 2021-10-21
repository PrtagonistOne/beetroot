from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import os
import requests
from bs4 import BeautifulSoup

base_url = 'https://api.pushshift.io/reddit/comment/search/'


def get_data(url, parametrs):
    r = requests.get(url, parametrs)
    print(f'process {os.getpid()} and parent {os.getppid()}')
    return BeautifulSoup(r.text, 'lxml')


params1 = {'subreddit': 'python', 'sort': 'desc', 'sort_type': 'created_utc', 'size': 1}
params2 = {'subreddit': 'java', 'sort': 'desc', 'sort_type': 'created_utc', 'size': 1}
params3 = {'subreddit': 'c++', 'sort': 'desc', 'sort_type': 'created_utc', 'size': 1}
params4 = {'subreddit': 'rubi', 'sort': 'desc', 'sort_type': 'created_utc', 'size': 1}


def main():
    with ProcessPoolExecutor() as executor:
        processes = []
        for i in range(4):
            t = multiprocessing.Process(target=get_data, args=(base_url, "params" + str(i + 1),))
            processes.append(t)
            t.start()
        for process in processes:
            process.join()


if __name__ == "__main__":
    main()
