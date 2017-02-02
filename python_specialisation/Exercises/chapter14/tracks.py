import xml.etree.ElementTree as ET
import _sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

#Make tables
cur.execute('''
CREATE TABLE IF NOT EXISTS Artist (
    id INTEGER NOT
''')
