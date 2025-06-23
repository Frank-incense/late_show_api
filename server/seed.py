from server.models import Episode, Guest, Appearance, User
from server.app import app, db
from datetime import datetime
from faker import Faker
import random

with app.app_context():
    fake = Faker()
    # Drop and create all tables
    db.drop_all()
    db.create_all()
    
    users = [User(username=fake.first_name()) for i in range(5)]
    for user in users:
        user.password_hash = fake.password()

    db.session.add_all(users)
    db.session.commit()
    print('Users added')

    episodes = [Episode(date=fake.date_this_decade(before_today=True),number=random.randint(1,100)) for i in range(1,20)]
    db.session.add_all(episodes)
    db.session.commit()
    print('Episodes added')

    guests = [Guest(name=fake.first_name(), occupation=fake.job()) for i in range(1,10)]
    db.session.add_all(guests)
    db.session.commit()
    print('Guests added')
    print(random.randint(1,5))
    appearances = [Appearance(rating=random.randint(1,5), guest_id=random.randint(1,9), episode_id=random.randint(1,9))for i in range(10)]

    db.session.add_all(appearances)
    db.session.commit()
    print('Appearances added')