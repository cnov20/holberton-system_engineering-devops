#!/usr/bin/python3

"""
Python script that, using linked to REST API,
for a given employee ID, returns information
about his/her TODO list progress and exports to CSV file.
"""

import csv
import json
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

    data_dict = {}
    data_list = []
    for item in resultsTodos:
        completed = item.get('completed')
        title = item.get('title')
        data_dict[employeeId] = {
                "task": title,
                "completed": completed,
                "username": userName
            }
        data_list.append(data_dict)

        path = employeeId + '.json'
        with open(path, 'w', encoding='utf-8', newline='') as json_file:
            for item in data_list:
                json.dump(data_list, json_file)
