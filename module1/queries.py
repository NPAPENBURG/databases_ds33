get_name_hp = '''SELECT name, hp
                 FROM charactercreator_character;'''

total_char = '''SELECT COUNT(*)
                FROM charactercreator_character;'''

necro = '''SELECT COUNT(*)
                FROM charactercreator_necromancer;'''

cleric = '''SELECT COUNT(*)
                FROM charactercreator_cleric;'''

fighters = '''SELECT COUNT(*)
                FROM charactercreator_fighter;'''

mages = '''SELECT COUNT(*)
                FROM charactercreator_mage;'''

thief = '''SELECT COUNT(*)
                FROM charactercreator_thief;'''

total_subchar = '''SELECT COUNT(*)
                FROM charactercreator_necromancer;'''

total_item = '''SELECT COUNT(*)
                FROM armory_item;'''

total_weapons = '''SELECT COUNT(*)
                FROM armory_weapon;'''

total_non_weapon = '''SELECT armory_item.item_id
                        FROM armory_item LEFT JOIN armory_weapon
                        ON armory_item.item_id = armory_weapon.item_ptr_id
                        WHERE armory_weapon.item_ptr_id IS NULL;'''

char_items = '''SELECT COUNT(*)
                FROM charactercreator_character_inventory
                GROUP BY character_id
                LIMIT 20;'''

char_weapons = '''SELECT count(item_ptr_id)
                  FROM charactercreator_character_inventory
                  LEFT JOIN armory_weapon
                  ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
                  GROUP BY character_id;'''

avg_items = '''
        SELECT
            AVG(count_id)
        FROM
        (
            SELECT COUNT(id) count_id
            FROM charactercreator_character_inventory
            GROUP BY character_id
        )'''

avg_weap = '''
        SELECT
	        AVG(count_id)
        FROM
        (
	    SELECT character_id, COUNT(item_ptr_id) count_id 
	        FROM charactercreator_character_inventory AS inventory
	        LEFT JOIN armory_weapon AS weapons
	        ON inventory.item_id = weapons.item_ptr_id
	        GROUP BY character_id
        )'''