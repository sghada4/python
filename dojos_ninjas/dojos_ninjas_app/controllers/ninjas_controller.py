from flask import render_template, redirect, request
from dojos_ninjas_app import app
from dojos_ninjas_app.models import ninja_model
from dojos_ninjas_app.models import dojo_model

# ======= Display Route ========
@app.route("/ninjas")
def show_all_ninjas():
    all_ninjas = ninja_model.Ninja.fetch_all_ninjas()
    return render_template("all_ninjas.html", all_ninjas=all_ninjas)

# Display Route
@app.route("/ninjas/new")
def display_ninja_form():
    all_dojos = dojo_model.Dojo.fetch_all_dojos()
    print(all_dojos)
    return render_template("create_ninja.html", all_dojos = all_dojos)


# Action Route 
@app.route("/process", methods=['post'])
def give_ninja():
    ninja_model.Ninja.create_ninja(request.form)
    return redirect("/dojos")