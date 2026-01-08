import sqlite3
from faker import Faker
fake = Faker('en_GB')
from random import randint, choice

conn = sqlite3.connect('student.sqlite')
cursor = conn.cursor()

parameterized_insert_query = """
INSERT INTO
    students (first_name, last_name, age, gender)
VALUES 
    (?, ?, ?, ?);
"""





student_data = []

for _ in range(100):
    first_name = fake.first_name()
    last_name = fake.last_name()
    age = randint(11, 18)
    gender = choice(['Male', 'Female'])
    student_data.append((first_name, last_name, age, gender))

conn.executemany(parameterized_insert_query, student_data)


conn.commit()
conn.close()