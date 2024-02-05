from flask import Flask
from flask import render_template
import pymysql
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=11451,host="127.0.0.1")