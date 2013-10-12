#!/usr/bin/env python

# this code demonstarates python can  be use to connect to mysql
# the databse api of python lets u connect to different databses
# like sqlite3, postresql, mongoDB etc.
# eg.
# import sqlite3
# db=sqlite3.connect('name of database')

import MySQLdb


''' the connect function is used get a handle to the db, it takes the
    following shown arguments '''

db = MySQLdb.connect(
  host = 'localhost', # ip
  user = 'root',
  passwd = 'root',
  db = 'security' #name of database to connect to
)

# on the db handle we create a cursor on which we can execute any sql query

cursor = db.cursor()  # creating cursor

# To exectute aquery on the db we use cursor.execute(the sql command to execute)
# basically we can execute any sql query through for eg, INSERT, DELETE, UPDATE etc.
cursor.execute('show tables')

# and to fetch the results
results = cursor.fetchall()

