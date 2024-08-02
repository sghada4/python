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
	return redirect(f'/show_user/{user_id}')

@app.route('/show_user/<int:id>')
def show_one_user(id):
    data = {'id':id}
    user = User.get_one_by_id(data)

    return render_template("show_one_user.html", user= user)

@app.route('/edit_user_form/<int:id>')
def edit(id):
    data = {'id':id}
    user = User.get_one_by_id(data)

    return render_template("edit_user.html", user= user)

@app.route('/edit_user',methods=['POST'])
def edit_user():
	id = request.form['id']
	data = {
		"id": id,
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email']
	}
	User.edit(data)
	return redirect(f'/show_user/{id}')

@app.route('/delete/<int:id>')
def delete(id):
    User.delete({'id': id})

    return redirect('/users')