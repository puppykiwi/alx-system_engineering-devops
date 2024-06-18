import sys
import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/subreddit/about"
    
    response = requests.get(url, subreddit)

    if response.status_code == 200:
        print("call successful")
        data = response.json()
        return data
    else:
        print("Er code: ", response.status_code)


if __name__ == '__main__':
    # number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))