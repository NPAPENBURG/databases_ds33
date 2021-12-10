Question_1_Query = """
    SELECT survived, COUNT(survived)
    FROM titanic
    GROUP BY survived;
"""

did_not_survive = 545
survived = 342

Question_2_Query = """
    SELECT pclass, COUNT(pclass) as total
    FROM titanic
    GROUP BY pclass;
"""
pclass_1 = 216
pclass_2 = 487
pclass_3 = 184

Question_3_Query = """
    SELECT pclass, survived, COUNT(survived)
    FROM titanic
    GROUP BY pclass, survived
    ORDER BY pclass, survived;
"""

pclass1 = {'dead' : 80, 'alive' : 136}
pclass2 = {'dead': 97, 'alive' : 87}
pclass3 = {'dead' : 368, 'alive' : 119}
    
Question_4_Query = """
    SELECT survived, AVG(age)
    FROM titanic
    GROUP BY survived
    ORDER BY survived;
"""

average_age_died = 30.2
average_age_survived = 28.4

Question_5_query = """
    SELECT pclass, AVG(age)
    FROM titanic
    GROUP BY pclass;
"""

average_age_pclass1 = 38.8
average_age_pclass2 = 25.2
average_age_pclass3 = 30.0

Question_6_query_a = """
    SELECT pclass, AVG(fare)
    FROM titanic
    GROUP BY pclass
    ORDER BY pclass;
"""

average_fare_pclass1 = 84.2
average_fare_pclass2 = 20.7
average_fare_pclass3 = 13.7

Question_6_query_b = """
    SELECT survived, AVG(fare)
    FROM titanic
    GROUP BY survived;
"""

average_fare_survived = 48.4
average_fare_died = 22.2

Question_7_query_a = """
    SELECT pclass, AVG(sibling_or_spouse)
    FROM titanic
    GROUP BY pclass;
"""

average_sibspouse_pclass1 = 0.42
average_sibspouse_pclass2 = 0.4
average_sibspouse_pclass3 = 0.62

Question_7_query_b = """
    SELECT survived, AVG(sibling_or_spouse)
    FROM titanic
    GROUP BY survived;
"""

average_sibspouse_died = 0.56
average_sibspouse_survived = 0.47

Question_8_query_a = """
    SELECT pclass, AVG(parents_or_children)
    FROM titanic
    GROUP BY pclass;
"""

average_parchild_pclass1 = 0.36
average_parchild_pclass2 = 0.38
average_parchild_pclass3 = 0.4

Question_8_query_b = """
    SELECT survived, AVG(parents_or_children)
    FROM titanic
    GROUP BY survived;
"""

average_parchild_died = 0.33
average_parchild_survived = 0.46


Question_9_query = """
    SELECT name, COUNT(name) 
    FROM Titanic 
    GROUP BY name
    HAVING COUNT(name) > 1;
"""

duplicate_names = 'No'