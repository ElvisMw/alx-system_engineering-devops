#!/usr/bin/python3
"""
Retrieve TODO list progress for a given employee ID
from a REST API and export to JSON.
"""

import json
import requests
import sys


def export_to_json(employee_id):
    """
    Retrieve TODO list progress for the specified
    employee ID and export to JSON.
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

        """ Prepare JSON data"""
        json_data = {str(user_id): [{"task": task.get("title"), "completed": task.get("completed"), "username": username} for task in todos_data]}

        """ Export to JSON file"""
        filename = f"{user_id}.json"
        with open(filename, mode='w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4)

        print(f"Data exported to {filename}")

    except requests.exceptions.RequestException as em:
        print(f"Error: {em}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_json(employee_id)
