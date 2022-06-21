import datetime

from app.db import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(150))
    body = db.Column(db.Text)
    published_date = db.Column(db.DateTime(timezone=True), default=None)
    created_date = db.Column(db.DateTime(timezone=True),default=datetime.datetime.utcnow)
    is_deleted = db.Column(db.Boolean, default=False)
    published =db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Post id:{self.id} title:{self.title} body:{self.body}>'