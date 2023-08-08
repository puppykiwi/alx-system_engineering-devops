#!/usr/bin/python3
"""Module that consumes the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit."""


import requests


def count_words(subreddit_name, word_list, word_counts=None, after=None):
    if word_counts is None:
        word_counts = {}
    
    base_url = f"https://www.reddit.com/r/{subreddit_name}/hot.json"
    params = {"limit": 100, "after": after, "allow_redirects": False}
    headers = {'user-agent': 'custom'}

    response = requests.get(base_url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        children = data.get("data", {}).get("children", [])

        for child in children:
            title = child.get("data", {}).get("title", "").lower()
            print(title) #debug
            for word in word_list:
                if word.lower() in title:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1

        after = data.get("data", {}).get("after")
        if after:
            return count_words(subreddit_name, word_list, after, word_counts)
        else:
            sorted_counts = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    elif response.status_code == 404 or response.status_code == 302:
        return None


if __name__ == "__main__":
    subreddit_name = "kenya"
    keywords = ["python"]
    count_words(subreddit_name, keywords)

