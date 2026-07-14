from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    name = request.form.get('name')
    return render_template('login.html', name=name)

app.run(debug=True)


# redirct and errors--->

# redirect()
# (location, statuscode)

# Flask SQLite--->
# import sqlite3