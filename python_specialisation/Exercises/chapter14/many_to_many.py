import _sqlite3

conn = sqlite3.connect('many_many.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS USER;
DROP TABLE IF EXISTS COURSE;
DROP TABLE IF EXISTS MEMBER;

CREATE TABLE User (
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT
    email   TEXT
)

CREATE TABLE Course (
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title   TEXT
)

CREATE TABLE  Member(
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)

)


''')
