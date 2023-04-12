#!/usr/bin/python3
"""Write a script that lists all states from the database"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    #meant to connect database to python file
     db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
