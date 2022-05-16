#!/usr/bin/python3
"""
Gather data from an API
"""
import json
import requests
from sys import argv
from urllib import response


if __name__ == "__main__":

        User = response = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(
                argv[1]
                )
            )
        todos = response = requests.get(
            "https://jsonplaceholder.typicode.com/todos"
            ).json()

        file = argv[1] + ".json"
        user = {}
        list = []

        for task in todos:
            if task.get('userId') == int(argv[1]):
                Dict = {"task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": User.json().get("username")}
                list.append(Dict)
        user[argv[1]] = list

        with open(file, "w") as f:
            json.dump(user, f)
