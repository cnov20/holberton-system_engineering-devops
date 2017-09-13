#!/usr/bin/python3

"""
Python script that, using linked to REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""

import csv
import requests
from sys import argv


if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com'
    tasks = '/todos?'
    users = '/users/'
    employeeId = argv[1]
    fullPathUsers = url + users + employeeId
    fullPathTodos = url + tasks + employeeId
    params = {'userId': employeeId}
    reqUsers = requests.get(fullPathUsers)
    resultsUsers = reqUsers.json()
    userName = resultsUsers.get('username')
    reqTodos = requests.get(fullPathTodos, params=params)
    resultsTodos = reqTodos.json()

    data = []
    for item in resultsTodos:
        completed = item.get('completed')
        title = item.get('title')
        data += [employeeId, userName, completed, title]

    path = employeeId + '.csv'
    with open(path, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for item in data:
            writer.writerow([item])
