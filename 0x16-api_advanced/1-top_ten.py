#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.
'''

import requests
import sys
"""
This program will find and print the no of subscribers in a specified
reddit subreddit
"""


def top_ten(subreddit):
    """
    Calls and formats a stribng from a json result
    """
    url = "https://www.reddit.com"
    params = {"limit": "10"}
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get('{}/r/{}/hot.json'
                            .format(url, subreddit),
                            headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        # print("call successful")
        # print(response.json)
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        for post in posts:
            post_data = post.get('data', {})
            title = post_data.get('title')
            score = post_data.get('score')
            permalink = post_data.get('permalink')
            url = post_data.get('url')
            print("Title: {}\nScore: {}\nURL:{}\nPermalink: {}\n"
                  .format(title, score, url, permalink))

        else:
            print("Unexpected JSON structure")
            return 0

    else:
        print("Err code: ", response.status_code)
        return 0

if __name__ == '__main__':
    top_ten = __import__('1-top_ten').top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
