#!/usr/bin/python3
"""
Script that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.

Requirements:
- Prototype: def top_ten(subreddit)
- If not a valid subreddit, print None.
- Invalid subreddits may return a redirect to search results.
  Ensure that you are not following redirects.
"""

import requests

def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit.

    Returns:
    - None: If the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    """Check if the request was successful (status code 200)"""
    if response.status_code == 404:
        print("None")
        return

    """ Extract the results from the response"""
    results = response.json().get("data")

    """Print titles of the first 10 hot posts"""
    [print(c.get("data").get("title")) for c in results.get("children")]

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

