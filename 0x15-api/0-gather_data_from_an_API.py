#!/usr/bin/python3

""" a Python script that, using this REST API,
    for a given employee ID, returns information
    about his/her TODO list progress. """

import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))
    name = user.json().get('name')
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(user_id))
    todos = todos.json()
    completed = [task for task in todos if task.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(completed), len(todos)))
    for task in completed:
        print("\t {}".format(task.get('title')))
