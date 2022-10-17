#!/usr/bin/python3
""" Module of Gather data from an API"""

if __name__ == '__main__':
    import requests
    import sys

    EMPLOYEE_NAME = "name"
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(sys.argv[1]))
    EMPLOYEE_NAME = r.json().get('name')
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                     .format(sys.argv[1]))
    reponse = r.json()

    for loop in reponse:
        TOTAL_NUMBER_OF_TASKS += 1
        if loop.get('completed'):
            NUMBER_OF_DONE_TASKS += 1

    print("Employee {} is done with tasks({}/{})".format(
         EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for loop in reponse:
        if loop.get('completed'):
            print("\t ", loop.get('title'))
