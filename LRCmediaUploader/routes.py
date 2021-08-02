from flask import Flask, render_template, url_for, redirect, flash, request
from forms import LoginForm, SignupForm, FileForm
from LRCmediaUploader import app


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