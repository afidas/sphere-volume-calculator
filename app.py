from flask import Flask,redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/result", methods=["POST"])
def result(): 
    radius = abs(float(request.form["radius"]))
    pi = 3.14
    
    volume = round((4/3 * pi * radius ** 3), 2)
    
    return render_template("result.html", radius=radius, result=volume)


if __name__ == '__main__':
    app.run(debug=True)