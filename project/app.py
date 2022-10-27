from base64 import encode
from datetime import datetime
from flask import Flask, flash, render_template, request, redirect, url_for
from sqlalchemy import false, null, true
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# import hashlib

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/assignment'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)
app.secret_key='djksdkADADjh'

class contactus(db.Model):
    email = db.Column(db.String(25), nullable =False)
    name  = db.Column(db.String(30), nullable = False)
    subject = db.Column(db.String(50), nullable = False, unique = True)
    message = db.Column(db.String(100), nullable = False, unique = True)
    qury = db.Column(db.String(100), nullable = False, unique = True)
    datetime = db.Column(db.DateTime,nullable = False)
    sno = db.Column(db.Integer, nullable = True, primary_key = True)


class users(db.Model):
    name = db.Column(db.String(25), nullable =False, primary_key = True)
    email = db.Column(db.String(25), nullable =False, unique = True)
    pass1 = db.Column(db.String(30), nullable =False)
    pass2 = db.Column(db.String(30), nullable =False)
    dob = db.Column(db.DateTime, nullable =False)
    gender = db.Column(db.String(10), nullable =False)
    reqdatetime = db.Column(db.DateTime, nullable =False)

@app.route("/", methods=['POST', 'GET'])
def contactpage():
    return render_template('index.html')

@app.route("/contactSubmit" , methods=['POST','GET'])
def contactSubmitting():
    if request.method == 'POST':
        email = request.form.get('email')
        name  = request.form.get('name')
        subject  =request.form.get('subject')
        message  = request.form.get('message')
        query = request.form.get('query')
        dateT = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = contactus(name = name, email = email, subject= subject, message = message, qury = query , datetime = dateT)
        db.session.add(entry)
        db.session.commit()
        flash('You are successfull Submited')
        return redirect(url_for('contactpage'))

@app.route("/showContactList")
def contactList():
    contactlist = contactus.query.all()
    return render_template('showContactList.html', contactlist = contactlist)

@app.route("/signup")
def signUp():
    return render_template('signup.html')


@app.route("/signuping" , methods = ['POST', 'GET'])
def signing():
    if request.method == 'POST':
        name  = request.form.get('name')
        email  = request.form.get('email')
        temp = request.form.get('password1')
        pass1 = bcrypt.generate_password_hash(temp)
        temp2  = request.form.get('password2')
        pass2 = bcrypt.generate_password_hash(temp2)
        dob  = request.form.get('dob')
        gender = request.form.get('gender')
        regDate  = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = users(name = name, email = email, pass1 = pass1, pass2 = pass2, dob = dob, gender = gender, reqdatetime = regDate)
        db.session.add(entry)
        db.session.commit()
        flash("You are successfull signup")
        return render_template('/welcomePage.html')
    else:
        flash("You are fail to signup")
        return redirect(url_for('signUp'))



app.run(debug=True)


# to remember 
#    pass1 = hashlib.md5(passwordToEncode, encode())