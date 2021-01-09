from flask import Flask, redirect, url_for, render_template, request
from flask import request
from flask import session
import pandas as pd

app = Flask(__name__)
app.secret_key = '123'


@app.route('/open')
@app.route('/')
def openPage():
    return render_template('page1.html')


@app.route('/main')
def page2():
    return render_template('page2.html')

@app.route('/contactMe')
def page3():
    return render_template('page3.html')

@app.route('/UserList')
def UserList():
    return render_template('Users List.html')

@app.route('/assignment8')
def assignment8Page():
    return render_template('assignment8.html', hobby2='Cooking', name="Hilit", hobbies=['Dancing','knitting','Swimming'])

@app.route('/assignment8New')
def assignment8NewPage():
    return render_template('assignment8New.html', hobby2='Cooking', name="Hilit", hobbies=['Dancing','knitting','Swimming'])



@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    name = 'NONE'
    Users = {"Bar": "Bamani", "Liel": "Yanai", "Shiri": "Bash", "Daniel": "Peleg", "Rotem": "Halfon","Or": "Azar"}
    username = ' '
    logged_in = True

    if request.method == 'GET':
        if 'name' in request.args:
            name = request.args['name']

    if request.method == 'POST':
        username = request.form['username']
        session['logged_in'] = True
        session['username'] = username


    return render_template('assignment9.html',
                           request_method=request.method,
                           name = name,
                           Users = Users,
                           username = username)

@app.route('/log_out')
def log_out():
    session.pop('username')
    session['logged_in'] = False
    return redirect('/assignment9')


@app.route('/class10', methods=['GET', 'POST'])
def class10_func():
    username = ''
    second_name = ''
    if request.method == 'POST':
        # way to get to secured data - check in DB of the website
        session['logged_in'] = True
        username = request.form['username']
        session['username'] = username

    if request.method == 'GET':
        if 'second_name' in request.args:
            second_name = request.args['second_name']

    return render_template('class10.html',
                           request_method=request.method,
                           username=username,
                           second_name=second_name)


if __name__ == '__main__':
    app.run(debug=True)
