#!/usr/bin/python3
""" QUery the Reddit API and returns the number of subscribers for a given subreddit."""

from os import getenv
import praw
import requests
from dotenv import load_dotenv
from sys import argv

load_dotenv()
reddit = praw.Reddit(
    client_id=getenv('CLIENT'),
    client_secret=getenv('SECRET'),
    user_agent=getenv('AGENT')
)

def number_of_subscribers(subreddit):
    subreddit = reddit.subreddit(subreddit)
    if subreddit is None:
        return 0
    return subreddit.subscribers

if __name__ == "__main__":
    print(number_of_subscribers(argv[1]))