#!/usr/bin/python3
"""
A function that queries the reddit api and return the number of subscribers
for a given subredit
"""

import requests


def number_of_subscribers(subreddit):
    """FUNCTION TO RETURN THE NUMBER OF SUBSCIBERS FOR A GIVEN SUBREDDIT"""
    base_Url = "https://www.reddit.com/"
    user_Url = f"{base_Url}/r/{subreddit}/about.json"

    user_agent = {"User-Agent": "Alx/advanced"}

    response = requests.get(user_Url, headers=user_agent,
                            allow_redirects=False, timeout=10)

    if response.status_code in [301, 302, 400, 404]:
        return 0

    return response.json().get('data').get("subscribers")

