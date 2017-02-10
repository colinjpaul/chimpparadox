import json
import sqlite3

conn = sqlite3.connect('test_db.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE Counts (
    count    INTEGER,
    org      TEXT
)
''')
    
