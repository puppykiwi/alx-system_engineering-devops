#!/usr/bin/python3

"""
Using what you did in the task #0,
extend your Python script to export data in the JSON format.

Requirements:
Records all tasks from all employees
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID":
[ {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {
    "username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))
    name = user.json().get('username')
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(user_id))
    todos = todos.json()
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": name} for task in todos]}, jsonfile)
