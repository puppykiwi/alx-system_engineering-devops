#!/usr/bin/python3

import requests
import sys

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    #headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": "10"}
    
    response = requests.get(url, params)

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
            print(f"Title: {title}\nScore: {score}\nURL: {url}\nPermalink: {permalink}\n")
        
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