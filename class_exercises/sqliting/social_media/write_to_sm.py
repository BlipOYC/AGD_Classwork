import sqlite3

conn = sqlite3.connect('social_media')
cursor = conn.cursor()

parameterized_insert_user_query = """
INSERT INTO
    users (name, age, gender, nationality)
VALUES
    (?, ?, ?, ?);
"""

people = [('James', 25, 'male', 'USA'),
          ('Leila', 32, 'female', 'France'),
          ('Brigitte', 35, 'female', 'England'),
          ('Mike', 40, 'male', 'Denmark'),
          ('Elizabeth', 21, 'female', 'Canada'),
          ]

#conn.executemany(parameterized_insert_query, people)

posts = [('Happy', 'I am feeling very happy today', 1),
         ('Hot Weather', 'The weather is very hot today', 2),
         ('Help', 'I need some help with my work', 2),
         ('Great News', 'I am getting married', 1),
         ('Interesting Game', 'It was a fantastic game of tennis', 5),
         ('Party', 'Anyone up for a late-night party today?', 3),
         ]

parameterized_insert_posts_query = """
INSERT INTO
    posts(title, description, user_id)
VALUES
    (?, ?, ?);
"""

#conn.executemany(parameterized_insert_posts_query, posts)

comments = [('Count me in', 1, 6),
            ('What sort of help?', 5, 3),
            ('Congrats buddy', 2, 4),
            ('I was rooting for Nadal though', 4, 5),
            ('Help with your thesis?', 2, 3),
            ('Many congratulations', 5, 4),]

parameterized_insert_comments_query = """
INSERT INTO
    comments()
VALUES
    (?, ?, ?);
"""

conn.commit()
conn.close()