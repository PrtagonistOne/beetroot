import requests

wiki_api = 'https://www.mediawiki.org/wiki/API:Main_page/uk'
twitter_api = 'https://developer.twitter.com/en/docs'

resp = requests.get(wiki_api)

with open("robots.txt", 'w') as file_object:
    file_object.write(resp.text)

resp = requests.get(twitter_api)

with open("robots.txt", 'w+') as file_object:
    file_object.write(resp.text)