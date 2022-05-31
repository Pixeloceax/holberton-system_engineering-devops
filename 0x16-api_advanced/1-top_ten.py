#!/usr/bin/python3
"""
    1-top_ten.py
"""
import requests


def top_ten(subreddit):
    """
        top_ten
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'UA'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for post in range(10):
            print(data.get
                  ('data').get('children')
                  [post].get('data').get('title'))
    else:
        print ("None")
