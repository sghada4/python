from flask_app.models.user_model import User
from flask_app import app
from flask import redirect, request, render_template
@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
    # we redirect to the template with the form.
        return redirect('/')
    # ... do other things
    return redirect('/dashboard')

@app.route('/')
def display_reg():
    return render_template('register.html')
@app.route('/dashboard')
def show_emails():
    all_emails=User.get_all()
    return render_template('show_emails.html', all_emails=all_emails)