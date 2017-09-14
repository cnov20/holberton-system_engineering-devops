#!/usr/bin/python3

'''
This is module utilizes the Reddit API to make API calls,
which query for total number of subscribers for a given subreddit
'''

from fake_useragent import UserAgent
import requests

def number_of_subscribers(subreddit):

    ua = UserAgent()
    headers = {'User-Agent': str(ua.random)}
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    response = requests.get(url, headers=headers).json()
    responseStatus = requests.get(url, headers=headers)
    if responseStatus.status_code != 200:
        return (0)
    else:
        subscribers = response.get('data').get('subscribers')
        return (subscribers)
