from flask import render_template, redirect, request
from dojos_ninjas_app import app
from dojos_ninjas_app.models import dojo_model
from dojos_ninjas_app.models import ninja_model

# ====== Display Route ========
@app.route("/dojos")
def show_all_dojos():
    us_dojos = dojo_model.Dojo.fetch_all_dojos()

    return render_template("all_dojos.html", us_dojos = us_dojos)


# ====== Display Route ========
@app.route("/dojos/form")
def show_dojo_form():

    return render_template("create_dojo.html")

# ====== Action Route ========
@app.route('/dojos/add', methods=['post'])
def process_dojo_form():
    # data = {
    #     'name': request.form['name'],
    #     'population': request.form['population'],
    #     'area': request.form['area']
    # }
    dojo_id = dojo_model.Dojo.create_dojo(request.form)

    return redirect("/dojos")

# ====== Display Route ========
@app.route('/dojos/<int:id>/show')
def show_one_dojo(id):
    data = {'id':id}
    dojo = dojo_model.Dojo.get_one_dojo_by_id(data)
    ninjas = ninja_model.Ninja.fetch_ninjas_dojo(data)

    return render_template("show_one_dojo.html", dojo= dojo, ninjas=ninjas)