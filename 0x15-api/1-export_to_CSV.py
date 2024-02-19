#!/usr/bin/python3
"""
Retrieve TODO list progress for a given employee ID from a 
REST API and export to CSV.
"""

import csv
import requests
import sys


def get_todo_progress(employee_id):
    """
    Retrieve TODO list progress for the specified employee ID.
    Export data to CSV with format: "USER_ID","USERNAME",
    "TASK_COMPLETED_STATUS","TASK_TITLE".
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch user information
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get("name")

        # Fetch TODO list information
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Calculate progress
        total_tasks = len(todos_data)
        completed_tasks = [task for task in todos_data if task.get("completed")]
        num_completed_tasks = len(completed_tasks)

        # Display progress
        print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task.get('title')}")

        # Export to CSV
        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for task in todos_data:
                csv_writer.writerow([employee_id, employee_name, str(task.get('completed')), task.get('title')])

        print(f"Data exported to {csv_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_progress(employee_id)
