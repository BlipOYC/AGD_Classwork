import sqlite3
from faker import Faker
fake = Faker('en_GB')
from random import randint, choice

conn = sqlite3.connect('student.sqlite')
cursor = conn.cursor()

j_select_query = """
SELECT * FROM students
WHERE SUBSTRING(first_name, 1, 1) = 'J'
"""

g_select_query = """
SELECT * FROM students
GROUP BY gender
"""


print(cursor.execute(j_select_query).fetchmany(5), end="\n\n")
print(cursor.execute(g_select_query).fetchall())

conn.commit()
conn.close()