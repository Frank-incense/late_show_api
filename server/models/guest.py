from server.config import db
from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin

class Guest(db.Model, SerializerMixin):

    __tablename__ = "guests"

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    occupation = Column(String(), nullable=False)

    def __repr__(self):
        return f"<Guest: {self.id}, {self.name}>"