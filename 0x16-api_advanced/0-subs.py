#!/usr/bin/python3
"""
0-subs
"""
import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number
    of subscribers for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'my-app/0.0.1'}

    response = requests.get(url, headers=headers)

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

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
