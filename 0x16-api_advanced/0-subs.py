#!/usr/bin/python3
""" function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0. """

import requests
from requests.exceptions import RequestException

   try:
      # Set custom headers, including a User-Agent
           headers = {
           'User-A
           gent': 'MozillaMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
       }

 for the specified subreddit
       # Make a GET request to the Reddit API for the specified subreddit
       url = f'https://www.reddit.com/r/{subreddit}/about.json'
       response = requests.get(url, headers=headers, allow_redirects=False)
       response.raise_for_status()  # Raise an exception for non-2xx status codes

       # Extract the number of subscribers from the response JSON
       data = response.json()
       if 'data' in data and 'subscribers' in data['data']:
           subscribers = data['data']['subscribers']
           return subscribers
       else:
           return 0  
       
    except RequestException as e:
       # Handle exceptions related to the HTTP request
       print(f"Error: {e}")
       return 0
