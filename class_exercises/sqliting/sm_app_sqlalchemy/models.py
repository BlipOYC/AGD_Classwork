import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional

class Base(so.DeclarativeBase):
    pass

likes_table = sa.Table(
    'likes',
    Base.metadata,
    sa.Column('user_id', sa.Integer,
              sa.ForeignKey(column='users.id', ondelete='CASCADE'),
              primary_key=True),
    sa.Column('post_id', sa.Integer,
              sa.ForeignKey(column='posts.id', ondelete='CASCADE'),
              primary_key=True),
)

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    age: Mapped[Optional[int]]
    gender: Mapped[Optional[str]]
    nationality: Mapped[Optional[str]]
    liked_posts: Mapped[list["Post"]] = relationship(
        secondary=likes_table,
        back_populates="liked_by_users"
    )
    comments_made: Mapped[List["Comment"]] = so.relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )


    def __repr__(self):
        return f"User(name='{self.name}', age={self.age}, gender={self.gender}, nationality={self.nationality})"

class Post(Base):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(index=True)
    description: Mapped[str] = mapped_column(index=True)
    liked_by_users: Mapped[List[User]] = relationship(
        secondary=likes_table,
        back_populates="liked_posts"
    )

    def __repr__(self):
        return f"Post(title='{self.title}', description={self.description})"

class Comment(Base):
    __tablename__ = 'comments'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(index=True)
    user_id: Mapped[int] = mapped_column(
        sa.ForeignKey(column='users.id', ondelete='CASCADE'), nullable=False
    )
    user: Mapped["User"] = so.relationship(back_populates="comments_made")
    comment_id: Mapped[int] = mapped_column(
        sa.ForeignKey(column='comments.id', ondelete='CASCADE'), nullable=False
    )

    def __repr__(self):
        return f"Comment(text='{self.text}')"

