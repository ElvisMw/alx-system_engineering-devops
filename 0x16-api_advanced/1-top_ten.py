#!/usr/bin/python3
"""
Script that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return

    """ Extract the results from the response"""
    results = response.json().get("data")

    """Print titles of the first 10 hot posts"""
    [print(c.get("data").get("title")) for c in results.get("children")]
