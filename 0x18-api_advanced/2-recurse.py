#!/usr/bin/python3

'''
This module utilizes the Reddit API to make API calls,
which query for the titles of all 'hot' articles
of a given subreddit - recursively
'''

import requests


def recurse(subreddit, hot_list=[], after=None):

    '''
    Method finds ALL 'hot' articles in given subreddit - recursively
    subreddit: given subreddit to be make request to
    '''

    headers = {
        'User-Agent': 'Mozilla/5.0; (Macintosh Intel Mac OS X 10_10_1)'
        'AppleWebKit/537.36 (KHTML, like Gecko)'
        'Chrome/39.0.2171.95 Safari/537.36',
        'limit': '100'
    }

    following_url = 'https://www.reddit.com/r/{}/hot.json?\
    after={}&hot_list={}'.format(subreddit, after, hot_list)

    response = requests.get(following_url, headers=headers,
                            allow_redirects=False).json()

    if response.get('error'):
        return None

    after = response.get('data').get('after')
    before = response.get('data').get('before')
    children = (response.get('data').get('children'))

    hot_list.append(children)

    return (recurse(subreddit, hot_list, after))
    '''
    print("Before {}".format(before))
    print("Children {}".format(hot_list))
    print("After {}".format(after))
    '''

    '''
     for post in postsList:
        data = post.get('data')
        title = data.get('title')
        print('{}'.format(title))
    '''
