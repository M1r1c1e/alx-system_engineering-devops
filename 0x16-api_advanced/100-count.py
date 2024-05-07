#!/usr/bin/python3
"""a recursive function that queries the Reddit API, parses the title of all hot articles, 
and prints a sorted count of given keywords (case-insensitive, delimited by spaces
"""
import requests


def count_words(subreddit, word_list, array=None, after=""):
    if array is None:
        array = {}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after}
    data = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)

    if data.status_code == 200:
        results = data.json().get("data")
        after = results.get("after")

        for entry in results.get("children"):
            split = entry.get("data").get("title").lower().split()

            for word in word_list:
                if word.lower() in split:
                    times = len([t for t in split if t == word.lower()])
                    if array.get(word) is None:
                        array[word] = times
                    else:
                        array[word] += times

        if after:
            count_words(subreddit, word_list, array, after)
        else:
            sorted_results = sorted(array.items(), key=lambda x: (-x[1],
                                    x[0].lower()))
            for word, count in sorted_results:
                print("{}: {}".format(word.lower(), count))
