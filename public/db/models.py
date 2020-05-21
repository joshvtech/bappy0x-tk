from flask import Markup, render_template_string
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
from humanize import naturaltime

from flask_login import UserMixin
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin

db = SQLAlchemy()

class links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    url = db.Column(db.String(120))

    def __init__(self, id, name, url):
        self.id = id
        self.name = name
        self.url = url

    def __repr__(self):
        return(f"<link {self.id}>")

class notifications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    important = db.Column(db.Boolean)
    timestamp = db.Column(db.DateTime)
    header = db.Column(db.String(120))
    body = db.Column(db.String(512))

    def __init__(self, id, important, header, body):
        self.id = id
        self.important = important
        self.header = header
        self.body = body

    def __repr__(self):
        return(f"<Notification {self.id}>")

    def render():
        notifs = []
        currentTime = datetime.now()
        for i in notifications.query.filter_by(timestamp=None).all() + notifications.query.filter(notifications.timestamp!=None).order_by(notifications.timestamp).limit(4).all():
            if i.timestamp and i.timestamp > currentTime:
                continue
            notifs.append(
                {
                    "id": i.id, 
                    "important": i.important,
                    "timestamp": naturaltime(currentTime - i.timestamp) if i.timestamp else None,
                    "header": Markup(i.header),
                    "body": Markup(render_template_string(i.body))
                }
            )
        return notifs

class users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)

class OAuth(OAuthConsumerMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(users.id))
    user = db.relationship(users)

class videos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    url = db.Column(db.String(120))

    def __init__(self, id, name, url):
        self.id = id
        self.name = name
        self.url = url

    def __repr__(self):
        return(f"<video {self.id}>")

