from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
