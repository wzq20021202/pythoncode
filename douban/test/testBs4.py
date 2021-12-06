# -*- codeing = utf-8 -*-
# @Time : 2021/8/15 9:50
# @Author : wzq
# @File : testBs4.py
# @Software : PyCharm
import re
from bs4 import BeautifulSoup
file = open("./baidu.html","rb")
html = file.read()
bs = BeautifulSoup(html,"html.parser")
# print(bs.title)
# print(bs.head)
# print(bs.a)
# print(bs.a.attrs)
# print(type(bs))
# print(bs.name)
# print(bs)
# print(bs.a.string)
# print(bs.head.contents)
#文档的搜索
#字符串过滤
# t_list = bs.find_all("a")
# # print(t_list)
# t_list = bs.find_all(re.compile("a"))
# print(t_list)