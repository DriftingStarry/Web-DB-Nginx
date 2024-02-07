from flask import Flask
from flask import render_template
import pymysql
def get():
    conn = pymysql.connect(host='mydb',port=3306,user='Flask',password='Flask_1919810',database='hddata')
    cur = conn.cursor()
    sql = "select * from news"
    cur.execute(sql)
    conn.commit()
    r = cur.fetchall()
    return r[-1:-11:-1]
app = Flask(__name__)

@app.route('/')
def index():
    r = get()
    return render_template("index.html",r=r)

if __name__ == "__main__":
    app.run(port=11451,host="127.0.0.1")