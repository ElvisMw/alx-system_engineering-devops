#!/usr/bin/python3
"""
100-count
"""
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursive function that queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords.

    Args:
    - subreddit (str): The name of the subreddit.
    - word_list (list): List of keywords to count.
    - after (str): The 'after' parameter for pagination (default is None).
    - counts (dict): Dictionary to store the counts of each keyword (default is None).

    Returns:
    - None: Prints the sorted count of keywords.
    """
    if counts is None:
        counts = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-Agent': 'my-app/0.0.1'}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json().get('data')
        children = data.get('children')

        # Extract titles and count keyword occurrences
        for child in children:
            title = child.get('data').get('title').lower()
            for word in word_list:
                word_lower = word.lower()
                if word_lower in title:
                    counts[word_lower] = counts.get(word_lower, 0) + title.count(word_lower)

        # Recursive call with the 'after' parameter for pagination
        after = data.get('after')
        if after:
            count_words(subreddit, word_list, after, counts)

    # Print the sorted count of keywords
    if after is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for keyword, count in sorted_counts:
            print("{}: {}".format(keyword, count))
