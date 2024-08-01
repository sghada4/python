from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = "I'm not in the mood"

@app.route('/process', methods=['POST'])
def display_form():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')


@app.route('/')
def show_form():
    return render_template('form.html')

@app.route('/result')
def show_result():
    return render_template('show_result.html')


if __name__ == '__main__':
    app.run(debug=True)