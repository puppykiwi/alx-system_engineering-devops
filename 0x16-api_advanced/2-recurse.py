#!/usr/bin/python3

import requests
import sys

def recurse(subreddit, counter):
    url = "https://www.reddit.com/r/{subreddit}/hot.json"
    params = 

    posts = data.get('data', {}).get('children', [])  # Extract posts
    after = data.get('data', {}).get('after')


if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
