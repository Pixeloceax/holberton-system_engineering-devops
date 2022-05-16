#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
from sys import argv
from urllib import response


if __name__ == "__main__":

    if len(argv) > 1:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(
                argv[1]
                )
            )
        User = (response.json())
        response = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                argv[1]
            )
        )
        todos = (response.json())

        number_done = 0
        total = 0
        task_done = []

        for task in todos:
            total += 1
            if task.get("completed") is True:
                number_done += 1
                task_done.append(task.get("title"))

        print(
            "Employee {} is done with tasks({}/{}):".format(
                User.get("name"), number_done, total)
            )
        for task in task_done:
            print("\t {}".format(task))
