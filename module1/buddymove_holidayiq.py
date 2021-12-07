""" Module to Query a database"""
import sqlite3
import pandas as pd


def connect_to_db(db_name='buddymove_holidayiq.sqlite3'):
    ''' Function to connect to the Database'''
    return sqlite3.connect(db_name)


def execute_q(connection, query):
    ''' Exucute queries using this function'''
    curs = connection.cursor()
    curs.execute(query)
    results = curs.fetchall()
    return results


def create_table(dataframe):
    '''Create a table for the Database'''
    dataframe.to_sql('buddymovie', con=connect_to_db())

# URL TO THE CSV
URL = 'https://raw.githubusercontent.com/bloominstituteoftechnology/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv'

# Reading in the CSV
df = pd.read_csv(URL)

# These lines of code were to make the Database and table
# connect_to_db()
# create_table(df)

# Query string to get the number of rows
RCOUNT = ''' SELECT COUNT(*)
            FROM buddymovie;'''

# Query String to get the number of people who were over 100
NATURE_SHOPPING =  ''' SELECT COUNT(*)
                       FROM buddymovie
                       WHERE nature >= 100 AND shopping >= 100;'''

# Query String to get the averages of the columns
AVERAGES = '''SELECT AVG(sports), AVG(Religious), AVG(Nature),
                     AVG(Theatre), AVG(Shopping), AVG(picnic)
              FROM buddymovie
'''

# Connection to database
conn = connect_to_db()

# Querying the database using the strings
results1 = execute_q(conn, RCOUNT)
results2 = execute_q(conn, NATURE_SHOPPING)
results3 = execute_q(conn, AVERAGES)

#printing the Results
print(f'The number of rows: {results1[0][0]}')
print(f'Total of people who did 100+ for Nature and Shopping: {results2[0][0]}')
print(f'Averages - Sports: {round(results3[0][0], 2)},'
        f'Religious: {round(results3[0][1], 2)}, Nature: {round(results3[0][2], 2)},'
        f'Theatre: {round(results3[0][3], )}, Shopping: {round(results3[0][4], 2)},'
        f'Picnic: {round(results3[0][5], 2)}')
