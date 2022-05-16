#!/usr/bin/python3
"""
Gather data from an API
"""
import csv
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
        User = (response.json().get("username"))
        response = requests.get("https://jsonplaceholder.typicode.com/todos")
        todos = (response.json())

    file = argv[1] + ".csv"

    with open(file, "w") as f:
        writer = csv.writer(f,
                            delimiter=",",
                            quotechar='"',
                            quoting=csv.QUOTE_ALL,
                            lineterminator='\n')
        for task in todos:
            if task.get('userId') == int(argv[1]):
                writer.writerow([argv[1], User, str(task.get("completed")),
                                 task.get("title")])
