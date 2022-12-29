# Evey models represent a table in the database
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null, text
from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text('now()'), nullable=False)
    owner_id = Column(Integer, ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    # helps to get the user who created the post
    owner = relationship("Users")


class Users(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text('now()'), nullable=False)


class Vote(Base):
    __tablename__ = "votes"

    user_id = Column(Integer, ForeignKey(
        'users.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    post_id = Column(Integer, ForeignKey(
        'posts.id', ondelete='CASCADE'), primary_key=True, nullable=False)
