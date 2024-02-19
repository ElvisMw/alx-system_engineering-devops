#!/usr/bin/python3
"""
This Python module (`gather_data_from_an_API.py`) retrieves and
displays information about an employee's
TODO list progress using a REST API.
"""
import requests
from sys import argv


def get_employee_data(employee_id):
    """Fetch user data and calculate progress."""
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get("name")

    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]
    num_completed_tasks = len(completed_tasks)

    return employee_name, num_completed_tasks, total_tasks, completed_tasks


def display_progress(employee_name, num_completed_tasks, total_tasks, completed_tasks):
    """Display progress information."""
    print(f"Employee {employee_name} is done with tasks("
          f"{num_completed_tasks}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = argv[1]
        try:
            employee_name, num_completed_tasks, total_tasks, completed_tasks = get_employee_data(int(employee_id))
            display_progress(employee_name, num_completed_tasks, total_tasks, completed_tasks)
        except ValueError:
            print("Invalid employee ID. Please provide a valid integer.")
