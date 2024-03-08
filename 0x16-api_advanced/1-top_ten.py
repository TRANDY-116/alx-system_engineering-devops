#!/usr/bin/python3
"""Module for task 1"""


def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""
    import requests

    response = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "Alx/requests"},
                            allow_redirects=False)
    if response.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in response.json().get("data").get("children")]
