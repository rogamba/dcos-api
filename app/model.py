import datetime
import hashlib
from app import db

# carga la tabla de users
class Post(db.Model):
    __tablename__ = 'post'
    id_post = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(255),unique=True)
    text = db.Column(db.String(255))
    date = db.Column(db.DateTime)

    @staticmethod
    def create(user, text, date):
        post = Post(
            user=user,
            text=text,
            date=date
        )
        db.session.add(post)
        db.session.commit()
        return post
