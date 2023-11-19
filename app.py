from flask import Flask,render_template
from python_rotaeno_stabilizer import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)