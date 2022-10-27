from flask import Flask, render_template
from sqlalchemy import false, null, true
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/showContactList")
def contactList():
    return render_template('showContactList.html')

@app.route("/signup")
def signUp():

    return render_template('signup.html')

app.run(debug=True)