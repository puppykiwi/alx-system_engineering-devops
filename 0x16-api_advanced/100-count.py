#!/usr/bin/python3
"""Module that consumes the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit."""


import praw
import prawcore
from os import getenv
from dotenv import load_dotenv
load_dotenv()


def count_words(subreddit_name, word_list, word_counts=None, after=None):
    if word_counts is None:
        word_counts = {}

    reddit = praw.Reddit(
    
        client_id=getenv("CLIENT"),
        client_secret=getenv('SECRET'),
        user_agent=getenv('AGENT')
    )
    
    try:
        subreddit = reddit.subreddit(subreddit_name)
        hot_posts = subreddit.hot(limit=None, params={'after': after})
        
        for post in hot_posts:
            title_words = post.title.lower().split()
            for word in word_list:
                if word.lower() in title_words:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1

        if hot_posts.params.get('after'):
            return count_words(subreddit_name, word_list, word_counts, after=hot_posts.params['after'])
        else:
            sorted_counts = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    except (prawcore.exceptions.NotFound, prawcore.exceptions.Redirect):
        return None

if __name__ == "__main__":
    subreddit_name = "kenya"  # Replace with your desired subreddit
    keywords = ["python", "javascript", "java"]  # Replace with your desired keywords
    count_words(subreddit_name, keywords)
