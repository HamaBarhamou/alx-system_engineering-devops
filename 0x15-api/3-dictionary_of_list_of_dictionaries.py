#!/usr/bin/python3
""" Module of Gather data from an API"""


from urllib import response

from html2text import ListElement


if __name__ == '__main__':
    import json
    import requests
    import sys

    r = requests.get('https://jsonplaceholder.typicode.com/users/')
    LISTE_USR = r.json()
    dic = {}
    for usr in LISTE_USR:
        id = usr.get('id')
        res = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}/todos'
                .format(id))
        data = res.json()
        tab = []
        for loop in data:
            js = {}
            js["username"] = usr.get('username')
            js["task"] = loop.get('title')
            js["completed"] = loop.get("completed")
            tab.append(js)
        dic[id] = tab

    filename = 'todo_all_employees.json'
    with open(filename, 'w') as mon_fichier:
        json.dump(dic, mon_fichier)
