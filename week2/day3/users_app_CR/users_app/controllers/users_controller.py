from users_app import app
from flask import render_template,redirect,request,session,flash
from users_app.models.user_model import User

@app.route('/users')
def users_show():
	return render_template('read_all.html',users=User.get_all())

@app.route("/user/form")
def show_user_form():
    return render_template("create_user.html")

@app.route('/create/user',methods=['POST'])
def create_user():
	data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email']
	}
	user_id = User.save(data)
	return redirect('/users')

        


