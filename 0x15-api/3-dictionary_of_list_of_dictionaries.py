#!/usr/bin/python3
"""
Export data in the JSON format.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    
    user_response = requests.get(f"{base_url}/users/{user_id}")
    todos_response = requests.get(f"{base_url}/todos?userId={user_id}")

    try:
        user = user_response.json()
        todos = todos_response.json()

        user_id = str(user.get("id"))
        username = user.get("username")

        user_tasks = []

        for task in todos:
            task_data = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            user_tasks.append(task_data)

        all_employees_data = {}

        for user_id in range(1, 11):
            user_response = requests.get(f"{base_url}/users/{user_id}")
            todos_response = requests.get(f"{base_url}/todos?userId={user_id}")

            user = user_response.json()
            todos = todos_response.json()

            username = user.get("username")

            user_tasks = []

            for task in todos:
                task_data = {
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }
                user_tasks.append(task_data)

            all_employees_data[user_id] = user_tasks

        with open("todo_all_employees.json", "w") as json_file:
            json.dump(all_employees_data, json_file)

    except ValueError as e:
        print(f"Error: {e}")
