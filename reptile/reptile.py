# -*- coding: utf-8 -*-
import requests as rq
from bs4 import BeautifulSoup
import pymysql
import time

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
                urls.append([title,'https://news.hqu.edu.cn/'+href])
    for url in urls:
        print(url)
    return urls

def dbwrite(host,port,url):
    conn = pymysql.connect(host=host,port=port,user='PyReptile',password='Py_114514',database='hddata')
    cur = conn.cursor()
    sql = "insert into news (title, turl) values ('%s','%s')"%(url[0],url[1])
    cur.execute(sql)
    conn.commit()

global preurls
preurls = []

def main():
    web = "https://news.hqu.edu.cn/hdyw.htm"
    host = 'mydb'
    port = 3306
    urls = reptile(web)
    for url in urls:
        if url not in preurls:
            print(url[0],url[1])
            dbwrite(host,port,url)
            preurls.append(url)
        else:
            print('Wirte None')
    while len(preurls) >= 11:
        preurls.pop(0)
        print(preurls)

while True:
    main()
    time.sleep(300)