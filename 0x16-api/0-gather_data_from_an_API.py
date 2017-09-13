#!/usr/bin/python3

'''

Python script that, using linked to REST API,
for a given employee ID, returns information
about his/her TODO list progress.

'''

from os import getenv
from sys import argv
import requests
import json

url = 'https://jsonplaceholder.typicode.com'
tasks = '/todos?'
users = '/users/'
employeeID = argv[1]
fullPathUsers = url + users + employeeID
fullPathTodos = url + tasks + employeeID
params = {'userId': employeeID}
reqUsers = requests.get(fullPathUsers)
resultsUsers = reqUsers.json()
name = resultsUsers.get('name')
reqTodos = requests.get(fullPathTodos, params=params)
resultsTodos = reqTodos.json()

print('Employee {} is done with tasks'.format(name), end="")

tasksCompleted = 0
tasksTotal = 0
for item in resultsTodos:
    completed = item.get('completed')
    if completed:
        tasksCompleted += 1
    tasksTotal += 1

print('({}/{}):'.format(tasksCompleted, tasksTotal))

for item in resultsTodos:
    completed = item.get('completed')
    if completed:
        print('\t ', item.get('title'))
