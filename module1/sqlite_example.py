# Step 0 - import sqlite3
import sqlite3
import queries as q



# DB CONNECTION
def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    results = curs.fetchall()
    return results


if __name__ == '__main__':
    conn = connect_to_db()
    results = execute_q(conn, q.char_items)
    print(results)





# #### EVERYTHING UNDER IS THE LONG WAY OF DOING THIS ###

# # Step 1 - Make a Connection to the database
# # TRIPLE CHECK THE SpELLING OF DB NAME
# connection = sqlite3.connect('rpg_db.sqlite3')

# #  Step 2 - Make the "cursor"
# cursor = connection.cursor()

# # Step 3 - Write a Query
# # Needs to be a string
# # need to end in a semicoln
# # query = '''SELECT name, hp
# #            FROM charactercreator_character;'''

# # Step 4 - Execture the query on the cusor
# # Gets the data from DB, but doesn't show it
# cursor.execute(q.get_name_hp)

# # Step 5 - Pull the results from the cursor
# results = cursor.fetchall()

# if __name__ == '__main__':
#     print(results[:5])