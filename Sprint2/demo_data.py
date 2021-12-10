"""
Part 1 Sprint Challenge
There are 3 rows.
There are 2 rows with x and y >= 5.
There are 2 unique values in y
"""
import sqlite3 as sql

# Connecting to the SQLite Database and creating the Cursor
CONN = sql.connect('demo_data.sqlite3')
CURS = CONN.cursor()

# List of values to put into the table.
table_values = [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]


def execute_q(connection, query):
    ''' Exucute queries using this function'''
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    connection.commit()
    return results


# Query to create a new table called demo
CREATE_DEMO_TABLE = """
    CREATE TABLE IF NOT EXISTS demo (
        s VARCHAR NOT NULL,
        x INT NOT NULL,
        y INT NOT NULL
        );"""

CURS.execute(CREATE_DEMO_TABLE)

# Query to insert into Demo table
INSERT_INTO_DEMO = """
    INSERT INTO demo (s, x, y)
    VALUES (?, ?, ?)"""

# Adding Values into the table
for values in table_values:
    CURS = CONN.cursor()
    CURS.execute(INSERT_INTO_DEMO, values)
    CONN.commit()


# Quert to get the number of rows
row_count = """
    SELECT COUNT(*)
    FROM demo;"""

# Query to get rows with x and y equal or higher than 5
xy_at_least_5 = """
    SELECT COUNT(*)
    FROM demo
    WHERE x >= 5
    AND y >= 5;"""

# Query to get uniqure/distant y row entries
unique_y = """
    SELECT COUNT(DISTINCT(y))
    FROM demo;"""


if __name__ == '__main__':
    rowcount = execute_q(CONN, row_count)
    xy_atleast_5 = execute_q(CONN, xy_at_least_5)
    unique_y = execute_q(CONN, unique_y)
    print(rowcount)
    print(xy_atleast_5)
    print(unique_y)
