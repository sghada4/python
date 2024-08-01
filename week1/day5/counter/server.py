from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "Mon binome n'est pas serieux au travail aujourd'hui"

@app.route("/home")
def home():
    if 'number' in session:
        session['number']+=1
    else:
        session['number']=1
    return render_template("index.html")

@app.route('/')
def visit():
    return redirect('/home')

@app.route('/click', methods=['post'])
def add():
    session['number']+=1
    return redirect('/')

@app.route('/reset', methods=['post'])
def clear():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)