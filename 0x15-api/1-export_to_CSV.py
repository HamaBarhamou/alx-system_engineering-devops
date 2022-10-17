#!/usr/bin/python3
""" Module of Gather data from an API"""


if __name__ == '__main__':
    import csv
    import requests
    import sys

    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(sys.argv[1]))
    EMPLOYEE_NAME = r.json().get('username')
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                     .format(sys.argv[1]))
    reponse = r.json()

    filename = sys.argv[1] + '.csv'
    with open(filename, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for loop in reponse:
            writer.writerow([sys.argv[1], EMPLOYEE_NAME,
                             str(loop.get('completed')),
                             loop.get('title')])
