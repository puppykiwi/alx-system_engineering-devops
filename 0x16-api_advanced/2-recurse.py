#!/usr/bin/python3

"""Module that consumes the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit."""
import requests
from sys import argv


def recurse(subreddit, hot_list=[], after=None):
    """
    Args:
        subreddit (str): subreddit

    Returns:
        int: number of subscribers
    """
    base_url = 'https://www.reddit.com/r/'

    url = '{}{}/about.json'.format(base_url, subreddit)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    results = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )
    if results.status_code == 200:
        return results.json()['data']['subscribers']
    return 0


if __name__ == "__main__":
    print(recurse(argv[1]))
