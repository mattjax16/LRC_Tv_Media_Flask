from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#import library for encryption
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'\

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbdir/test.db'

#initilize database
db = SQLAlchemy(app)
# db.create_all()
#initiize encryption
bcrypt = Bcrypt(app)

#import at the routes at the end to
from LRCmediaUploader import routes
