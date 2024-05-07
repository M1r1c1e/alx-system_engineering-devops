#!/usr/bin/python3
"""querying the Reddit API and 
returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-Agent": "Mozilla/5.0"}

    dataAPI = requests.get(url, headers=header, allow_redirects=False)

    if dataAPI.status_code == 200:
        subscribers = dataAPI.json().get("data").get("subscribers")
        return subscribers
    return 0
