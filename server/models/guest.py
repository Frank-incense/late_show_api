from server.config import db
from sqlalchemy import Column, Integer, String

class Guest(db.Model):

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    occupation = Column(String(), nullable=False)

    def __repr__(self):
        return f"<Guest: {self.id}, {self.name}>"