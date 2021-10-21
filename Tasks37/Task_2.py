import aiohttp
import asyncio
import json


async def get_data(url, parametrs):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, params=parametrs) as r:
            data = await r.text()
            value = json.loads(data)
        temp = []
        for i in list(range(parametrs['size'])):
            temp.append(value['data'][i]['body'])
    return temp


if __name__ == '__main__':
    base_url = 'https://api.pushshift.io/reddit/comment/search/'

    with open('task_2.txt', 'w') as file:
        loop = asyncio.get_event_loop().run_until_complete(
            get_data(base_url, {'subreddit': 'python', 'sort': 'desc', 'sort_type': 'created_utc', 'size': 4}))
        json.dump(loop, file, indent=1)
