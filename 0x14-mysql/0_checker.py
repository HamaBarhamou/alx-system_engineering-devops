#!/usr/bin/python3
"""
SSH into student's servers web-01 and web-02 to verify that
MySQL is installed.
"""
import sys

from fabric import Connection
from paramiko import RSAKey


host = sys.argv[1]
user = sys.argv[2]
rsa_key_file = sys.argv[3]

rsa_key = RSAKey.from_private_key(open(rsa_key_file))

with Connection(host, user=user, connect_kwargs={"pkey": rsa_key}) as c:
    c.run("mysql --version > temp_mysql_v", shell="/bin/bash", warn=False)
    c.run("cat temp_mysql_v | tr -s ' ' | cut -d' ' -f5 | cut -d'.' -f1-2 | tr -d '\n'", shell="/bin/bash", warn=False)