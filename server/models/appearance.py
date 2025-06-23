from server.config import db
from sqlalchemy.orm import validates, relationship
from sqlalchemy import Column, Integer,  ForeignKey
from sqlalchemy_serializer import SerializerMixin


class Appearance(db.Model, SerializerMixin):

    __tablename__ = "appearances"

    id = Column(Integer(), primary_key=True)
    rating = Column(Integer())
    guest_id = Column(Integer(), ForeignKey('guests.id'))
    episode_id =Column(Integer(), ForeignKey('episodes.id', ondelete='CASCADE'))

    guest = relationship('Guest', back_populates='appearances')
    episode = relationship('Episode', back_populates='appearances')

    serialize_rules = ('-guest.appearances', '-episode.appearances',)
    serialize_only = ('id', 'rating', 'guest_id', 'episode_id')
    
    def __repr__(self):
        return f"Appearance: {self.id}, {self.rating}"
    
    @validates('rating')
    def validate_rating(self, key, value):
        if isinstance(value, int) and 1 <= value <= 5:
            return value
        raise ValueError('Rating should be between 1 and 5 inclusive')
    