#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.
'''

import requests
import sys
"""
This program will find and print the no of subscribers in a specified
reddit subreddit
"""


def number_of_subscribers(subreddit):
    """
    Calls and formats a stribng from a json result
    """
    url = "https://www.reddit.com"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get('{}/r/{}/about.json'
                            .format(url, subreddit),
                            headers=headers, allow_redirects=False)

    if response.status_code == 200:
        # print("call successful")
        # print(response.json)
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            print("Unexpected JSON structure")
            return 0
    else:
        if response.status_code == 404:
            print("OK")
        # print("Err code: ", response.status_code)
        return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
