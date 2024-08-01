from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template("index.html")

@app.route('/<int:x>')
def checkerboard_x(x):
    return render_template("index_x.html",x=x)

@app.route('/<int:x>/<int:y>')
def checkerboard_x_y(x,y):
    return render_template("index_x_y.html",x=x,y=y)

@app.route('/<int:x>/<int:y>/<first_color>/<second_color>')
def checkerboard_x_y_colors(x,y,first_color,second_color):
    return render_template("index_x_y_colors.html",x=x,y=y,first_color=first_color,second_color=second_color)




if __name__ == "__main__":
    app.run(debug=True)