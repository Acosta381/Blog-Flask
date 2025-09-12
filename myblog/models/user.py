from myblog import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    password = db.Column(db.String)

    def __init__(self, username, password):  # to be able to create, fetch or manage the user database class
        self.username = username
        self.password = password

    def __repr__(self): # how should the object look when printed
        return f'User: {self.username}'