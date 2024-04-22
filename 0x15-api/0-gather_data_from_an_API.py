#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    name = requests.get("{}users/{}".format(url, sys.argv[1])).json()
    tasks = requests.get("{}users/{}/todos".format(url, sys.argv[1])).json()
    com_tasks = []
    for task in tasks:
        if task.get("completed") is True:
            com_tasks.append(task)

    titles = []
    for task in tasks:
        if task.get("completed") is True:
            titles.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):"
            .format(name.get("name"), len(com_tasks), len(tasks)))
    for title in titles:
        print("\t {}".format(title))
