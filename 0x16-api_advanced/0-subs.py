#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API and returns the number
    of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    """Check if the request was successful (status code 200)"""
    if response.status_code == 200:
        data = response.json()

        """ Check if 'data' and 'subscribers' keys exist in the response"""
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            """ If the structure of the response is unexpected, return 0"""
            return 0
    else:
        """If the subreddit is invalid or any other error occurs, return 0"""
        return 0
