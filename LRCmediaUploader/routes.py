from flask import Flask, render_template, url_for, redirect, flash, request
from LRCmediaUploader import app, db, bcrypt
from LRCmediaUploader.forms import LoginForm, RegisterForm, MediaForm, UpdateAccountForm
from LRCmediaUploader.models import User, LRCmedia
from flask_login import login_user, current_user, logout_user, login_required
import os
import secrets
from PIL import Image
# from werkzeug.utils import secure_filename


def save_picture(form_picture):
    '''
    Helper function to give a pictire in profile pics a random picture name and save it
    '''
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn



def save_media_name(form_media):
    '''
    Helper function to to save the media
    '''
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_media.filename)
    media_fn = random_hex + f_ext
    media_path = os.path.join(app.root_path, 'static/media_files', media_fn)


    return media_path

@app.route("/",methods = ['GET','POST'])
@app.route("/home",methods = ['GET','POST'])
@login_required
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/admin")
@login_required
def admin():
    return render_template('admin.html')


@app.route("/register",methods = ['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        # hash the password created if valid
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        #create a new user
        user = User(username= form.username.data, email = form.email.data, password = hashed_pw)
        # add user to database
        db.session.add(user)
        #commit change
        db.session.commit()

        flash(f"Account created for{form.username.data}! You are now able to login!", 'success' )
        return redirect(url_for('login'))

    #if it is not valid on submit return to the login page
    else:
        return render_template('register.html', time = 'Register', form = form)



#For the login page
@app.route("/",methods = ['GET','POST'])
@app.route("/login",methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('account'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)

            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('account'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)




#for testing uploading
@app.route("/upload",methods = ['GET','POST'])
@login_required
def upload():
    form = MediaForm()
    if request.method == 'POST':
        uploaded_file = request.files['file']
        print(f'First form file {uploaded_file}')
        if uploaded_file.filename:
            coded_filename = save_media_name(uploaded_file)
            uploaded_file.save(coded_filename)
        return redirect(url_for('upload'))
    return render_template('upload.html',form = form)


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        # handles changing picture
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        # handles changing username
        current_user.username = form.username.data

        # handles changing email
        current_user.email = form.email.data

        # commits changes and redirects to account
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)





@app.route("/index",methods = ['GET','POST'])
def index():
    # form = FileForm()
    # if form.validate_on_submit():
    #     flash(f"Account created for{form.filename.data}!", 'success')
    #     return redirect(url_for('home'))
    # return render_template('index.html', form=form)
    return render_template('index.html')



@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))














@app.route("/joe")
def joe():
    return '<h>JOE IS A LITTLE BITCH</h>'