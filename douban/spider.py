# -*- codeing = utf-8 -*-
# @Time : 2021/8/13 19:53
# @Author : wzq
# @File : spider.py
# @Software : PyCharm
import re
import urllib.request,urllib.error
from bs4 import BeautifulSoup
import xlwt
import sqlite3
def main():
    baseurl = "https://movie.douban.com/top250"
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影Top.xls"
    askURL('https://movie.douban.com/top250' )


def getData(baseurl):
    datalist = []
    for i in range(0,10):
        url = baseurl + str(i*25)
        html = askURL(url)







    return datalist





# 得到指定一个url的网页资源
def askURL(url):
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}
    req = urllib.request.Request(url=url, headers=head)
    html = ''
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    return html









def saveData(savepath):
    print( )

if __name__ == "__main__":
    main()
