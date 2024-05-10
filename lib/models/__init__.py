import sqlite3

CONN = sqlite3.connect('mycontacts.sqlite3')
CONN.execute('PRAGMA foreign_keys = 1;') #This doesn't do what it's supposed to do and I dont't know why

CURSOR = CONN.cursor()