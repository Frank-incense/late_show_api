from server.config import db
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy_serializer import SerializerMixin
import datetime

class Episode(db.Model, SerializerMixin):

    __tablename__ = "eposodes"

    id = Column(Integer(), primary_key=True)
    date = Column(String(), nullable=False)
    number = Column(Integer(), nullable=False)

    def __repr__(self):
        return f"Episode: {self.id}, {self.number}"