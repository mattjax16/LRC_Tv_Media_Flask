from datetime import datetime
from LRCmediaUploader import db


#making data base classes
class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default = 'default.jpg')
    password = db.Column(db.String(60),nullable=False)
    uploaded_media = db.relation('LRCmedia', backref='author',lazy = True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class LRCmedia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    media_filename = db.Column(db.String(100), nullable=False)
    date_uploaded = db.Column(db.DateTime,nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    #make funcion for how it appears
    def __repr__(self):
        return f"LRCmedia('{self.media_filename}','{self.date_uploaded}','{self.id}')"
