import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.orm import Mapped

from models import User, Post, Comment


class Controller:
    def __init__(self, db_location='sqlite:///social_media.db'):
        self.current_user_id: int | None = None
        self.viewing_post_user_id: int | None = None
        self.engine = sa.create_engine(db_location)

    def set_current_user_from_name(self, name: str) -> User | None:
        with so.Session(bind=self.engine) as session:
            user = session.scalars(sa.select(User).where(User.name == name)).one_or_none()

            if user is None:
                # Fallback behaviour: clear current user and return None
                self.current_user_id = None
                return None

            self.current_user_id = user.id
        return user

    def get_user_name(self, user_id: int | None = None) -> 'str':
        if user_id is None:
            user_id = self.current_user_id
        with so.Session(bind=self.engine) as session:
            name = session.get(User, user_id).name
        return name

    def get_user_info(self, user_id: int | None = None):
        if user_id is None:
            user_id = self.current_user_id
        with so.Session(bind=self.engine) as session:
            info = session.get(User, user_id)
        return {"Name": info.name,
                "Age": info.age,
                "Gender": info.gender,
                "Nationality": info.nationality
            }

    def get_user_names(self) -> list[str]:
        with so.Session(bind=self.engine) as session:
            user_names = session.scalars(sa.select(User.name).order_by(User.name)).all()
        return user_names

    def make_user(self, name, age, gender, nationality):
        with so.Session(bind=self.engine) as session:
            new_user = User(name=name, age=age, gender=gender, nationality=nationality)
            session.add(new_user)
            session.commit()

    def make_post(self, title, description):
        with so.Session(bind=self.engine) as session:
            post = Post(title=title, description=description, user_id=self.current_user_id)
            session.add(post)
            session.commit()

    def make_comment(self, text, post_id):
        with so.Session(bind=self.engine) as session:
            comment = Comment(comment=text, user_id=self.current_user_id, post_id=post_id)
            session.add(comment)
            session.commit()

    def get_post_information(self):
        with so.Session(bind=self.engine) as session:
            posts = session.scalars(sa.select(Post).order_by(Post.id)).all()
            post_information = []
            for post in posts:
                post_info = {'title': post.title, 'description': post.description, 'post_id': post.id}
                post_information.append(post_info)
        return post_information

    def get_specific_post(self, post_id):
        if post_id is None:
            raise ValueError
        with so.Session(bind=self.engine) as session:
            post = session.scalars(sa.select(Post).where(Post.id == post_id)).one_or_none()
            comments = session.scalars(sa.select(Comment).where(Comment.post_id == post_id)).all()
            post_info = {'title': post.title, 'description': post.description, 'comments': comments}

        return post_info





if __name__ == '__main__':
    controller = Controller()
    controller.set_current_user_from_name('Alice')
    controller.get_user_names()
