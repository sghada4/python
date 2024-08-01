from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    #return 'Hello World!'
    return render_template('index.html')

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say_name(name):
    return f'Hi {name}!'

@app.route('/repeat/<int:times>/<word>')
def repeat(times, word):
    msg = ""
    for i in range(times):
        msg += f"{word} \n"
    return msg

@app.route('/index')
def index():
    return render_template('index.html', phrase="hello", times=5)

@app.route('/play')
def play():
    return render_template('index.html')

@app.route('/play/<int:x>')
def multi_play(x):
    return render_template('index.html', x=x)

@app.route('/play/<int:x>/<color>')
def play_change_color(x, color):
    return render_template('index.html', x=x, color=color)

if __name__=="__main__":
    app.run(debug=True)