# FLASK--->
# web framework for python
# handling user requests and responses
# managing web pages
# connecting to database

# you can use flask for build:
# login pages
# rest apis

# WSGI(web server gateway interface) 
# it allow python aplication  to communticate with a web server

# why is flask is a micro framework?
# becouse its modules and library is too smalls 

# the browser send a request
# the flask server recieve it
# flask processes it
# flask gets data from the database
# flask send a response
# the browser dsiplay it

# flask application
# creating your frist flask application

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return "hello world!"

@app.route('/about')
def about():
    return "this is the about page"

@app.route('/student/<name>')
def student(name):
    return f"Welcome, {name}!!!"

# router for query parameter--->
@app.route('/studenttt')
def studenttt():
    name = request.args.get('name')
    return f"welcome, {name}"

# http://127.0.0.1:5000/student?name=john

# for integer
# <int:number>

app.run(debug=True)

# SQL Queries--->
# MODELS->
# from flask_sqlalchemy import SQLALchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://students.db'

# db = SQLALchemy(app)

# class student(db.model):
#     id = db.column(db.integer, primary_key = True)
#     name = db.column(db.string(100), nullable = False)

#     def __rep__(self):