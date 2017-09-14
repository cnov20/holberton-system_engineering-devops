#!/usr/bin/python3

'''
This module utilizes the Reddit API to make API calls,
which query for total number of subscribers for a given subreddit
'''

import requests


def number_of_subscribers(subreddit):

    '''
    Method finds the num of subscribers in given subreddit
    subreddit: given subreddit to be make request to
    '''

    headers = {'User-Agent': 'Mozilla/5.0; (Macintosh Intel Mac OS X 10_10_1)'
               'AppleWebKit/537.36 (KHTML, like Gecko)'
               'Chrome/39.0.2171.95 Safari/537.36'}
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    response = requests.get(url, headers=headers,
                            allow_redirects=False).json()
    if response.get('error'):
        return (0)
    else:
        subscribers = response.get('data').get('subscribers')
        return(subscribers)
