#!/usr/bin/python3
"""a recursive function that queries the Reddit API and returns 
a list containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after}
    data = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)

    if data.status_code == 200:
        results = data.json().get("data")
        after = results.get("after")

        for entry in results.get("children"):
            hot_list.append(entry.get("data").get("title"))

        if after:
            return recurse(subreddit, hot_list, after)

        return hot_list

    return None
