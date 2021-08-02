from flask import Flask, render_template, url_for, redirect, flash, request
from forms import LoginForm, SignupForm, FileForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from datetime import datetime
from flask_wtf.file import FileField



app = Flask(__name__)

app.config['SECRET_KEY'] = 'GYSVz4V3z8BJNDVGrCcaaPNdsbwcbEaH'

#set up config for database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db= SQLAlchemy(app)

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

@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/admin")
def admin():
    return render_template('admin.html')


@app.route("/")
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', time='Login', form=form)


@app.route("/signup",methods = ['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f"Account created for{form.username.data}!", 'success' )
        return redirect(url_for('home'))
    return render_template('signup.html', time = 'Signup', form = form)



#for uploading
@app.route("/upload",methods = ['GET','POST'])
def upload():
    form = FileForm()
    if form.validate_on_submit():
        if request.method == 'POST':
            uploaded_file = request.files['file']
            if uploaded_file.filename != '':
                uploaded_file.save(uploaded_file.filename)
                flash(f"File {form.filename.data} has been uploaded!", 'success')
                return redirect(url_for('upload'))
    return render_template('upload.html', time='Upload', form=form)



#for testing uploading
@app.route("/upload_test",methods = ['GET','POST'])
def upload_test():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
        return redirect(url_for('upload_test'))
    return render_template('upload_test.html')



@app.route("/index",methods = ['GET','POST'])
def index():
    form = FileForm()
    if form.validate_on_submit():
        flash(f"Account created for{form.filename.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('index.html', form=form)

@app.route("/joe")
def joe():
    return '<h>JOE IS A LITTLE BITCH</h>'

if __name__ == '__main__':
    app.run(debug=True)
