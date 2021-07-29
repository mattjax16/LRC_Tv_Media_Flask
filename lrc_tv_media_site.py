from flask import Flask, render_template, url_for, redirect, flash
from forms import LoginForm, SignupForm, FileForm
from werkzeug.utils import secure_filename



app = Flask(__name__)

app.config['SECRET_KEY'] = 'GYSVz4V3z8BJNDVGrCcaaPNdsbwcbEaH'


@app.route("/home")
def home():
    return "<h1>Home Page</h1>"


@app.route("/about")
def about():
    return "<h1>About Page</h1>"


@app.route("/admin")
def admin():
    return "<h1>Admin Page</h1>"


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
        flash(f"Account created for{form.filename.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('upload.html', time='Upload', form=form)


#for uploading
@app.route("/index",methods = ['GET','POST'])
def index():
    form = FileForm()
    if form.validate_on_submit():
        flash(f"Account created for{form.filename.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
