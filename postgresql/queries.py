'''Queries for interacting with our SQLite and PostgreSQL databases'''

# Queries to test our connection and ability to create and insert into tables
create_table = '''
CREATE TABLE IF NOT EXISTS table3 (
        id SERIAL PRIMARY KEY,
        name VARCHAR(40) NOT NULL,
        number INT
    );
'''

insert_data = '''
INSERT INTO table3 (name, number)
VALUES ('a row name', 5), ('another row', 72);
'''

select_all = '''SELECT * FROM table3;'''



# +++_________________________________________________________________++++
# Getting Character data from SQLite
get_characters = '''
SELECT * FROM charactercreator_character;
'''

# Get Table info from charactercreator_character
get_characters_table = '''
PRAGMA table_info(charactercreator_character);
'''
# Create a Postgres table with the same schema as charactercreator_character
create_char_table = '''
CREATE TABLE IF NOT EXISTS charactercreator_character(
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    level INT NOT NULL,
    exp INT NOT NULL,
    hp INT NOT NULL,
    strength INT NOT NULL,
    intelligence INT NOT NULL,
    dexterity INT NOT NULL,
    wisdom INT NOT NULL
);
'''
