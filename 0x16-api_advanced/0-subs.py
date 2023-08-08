#!/usr/bin/python3
""" QUery the Reddit API and returns the
    number of subscribers for a given subreddit."""

from dotenv import load_dotenv
from os import getenv
import praw
import prawcore
import requests
from sys import argv

load_dotenv()



def number_of_subscribers(subreddit):
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
    subreddit_name = argv[1]  # Replace with your desired subreddit
    subscribers = number_of_subscribers(subreddit="intp")
    print(f"Subreddit '{subreddit_name}' has {subscribers} subscribers.")