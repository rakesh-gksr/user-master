# project/api/models/quotes.py
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from project import db


class friendships(db.Model):

    __tablename__ = "friendships"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    friend_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    userR = db.relationship(
        'User',
        backref=db.backref('userR', lazy='dynamic'),
    )
    friendR = db.relationship(
        'User',
        backref=db.backref('friendR', lazy='dynamic'),
    )
    # userR = db.relationship('User', backref=db.backref('job', lazy='dynamic')foreign_keys='friendships.user_id')
    # friendR = db.relationship('User', foreign_keys='friendships.friend_id')

    def __init__(self, user_id, friend_id):
        self.user_id = user_id
        self.friend_id = friend_id


    def __repr__(self):
        return '{}-{}-{}-{}'.format(self.user_id, self.friend_id)


class bestFriends(db.Model):

    __tablename__ = "best_friends"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    best_friend_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    job = db.relationship(
        'Job',
        backref=db.backref('job', lazy='dynamic'),
    )
    user = db.relationship(
        'User',
        backref=db.backref('user', lazy='dynamic'),
    )
    best_friend = db.relationship(
        'User',
        backref=db.backref('best_friend', lazy='dynamic'),
    )
    user = db.relationship('User', foreign_keys='best_friends.user_id')
    best_friend = db.relationship('User', foreign_keys='best_friends.best_friend_id')


    def __init__(self, user_id, best_friend_id):

        self.user_id = user_id
        self.best_friend_id = best_friend_id


    def __repr__(self):
        return '{}-{}-{}-{}'.format(self.user_id, self.best_friend_id)