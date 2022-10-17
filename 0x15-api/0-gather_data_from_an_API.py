#!/usr/bin/python3

if __name__ == '__main__':
    import requests
    import sys

    r = requests.get('https://jsonplaceholder.typicode.com/todos/{}'.format(sys.argv[1]))
    print(r.json)
    pass