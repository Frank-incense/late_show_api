from server.config import db
from sqlalchemy.orm import validates, relationship
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy_serializer import SerializerMixin

class Episode(db.Model, SerializerMixin):

    __tablename__ = "episodes"

    id = Column(Integer(), primary_key=True)
    date = Column(DateTime(), nullable=False)
    number = Column(Integer(), nullable=False)

    appearances= relationship('Appearance', back_populates='episode')

    serialize_rules = ('-appearances.episode',)

    def __repr__(self):
        return f"Episode: {self.id}, {self.number}"