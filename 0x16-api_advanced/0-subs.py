#!/usr/bin/python3
""" function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0. """

import requests


def number_of_subscribers(subreddit):
    """function to return the number of subscribers for a given subreddit """
    base_url = "https://www.reddit.com/"
    user_url = f"{base_url}/r/{subreddit}/about.json"

    user_agent = {"User-Agent": "Alx/requests"}

    response = requests.get(user_url, headers=user_agent,
                            allow_redirects=False)

    if response.status_code >= 300:
        return 0

    return response.json().get("data").get("subscribers")
