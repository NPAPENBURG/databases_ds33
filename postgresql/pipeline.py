'''File to Migreate sqlite db to postgresql'''

import psycopg2
from queries import *
import sqlite3

#Connect to Progres DB
DBNAME = 'qvtvylrj'
USER = 'qvtvylrj'
PASSWORD = 'XNVQvnkr3isj_LowPsWek15jG1RhjujB'
HOST = 'castor.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
pg_curs = pg_conn.cursor()

# Connect to SQLite DB
sl_conn = sqlite3.connect('rpg_db.sqlite3')
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


if __name__ == '__main__':
    # execute_query(pg_curs, pg_conn, create_table)
    # execute_query(pg_curs, pg_conn,  insert_data)
    # execute_query(pg_curs, pg_conn, select_all)
    # print(execute_query(sl_curs, sl_conn, get_characters))

    # Get Chars from SQLite
    characters = execute_query_sl(sl_curs, sl_conn, get_characters)
    #print(characters)

    # Make the Postgres tables
    execute_query_pg(pg_curs, pg_conn, create_char_table)

    # Take Character data and insert into Postgres DB
    for character in characters:
        insert_statement = '''
            INSERT INTO charactercreator_character (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
            VALUES {};
            '''.format(character[1:])
        execute_query_pg(pg_curs, pg_conn, insert_statement)