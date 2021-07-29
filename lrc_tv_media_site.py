from flask import Flask, render_template, url_for
from forms import LoginForm, SignupForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'GYSVz4V3z8BJNDVGrCcaaPNdsbwcbEaH'

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"


@app.route("/about")
def about():
    return "<h1>About Page</h1>"


@app.route("/admin")
def admin():
    return "<h1>Admin Page</h1>"

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', time='Login', form=form)

@app.route("/signup")
def signup():
    form = SignupForm()
    return render_template('siignup.html', time = 'Signup', form = form)


if __name__ == '__main__':
    app.run(debug=True)
