# -*- coding: utf-8 -*-
import requests as rq
from bs4 import BeautifulSoup
import pymysql
import time

def getid(href):
    i = -5
    id = ''
    while '0' <= href[i] <= '9':
        id = href[i] + id
        i -= 1
    return int(id)

def reptile(web):
    rep = rq.get(web)
    rep.encoding = 'utf-8'
    urls = []
    if rep.ok:
        html = rep.text
        soup = BeautifulSoup(html,"html.parser")
        for i in range(10):
            lis = soup.findAll("li" , attrs={"id" : "line_u11_%d"%(i)})
            for l in lis:
                title = l.h3.text
                href = l.a['href']
                urls.append([title,'https://news.hqu.edu.cn/'+href,getid(href)])
    return urls

def dbwrite(host,port,url):
    try:
        print('connecting database...')
        conn = pymysql.connect(host=host,port=port,user='PyReptile',password='Py_114514',database='hddata')
        print('connection established')
        cur = conn.cursor()
        try:
            sql = "insert into news (title, turl, id) values ('%s','%s',%d)"%(url[0],url[1],url[2])
            cur.execute(sql)
            conn.commit()
            print('Successfully Writed')
        except:
            print('Write Error')
        cur.close()
        conn.close()
        print('connection closed')
    except:
        print("connection failed, reconnecting in 5s")
        for i in range(5,0,-1):
            print(i)
            time.sleep(1)
        dbwrite(host,port,url)  

def main():
    web = "https://news.hqu.edu.cn/hdyw.htm"
    host = 'mydb'
    port = 3306
    urls = reptile(web)
    for url in urls:
        try:
            print("news < ",url[0],url[1],url[2])
            dbwrite(host,port,url)
        except:
            print('err')
while True:
    main()
    time.sleep(300)