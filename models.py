from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'{self.id} {self.first_name} {self.last_name} {self.email}'

class Brag(db.Model):
    __tablename__ = 'brags'
    id = db.Column(db.Integer, primary_key=True)
    headline = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    bragtags = db.relationship('bragtags', backref='brags', lazy=True)

    def __repr__(self):
        return f'{self.id} {self.headline} {self.content} {self.timestamp} {self.user_id}'

class BragTag(db.Model):
    __tablename__ = 'bragtags'
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(120), nullable=False)
    brags = db.relationship('brags', secondary='bragtags', backref='bragtags')

    def __repr__(self):
        return f'{self.id} {self.tag_name}'
