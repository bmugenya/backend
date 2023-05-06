from api import db
from datetime import datetime, timedelta
from time import time
from werkzeug.security import generate_password_hash, check_password_hash


class Updateable:
    def update(self, data):
        for attr, value in data.items():
            setattr(self, attr, value)


class User(db.Model,Updateable):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    email_verified = db.Column(db.DateTime)
    password_hash = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)
    favorite_ids = db.Column(db.String)

    accounts = db.relationship('Account')
    listings = db.relationship('Listing')
    reservations = db.relationship('Reservation')

    @property
    def avatar_url(self):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon'

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)



class Account(db.Model,Updateable):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    acc_type = db.Column(db.String)
    provider = db.Column(db.String)
    provider_account_id = db.Column(db.String)
    refresh_token = db.Column(db.String)
    access_token = db.Column(db.String)
    expires_at = db.Column(db.Integer)
    token_type = db.Column(db.String)
    scope = db.Column(db.String)
    id_token = db.Column(db.String)
    session_state = db.Column(db.String)

    user = db.relationship('User')


class Listing(db.Model,Updateable):
    __tablename__ = 'listings'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    image_src = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    category = db.Column(db.String)
    room_count = db.Column(db.Integer)
    bathroom_count = db.Column(db.Integer)
    guest_count = db.Column(db.Integer)
    location_value = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    price = db.Column(db.Integer)

    user = db.relationship('User')
    reservations = db.relationship('Reservation')


class Reservation(db.Model,Updateable):
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    total_price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now)

    user = db.relationship('User')
    listing = db.relationship('Listing')






