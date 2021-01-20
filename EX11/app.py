from flask import Flask, redirect, url_for, render_template, request, jsonify
from flask import request
from flask import session
import mysql.connector
from Assignment10.Assignment10 import Assigment10


app = Flask(__name__)
app.secret_key = '123'
app.register_blueprint(Assigment10)


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


# ------------------------connect to DB-------------------------- #

def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='myflasskappdb')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        # use for insert /update/delete
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # use for select statement
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value
 # ------------------------------------------------------ #

@app.route('/users_class11')
def users():
    query = "select * from users"
    query_result = interact_db(query, query_type='fetch')
    print(query_result)
    return render_template('users_class11.html', users=query_result)

@app.route('/insert-users_class11', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        query = "INSERT INTO users(name, email, password) VALUES ('%s', '%s', '%s')" % (name, email, password)
        interact_db(query, query_type='commit')
        return  redirect('/users_class11')
    return render_template('insert-users_class11.html', req_method=request.method)

@app.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'GET':
        user_id = request.args['id']
        query = "DELETE FROM users WHERE id='%s'" % user_id
        interact_db(query, query_type='commit')
        # return f'user with id {user_id} is deleted'
        return redirect('/users_class11')
    return 'deleted user'

@app.route('/product/<product_id>')
def get_product(product_id):
    return f'Product {product_id}'

#@app.route('/get_user', defaults={'user_id':2})
#@app.route('/get_user/<user_id>')
#def get_user(user_id):
 #   query = "SELECT * FROM users WHERE id='%s'" % user_id
  #  query_result= interact_db(query=query, query_type='fetch')
  #  return f'Users: {query_result}'


#------------------------Assignment11------------------------------#

@app.route('/assignment11/users')
def Assignment11():
        query = "SELECT * FROM users"
        query_result= interact_db(query= query, query_type='fetch')
        return f'users: {query_result}'


@app.route('/assignment11/users/selected', defaults={'SOME_USER_ID': 1})
@app.route('/assignment11/users/selected/<int:SOME_USER_ID>')
def get_user(SOME_USER_ID):
        query = "SELECT * FROM users WHERE id = '%s';" % SOME_USER_ID
        query_result= interact_db(query= query, query_type='fetch')
        if len(query_result) == 0:
            return 'Sorry, No user found :( '
        else:
            return jsonify({
                'success': 'True',
                'Data': query_result
            })