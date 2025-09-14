from myblog import db
from datetime import datetime

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow )

    def __init__(self, author, title, body):  # to be able to create, fetch or manage the user database class
        self.author = author
        self.title = title
        self.body = body

    def __repr__(self): # how should the object look when printed
        return f'Post: {self.title}'