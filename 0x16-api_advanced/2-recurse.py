#!/usr/bin/python3

import requests
import sys

def recurse(subreddit, count = 0, after = None, limit = 100, all_posts = None):

    if all_posts is None:
        all_posts = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": limit, "after": after, "count": count}

    response = requests.get(url, params)

    if response.status_code == 200:
        # print("success")
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
            print("\n ** resursing **\n")
            recurse(subreddit, count + len(posts), after, limit)

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
