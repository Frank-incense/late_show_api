from server.config import db
from sqlalchemy import Column, Integer, String

class User(db.Model):
    id = Column(Integer(), primary_key=True)
    username = Column(String(), unique=True, nullable=False)
    password_hash = Column(String(), nullable=False)

    def __repr__(self):
        return f"<User: {self.id}, {self.username}>"
    
    