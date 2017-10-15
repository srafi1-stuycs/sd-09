# Shakil Rafi
# SoftDev1 pd7
# HW09 -- No Treble
# 2017-10-15

import sqlite3   # enable control of an sqlite database
import csv       # facilitates CSV I/O

f='discobandit.db'

db = sqlite3.connect(f) # open if f exists, otherwise create
c = db.cursor()    # facilitate db ops

command = 'CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)'
c.execute(command) # create table
courses = open('courses.csv', 'r')
reader = csv.DictReader(courses)
for row in reader:
    command = 'INSERT INTO courses VALUES ("%s", %s, %s)' % (row['code'], row['mark'], row['id'])
    # print command
    c.execute(command) # add given row to table

command = 'CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER PRIMARY KEY)'
c.execute(command)
peeps = open('peeps.csv', 'r')
reader = csv.DictReader(peeps)
for row in reader:
    command = 'INSERT INTO peeps VALUES ("%s", %s, %s)' % (row['name'], row['age'], row['id'])
    # print command
    c.execute(command)

db.commit() # save changes
db.close()  # close database


