#_*_ coding:utf8 _*_

import requests
from bs4 import BeautifulSoup

# 1、获取链接，解析链接
url = 'https://www.runoob.com/python/python-100-examples.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Mobile Safari/537.36'
}  # 从自己的浏览器获得，requests请求时模拟浏览器发起请求
html = requests.get(url, headers = headers).content.decode('utf-8')
soup = BeautifulSoup(html, 'lxml')  # 解析链接
soup.prettify()

# 2、获取每个练习题的链接地址并且得到每个练习题的题目、程序分析和代码
aLink  = soup.find(id = 'content').find_all('a')

with open('python-100.txt', 'w', encoding='utf-8') as py100:
    for i in aLink:
        dic = {}
        reLink = 'https://www.runoob.com' + str(i.attrs['href'])
        link = requests.get(reLink, headers=headers).content.decode('utf-8')
        bs = BeautifulSoup(link, 'lxml')
        # 获取标题
        #dic['title'] = bs.find(id='content').h1.text
        dic['title'] = bs.select('#content h1')[0].get_text()
        # 获取练习题题目内容
        #dic['question'] = bs.find(id='content').find_all('p')[1].text
        dic['question'] = bs.select('#content p')[1].get_text()
        # 获取程序分析的内容
        #dic['analysis'] = bs.find(id='content').find_all('p')[2].text
        dic['analysis'] = bs.select('#content p')[2].text
        # 获取代码，代码的存放有两种形式，一种保存在div中，一种保存在pre中
        try:
            dic['code'] = bs.find(id='content').find(class_ = 'example_code').text
        except Exception as e:
            dic['code'] = bs.find('pre').text
        py100.write(dic['title'] + '\n')
        py100.write(dic['question'] + '\n')
        py100.write(dic['analysis'] + '\n')
        py100.write(dic['code'] + '\n')