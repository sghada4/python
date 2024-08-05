from flask_app import app
from flask_app.models.dojo_model import Dojo
from flask import render_template, request, redirect

@app.route('/')
def show():
    all_dojos= Dojo.get_all()
    return render_template('show_result.html', all_dojos=all_dojos)

@app.route('/process', methods=['POST'])
def display_form():
    if not Dojo.validate_dojo(request.form):
        return redirect('/create')
    dojo_id= Dojo.save(request.form)
    return redirect('/')
@app.route('/create')
def create():
    return render_template('form.html')