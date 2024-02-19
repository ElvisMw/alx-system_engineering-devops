#!/usr/bin/python3
"""
Export tasks of a specific employee to a CSV file.
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = argv[1]

    """ API endpoint for tasks"""
    api_url = "https://jsonplaceholder.typicode.com/todos"

    """" Retrieve tasks from the API"""
    response = requests.get(api_url, params={"userId": employee_id})
    tasks = response.json()

    """ CSV file name"""
    csv_filename = "{}.csv".format(employee_id)

    """ Write tasks to CSV"""
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        """ Write header"""
        writer.writeheader()

        """ Write tasks"""
        for task in tasks:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": task["title"].split()[0],
                "TASK_COMPLETED_STATUS": str(task["completed"]),
                "TASK_TITLE": task["title"]
            })

    print("Tasks exported to {}".format(csv_filename))
