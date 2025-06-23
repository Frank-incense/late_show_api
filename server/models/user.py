from server.config import db
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):

    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    username = Column(String(), unique=True, nullable=False)
    _password_hash = Column(String())

    def __repr__(self):
        return f"<User: {self.id}, {self.username}>"
    
    @validates('username')
    def validates_username(self, key, value):
        user = User.query.filter_by(username=value).first()
        if user and not isinstance(value, str):
            raise ValueError('Username should be unique string')
        return value
    
    @hybrid_property
    def password_hash(self):
        raise AttributeError('Cannot access this value')
    
    @password_hash.setter    
    def password_hash(self, value):
        from server.app import bcrypt
        password_hash = bcrypt.generate_password_hash(value.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        from server.app import bcrypt
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))


