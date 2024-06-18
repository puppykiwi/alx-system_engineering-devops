#!/usr/bin/python3

import requests
import sys

def number_of_subscribers(subreddit):
    # Calls and formats a stribng from a json result
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers)

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
        print("Er code: ", response.status_code)
        return 0


if __name__ == '__main__':
    # number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
