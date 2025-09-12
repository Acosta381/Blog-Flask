from myblog import db

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String, db.ForeignKey('users.id'), nullable = False)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)

    def __init__(self, username, password):  # to be able to create, fetch or manage the user database class
        self.username = username
        self.password = password

    def __repr__(self): # how should the object look when printed
        return f'User: {self.username}'