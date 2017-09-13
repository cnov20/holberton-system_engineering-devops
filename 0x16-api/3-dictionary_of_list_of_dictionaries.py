#!/usr/bin/python3

"""
Python script that, using linked to REST API,
for a given employee ID, returns information
about his/her TODO list progress and exports to JSON file.
"""

import csv
import json
import requests
from sys import argv


if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com'
    tasks = '/todos'
    users = '/users'
    fullPathUsers = url + users
    fullPathTodos = url + tasks
    reqUsers = requests.get(fullPathUsers)
    reqTodos = requests.get(fullPathTodos)
    resultsUsers = reqUsers.json()
    resultsTodos = reqTodos.json()

    data_dict = {}
    data_list = []
    for user in resultsUsers:

        for item in resultsTodos:
            employeeId = item.get('userId')
            userName = item.get('username')
            completed = item.get('completed')
            title = item.get('title')
            data_dict[employeeId] = {
                "task": title,
                "completed": completed,
                "username": userName
            }
            data_list.append(data_dict)

        path = 'todo_all_employees.json'
        with open(path, 'w', encoding='utf-8', newline='') as json_file:
            for item in data_list:
                json.dump(data_list, json_file)
