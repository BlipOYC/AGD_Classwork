import sqlalchemy as sa
import sqlalchemy.orm as so

from models import User, Post, Comment


class Controller:
    def __init__(self, db_location = 'sqlite:///social_media.db'):
        self.current_user_id: int|None = None
        self.viewing_post_user_id: int|None = None
        self.engine = sa.create_engine(db_location)

    def set_current_user_from_name(self, name:str) -> User|None:
        with so.Session(bind=self.engine) as session:
            user = session.scalars(sa.select(User).where(User.name == name)).one_or_none()

            if user is None:
                # Fallback behaviour: clear current user and return None
                self.current_user_id = None
                return None

            self.current_user_id = user.id
        return user

    def get_user_name(self, user_id: int|None = None) -> 'str':
        if user_id is None:
            user_id = self.current_user_id
        with so.Session(bind=self.engine) as session:
            name = session.get(User, user_id).name
        return name

    def get_user_names(self) -> list[str]:
        with so.Session(bind=self.engine) as session:
            user_names = session.scalars(sa.select(User.name).order_by(User.name)).all()
        return list(user_names)

    def make_user(self, name, age, gender, nationality):
        with so.Session(bind=self.engine) as session:
            new_user = User(name=name, age=age, gender=gender, nationality=nationality)
            session.add(new_user)
            session.commit()

    def make_post(self, title, description):
        with so.Session(bind=self.engine) as session:
            post = Post(title=title, description=description, user_id=self.current_user_id)
            session.add(post)

    def make_comment(self, text):
        with so.Session(bind=self.engine) as session:
            comment = Comment(text=text, user_id=self.current_user_id)
            session.add(comment)

    def get_some_posts(self):
        with so.Session(bind=self.engine) as session:
            posts = list(session.scalars(sa.select(Post).order_by(Post.id)).all())
        return posts[::-1][:3]

    def get_specific_post(self, post_id):
        with so.Session(bind=self.engine) as session:
            pass



if __name__ == '__main__':
    controller = Controller()
    controller.set_current_user_from_name('Alice')