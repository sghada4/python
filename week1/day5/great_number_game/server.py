from flask import Flask, request, session, render_template, redirect
import random
app = Flask(__name__)
app.secret_key='hello from coding dojo'

@app.route('/guess')
def index():
    if "number" not in session:
        session['number'] = random.randint(1,100)

    return render_template("index.html")

@app.route('/game',methods=['POST'])
def guess():
    session['number_submitted'] = int(request.form['number_submitted'])
    return redirect('/guess')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/guess')

if __name__== "__main__":
    app.run(debug=True)