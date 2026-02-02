import sqlalchemy as sa
import sqlalchemy.orm as so
from models import User, Post, Comment, Base

engine = sa.create_engine('sqlite:///social_media.db', echo=True)

# Create a session
session = so.Session(bind=engine)

# Create examples of Users
users = [User(name="Alice", age=30, gender="Female", nationality="Canadian"),
         User(name="Bob", age=25, gender="Male", nationality="American"),
         User(name="Charlie", age=28, gender="Male", nationality="British"),
         User(name="Diana", age=22, gender="Female", nationality="Australian"),
         ]

posts = [
    Post(title="This is post 1", description="Testing post 1"),
    Post(title="This is post 2", description="Testing post 2"),
    Post(title="This is post 3", description="Testing post 3"),
]

users[0].liked_posts.append(posts[0])


session.add_all(users)
session.commit()