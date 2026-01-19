import sqlite3

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")


select_users = "SELECT * FROM users"
with sqlite3.connect("social_media") as conn:
    users = execute_read_query(conn, select_users)

for user in users:
    print(user)


select_posts = "SELECT * FROM posts"

with sqlite3.connect("social_media") as conn:
    posts = execute_read_query(conn, select_posts)

for post in posts:
    print(post)

print("--------------------------------------------------")

select_users_posts = """
SELECT
    users.id,
    users.name,
    posts.description
FROM
    posts
    INNER JOIN users ON users.id = posts.user_id
"""


users_posts = execute_read_query(conn, select_users_posts)

for user_post in users_posts:
    print(user_post)

print("--------------------------------------------------")

select_posts_comments_users = """
SELECT
    posts.description as post,
    comments.text as comment,
    users.name
FROM
    posts
    INNER JOIN comments ON posts.id = comments.post_id
    INNER JOIN users ON user_id = comments.user_id
"""

posts_comments_users = execute_read_query(conn, select_users_posts)

for posts_comments_user in posts_comments_users:
    print(posts_comments_user)

print("-------------------------------------------------")

