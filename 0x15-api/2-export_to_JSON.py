#!/usr/bin/python3
""" Module of Gather data from an API"""


from urllib import response


if __name__ == '__main__':
    import json
    import requests
    import sys

    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(sys.argv[1]))
    EMPLOYEE_NAME = r.json().get('username')
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                     .format(sys.argv[1]))
    reponse = r.json()
    tab = []
    for loop in reponse:
        res = {}
        res["task"] = loop.get('title')
        res["completed"] = loop.get('completed')
        res["user"] = EMPLOYEE_NAME
        tab.append(res)

    filename = sys.argv[1] + '.json'
    data = {sys.argv[1]: tab}
    with open(filename, 'w') as mon_fichier:
        json.dump(data, mon_fichier)
