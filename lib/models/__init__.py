import sqlite3

CONN = sqlite3.connect('mycontacts.sqlite3')
CURSOR = CONN.cursor()