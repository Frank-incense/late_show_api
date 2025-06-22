from server.config import db
from sqlalchemy import Column, Integer,  ForeignKey
from sqlalchemy_serializer import SerializerMixin
import datetime

class Appearance(db.Model, SerializerMixin):

    __tablename__ = "appearances"

    id = Column(Integer(), primary_key=True)
    rating = Column(Integer())
    guest_id = Column(Integer(), ForeignKey('guests.id'))
    episode_id =Column(Integer(), ForeignKey('episodes.id'))

    def __repr__(self):
        return f"Appearance: {self.id}, {self.rating}"