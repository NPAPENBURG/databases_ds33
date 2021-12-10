""" Part 2 of the Spring Challenge"""

import sqlite3 as sql

conn = sql.connect('northwind_small.sqlite3')
curs = conn.cursor()


def execute_query(connection, query):
    """
    Function written to get answers to the questions asked.
    """
    cursor = connection.cursor()
    results = cursor.execute(query).fetchall()
    return results


expensive_items = """
    SELECT *
    FROM product
    ORDER BY unitprice DESC
    LIMIT 10;"""

avg_hire_age = """
    SELECT AVG(hiredate - birthdate)
    FROM employee;"""

avg_age_by_city = """
    SELECT city, AVG(hiredate - birthdate)
    FROM employee
    GROUP BY city;"""

ten_most_expensive = """
    SELECT productname, unitprice, companyname
    FROM product p
    LEFT JOIN supplier s
    ON p.supplierid = s.id
    ORDER BY unitprice DESC
    LIMIT 10;
"""

largest_category = """
   SELECT catname, COUNT(catname) as total_cat_entries
   FROM (SELECT c.categoryname AS catname
   FROM product p
   LEFT JOIN category c
   ON p.categoryid = c.id) s
   ORDER BY total_cat_entries DESC
   LIMIT 1;
"""

expensive_items = execute_query(conn, expensive_items)
avg_hire_age = execute_query(conn, avg_hire_age)
avg_age_by_city = execute_query(conn, avg_age_by_city)
ten_most_expensive = execute_query(conn, ten_most_expensive)
largest_category = execute_query(conn, largest_category)

print(expensive_items)
print(avg_hire_age)
print(avg_age_by_city)
print(ten_most_expensive)
print(largest_category)

"""ALL MY ANSWERS ARE HERE BELOW

expensives items
[(38, 'Côte de Blaye', 18, 1, '12 - 75 cl bottles', 263.5, 17, 0, 15, 0),
(29, 'Thüringer Rostbratwurst', 12, 6,
'50 bags x 30 sausgs.', 123.79, 0, 0, 0, 1),
(9, 'Mishi Kobe Niku', 4, 6, '18 - 500 g pkgs.', 97, 29, 0, 0, 1),
(20, "Sir Rodney's Marmalade", 8, 3, '30 gift boxes', 81, 40, 0, 0, 0),
(18, 'Carnarvon Tigers', 7, 8, '16 kg pkg.', 62.5, 42, 0, 0, 0),
(59, 'Raclette Courdavault', 28, 4, '5 kg pkg.', 55, 79, 0, 0, 0),
(51, 'Manjimup Dried Apples', 24, 7, '50 - 300 g pkgs.', 53, 20, 0, 10, 0),
(62, 'Tarte au sucre', 29, 3, '48 pies', 49.3, 17, 0, 0, 0),
(43, 'Ipoh Coffee', 20, 1, '16 - 500 g tins', 46, 17, 10, 25, 0),
(28, 'Rössle Sauerkraut', 12, 7, '25 - 825 g cans', 45.6, 26, 0, 0, 1)]

Average Hiring Age
[(37.22222222222222,)]

Average Age by City
[('Kirkland', 29.0), ('London', 32.5), ('Redmond', 56.0),
('Seattle', 40.0), ('Tacoma', 40.0)]

Ten Most Expensive
[('Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques'),
('Thüringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgroßmärkte AG'),
('Mishi Kobe Niku', 97, 'Tokyo Traders'),
("Sir Rodney's Marmalade", 81, 'Specialty Biscuits, Ltd.'),
('Carnarvon Tigers', 62.5, 'Pavlova, Ltd.'),
('Raclette Courdavault', 55, 'Gai pâturage'),
('Manjimup Dried Apples', 53, "G'day, Mate"),
('Tarte au sucre', 49.3, "Forêts d'érables"),
('Ipoh Coffee', 46, 'Leka Trading'),
('Rössle Sauerkraut', 45.6, 'Plutzer Lebensmittelgroßmärkte AG')]

Largest Catergory
[('Beverages', 77)]

"""
