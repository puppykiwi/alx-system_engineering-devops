#!/usr/bin/python3

import requests
import sys

def recurse(subreddit, count = 0, after = None, limit = 20):

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": limit, "after": after, "count": count}
    all_posts = []

    response = requests.get(url, params)

    if response.status_code == 200:
        print("success")
        data = response.json()
        posts = data.get('data', {}).get('children', []) 
        after = data.get('data', {}).get('after')

        for post in posts:
            post_data = post.get("data", {})
            post_title = post_data.get("title")
            all_posts.append(post_title)
            print (post_title)
            count += 1
        
    else:
        print("Err code: ", response.status_code)

    if after and count < limit:
            all_posts.extend(recurse(subreddit, count, after, limit))

    return all_posts

if __name__ == '__main__':
    # recurse = __import__('2-recurse').recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
