#!/usr/bin/python3

'''
This is module utilizes the Reddit API to make API calls,
which query for total number of subscribers for a given subreddit
'''

from fake_useragent import UserAgent
import requests


def number_of_subscribers(subreddit):

    '''
    Method finds the num of subscribers in given subreddit
    subreddit: given subreddit to be make request to
    '''

    ua = UserAgent()
    headers = {'User-Agent': str(ua.random)}
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    response = requests.get(url, headers=headers).json()
    if response.get('error'):
        return (0)
    else:
        subscribers = response.get('data').get('subscribers')
        return(subscribers)
