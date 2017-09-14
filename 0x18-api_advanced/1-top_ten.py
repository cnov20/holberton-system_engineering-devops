#!/usr/bin/python3

'''
This is module utilizes the Reddit API to make API calls,
which query for the top ten 'hot' posts for a given subreddit
'''

import requests


def top_ten(subreddit):

    '''
    Method finds the top ten 'hot' posts in given subreddit
    subreddit: given subreddit to be make request to
    '''

    headers = {
        'User-Agent': 'Mozilla/5.0; (Macintosh Intel Mac OS X 10_10_1)'
        'AppleWebKit/537.36 (KHTML, like Gecko)'
        'Chrome/39.0.2171.95 Safari/537.36'
    }
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    response = requests.get(url, headers=headers,  allow_redirects=False).json()
    if response.get('error'):
        print (None)
        return None
    else:
        postsList = response.get('data').get('children')[0:10]

        for post in postsList:
            data = post.get('data')
            title = data.get('title')
            print(title)
