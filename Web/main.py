from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "hello world!"

@app.route('/test')
def test():
    return render_template('test.html')
if __name__ == "__main__":
    app.run(port=11451,host="127.0.0.1")