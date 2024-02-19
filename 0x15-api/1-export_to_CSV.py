#!/usr/bin/python3
"""
Retrieve TODO list progress for a given employee
ID from a REST API and export to CSV.
"""

import csv
import requests
import sys


def export_to_csv(employee_id):
    """
    Retrieve TODO list progress for the specified
    employee ID and export to CSV.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        """ To fetch user information"""
        user_response = requests.get(user_url)
        user_data = user_response.json()
        user_id = user_data.get("id")
        username = user_data.get("username")

        """ To fetch TODO list information"""
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        """ Prepare CSV data"""
        csv_data = []
        for task in todos_data:
            task_completed_status = str(task.get("completed"))
            task_title = task.get("title")
            csv_data.append([str(user_id), username, task_completed_status, task_title])

        """ Export to CSV file"""
        filename = f"{user_id}.csv"
        with open(filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            csv_writer.writerows(csv_data)

        print(f"Data exported to {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)
