'''File to Migreate sqlite db to postgresql'''

import psycopg2
from queries import *
import sqlite3
import pandas as pd
import csv

#Connect to Progres DB
DBNAME = 'qvtvylrj'
USER = 'qvtvylrj'
PASSWORD = 'XNVQvnkr3isj_LowPsWek15jG1RhjujB'
HOST = 'castor.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
pg_curs = pg_conn.cursor()

# Connect to SQLite DB
sl_conn = sqlite3.connect('passenger9.sqlite3')
sl_curs = sl_conn.cursor()


def execute_query_pg(curs, conn, query):
    ''' Function to run querys on postgresql database'''
    results = curs.execute(query)
    conn.commit()
    return results

def execute_query_sl(curs, conn, query):
    ''' Function to run querys on postgresql database'''
    results = curs.execute(query).fetchall()
    return results

# Query to create a table
schema = """CREATE TABLE "passengers9" (
    "Survived" INT,
    "Pclass" INT,
    "Name" TEXT,
    "Sex" TEXT,
    "Age" NUMERIC(4, 2),
    "Siblings_Spouses_Aboard" INT,
    "Parents_Children_Aboard" INT,
    "Fare" NUMERIC(7, 4)
);"""


get_passengers = '''SELECT * FROM passengers9;'''


# CONVERTED THE CSV FILE TO AN SQLITE3 DB
df = pd.read_csv('titanic.csv')
df.to_sql('passengers9', con=sl_conn)



if __name__ == '__main__':
    passengers = execute_query_sl(sl_curs, sl_conn, get_passengers)
    # Get Chars from SQLite

    # Make the Postgres tables
    execute_query_pg(pg_curs, pg_conn, schema)

    # Take Character data and insert into Postgres DB
    with open('titanic.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        parsed = ((int(row[0]),
              int(row[1]),
              row[2].replace("'", '"'),  # Swap out the quote types
              row[3],
              float(row[4]),
              int(row[5]),
              int(row[6]),
              float(row[7]))
              for row in reader
              )
        for row in parsed:
            insert_result = """INSERT INTO "passengers9" VALUES""" + str(row) + ';'
            pg_curs.execute(insert_result)
        execute_query_pg(pg_curs, pg_conn, insert_result)
        