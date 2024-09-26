#!/usr/bin/python3
"""
Task 0:
Queries the Reddit API and returns total number of subscribers,
if a subreddit is invalid then it returns 0
0-subs.py
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns:
    Number of subscribers to a subreddit
    or 0 on invalid subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    head = {'user-agent': 'michellegsld-holberton'}
    req = requests.get(url, headers=head, allow_redirects=False)
    try:
        return req.json()['data']['subscribers']
    except:
        return 0
