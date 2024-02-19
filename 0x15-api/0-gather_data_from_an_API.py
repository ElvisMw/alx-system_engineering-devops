#!/usr/bin/python3
"""
Retrieve TODO list progress for a given employee ID from a REST API.
"""

import requests
import sys


def get_todo_progress(employee_id):
    """
    Retrieve and display TODO list progress for the specified employee ID.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        """ To fetch user information"""
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get("name")

        """ To fetch TODO list information"""
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        """ Calculate progress"""
        total_tasks = len(todos_data)
        completed_tasks = [
            task for task in todos_data if task.get("completed")]
        num_tasks = len(completed_tasks)

        """ Display progress"""
        first_line = "Employee {} done tasks({}/{}):".format(employee_name, num_tasks, total_tasks)
        print(first_line)
        for task in completed_tasks:
            print(f"\t{task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_progress(employee_id)
