import psycopg2 as pg2
import sqlite3 as sql
import pymongo


password = '2516'
dbname = 'charactercreator_characters'

client = pymongo.MongoClient(
    "mongodb+srv://npap:{}@cluster0.l0gka.mongodb.net/{}}?retryWrites=true&w=majority"
    .format(password, dbname))


sql_conn = sql.connect("rpg_db.sqlite3")
curs = sql_conn.cursor()

db = client.charactercreator_characters
collection = db.character_table


""" Fetching the three relevant tables from the SQLite database """

char_traits = curs.execute('SELECT * FROM charactercreator_character').fetchall()
char_items = curs.execute('SELECT * FROM charactercreator_character_inventory').fetchall()
char_weapons = curs.execute('SELECT * FROM armory_weapon').fetchall()


"""Creating a list of all the items that are classified as weapons"""

weapons = []

for w in char_weapons:
    weapons.append(w[0])


"""
Creating expanded character documents that includes character items and weapons. Note that instead of 'insert_one' 
we could append each dictionary to a list (expanded_char below) and use 'insert_many'
"""

# expanded_char = []

for w in char_traits:
    key = w[0]
    
    char_bag = []
    char_weapons = []
    
    for item in char_items:
        if item[1] == key:
            char_bag.append(item)
            
    for poss in char_bag:
        if poss[2] in weapons:
            char_weapons.append(item)
            
    character_doc = {
        "name" : w[1],
        "level" : w[2],
        "exp" : w[3],
        "hp" : w[4],
        "strength" : w[5],
        "intelligence" : w[6],
        "dexterity" : w[7],
        "wisdom" : w[8],
        "items" : char_bag,
        "weapons" : char_weapons
    }
    
    collection.insert_one(character_doc)
    

    '''
It was more difficult to work with MongoDB because the info I needed to collate related data was nested inside of unrelated data. 
Instead of being able to access and match keys using straightforward declarative language, 
I had to think of how to access and match keys using for-loops to build the documents I wanted to insert. 
MongoDB requires more coding know-how and more effort to decode and encode different documents as needed.

Unfortunately I ran the above cell twice so now I have duplicate documents in my collection, 
but I'll figure it out. It's a good incentive to consult the docs.
    '''