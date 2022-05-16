#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    user = requests.get(user_url).json()
    TODO = requests.get(todo_url).json()

    number_done = 0
    total = 0
    task_done = []

    for task in TODO:
        total += 1
        if task.get("completed") is True:
            number_done += 1
            task_done.append(task.get("title"))

    sentence = "Employee {} is done with tasks({}/{}):"
    print(sentence.format(user.get("name"), number_done, total))
    for task in task_done:
        print("\t {}".format(task))
