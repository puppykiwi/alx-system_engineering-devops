#!/usr/bin/python3
""" QUery the Reddit API and returns the top ten hot posts for a given subreddit."""

from os import getenv
import praw
import requests
from dotenv import load_dotenv
from sys import argv

load_dotenv()
def top_ten(subreddit):
    reddit = praw.Reddit(
        client_id=getenv('CLIENT'),
        client_secret=getenv('SECRET'),
        user_agent=getenv('AGENT')
    )

    try:
        subreddit = reddit.subreddit(subreddit)
        for submission in subreddit.hot(limit=10):
            print(submission.title)
    except (prawcore.exceptions.NotFound, prawcore.exceptions.Redirect):
        print(None)

if __name__ == "__main__":
    top_ten(argv[1])