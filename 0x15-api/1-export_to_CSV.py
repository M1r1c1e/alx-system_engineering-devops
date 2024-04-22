#!/usr/bin/python3
"""Returns to-do list information for a given employee ID and exports it to CSV."""
import requests
import sys
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    # Fetch user's information
    user_response = requests.get("{}users/{}".format(url, employee_id))
    user_data = user_response.json()

    # Fetch user's tasks
    tasks_response = requests.get("{}users/{}/todos".format(url, employee_id))
    tasks_data = tasks_response.json()

    # Filter completed tasks and prepare data for CSV
    completed_tasks = []
    for task in tasks_data:
        if task.get("completed"):
            completed_tasks.append([employee_id, user_data["username"], "Completed", task["title"]])

    # Save data to CSV file
    filename = f"{employee_id}.csv"
    with open(filename, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csv_writer.writerows(completed_tasks)

    print(f"Data exported to {filename}")

