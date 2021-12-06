# -*- codeing = utf-8 -*-
# @Time : 2021/8/13 20:06
# @Author : wzq
# @File : testUrllib.py
# @Software : PyCharm
# import urllib.request
# 获取一份get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))
# 获取一份post请求
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data = data)
# print(response.read().decode("utf-8"))


# url = "http://httpbin.org/post"
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
# }
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))
# url = "http://www.douban.com"
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
# }
# req = urllib.request.Request(url=url,headers=headers)
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))
