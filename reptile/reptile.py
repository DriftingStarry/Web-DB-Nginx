# -*- coding: utf-8 -*-
import requests as rq
from bs4 import BeautifulSoup

rep = rq.get("https://news.hqu.edu.cn/hdyw.htm")
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
            urls.append([title,"https://news.hqu.edu.cn/"+href])
for url in urls:
    print(url)

lis = open("./list.txt" , "w+" , encoding = "utf-8")
for url in urls:
    for s in url:
        lis.writelines(s)
lis.close()
