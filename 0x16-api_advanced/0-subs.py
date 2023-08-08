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



def number_of_subscribers(subreddit_name):
    user_agent = getenv("AGENT")
    
    url = f"https://www.reddit.com/r/{subreddit_name}/about.json"
    headers = {"User-Agent": user_agent}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0


if __name__ == "__main__":
    subreddit_name = argv[1]  # Replace with your desired subreddit
    subscribers = number_of_subscribers(subreddit_name="intp")
    print(f"Subreddit '{subreddit_name}' has {subscribers} subscribers.")