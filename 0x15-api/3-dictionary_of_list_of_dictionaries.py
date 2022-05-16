#!/usr/bin/python3
"""
    Gather data from an API
"""
import json
import requests
from sys import argv
from urllib import response


if __name__ == "__main__":
    User = (requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )).json()
    todos = (requests.get(
        "https://jsonplaceholder.typicode.com/todos"
    )).json()

    file = "todo_all_employees" + ".json"
    users = {}

    for user in User:
        list = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                Dict = {"username": user.get("username"),
                        "task": task.get("title"),
                        "completed": task.get("completed")}
                list.append(Dict)
        users[user.get('id')] = list

    with open(file, "w") as f:
        json.dump(users, f)
