#!/usr/bin/python3
"""
2-recurse
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit.
    - hot_list (list): List to store the titles of hot articles (default is an empty list).
    - after (str): The 'after' parameter for pagination (default is None).

    Returns:
    - List of titles of hot articles if successful, None otherwise.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-Agent': 'my-app/0.0.1'}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json().get('data')
        children = data.get('children')

        # Extract titles and add them to the hot_list
        titles = [child.get('data').get('title') for child in children]
        hot_list.extend(titles)

        # Recursive call with the 'after' parameter for pagination
        after = data.get('after')
        if after:
            recurse(subreddit, hot_list, after)

        return hot_list
    else:
        # If the subreddit is invalid or any other error occurs, return None
        return None
