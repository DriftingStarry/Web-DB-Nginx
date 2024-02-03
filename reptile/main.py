import requests as rq
from bs4 import BeautifulSoup

rep = rq.get("https://news.hqu.edu.cn/hdyw.htm")
if rep.ok:
    print(1)