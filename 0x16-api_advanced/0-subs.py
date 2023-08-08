#!/usr/bin/python3
""" QUery the Reddit API and returns the number of subscribers for a given subreddit."""

from os import getenv
import praw, prawcore
import requests
from dotenv import load_dotenv
from sys import argv

load_dotenv()
def number_of_subscribers(subreddit):
    
    reddit = praw.Reddit(
        client_id=getenv('CLIENT'),
        client_secret=getenv('SECRET'),
        user_agent=getenv('AGENT')
    )

    try:
        subreddit = reddit.subreddit(subreddit)
        return subreddit.subscribers
    except (prawcore.exceptions.NotFound, prawcore.exceptions.Redirect):
        return 0

if __name__ == "__main__":
    print(number_of_subscribers(argv[1]))