from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def default_board():
    return render_template("checkerboard.html", x=8, y=8, color1="blue", color2="red")

@app.route('/<int:x>')
def x_only(x):
    return render_template("checkerboard.html", x=x, y=8, color1="blue", color2="red")

@app.route('/<int:x>/<int:y>')
def x_y(x, y):
    return render_template("checkerboard.html", x=x, y=y, color1="blue", color2="red")

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def x_y_colors(x, y, color1, color2):
    return render_template("checkerboard.html", x=x, y=y, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True, port=5000)
