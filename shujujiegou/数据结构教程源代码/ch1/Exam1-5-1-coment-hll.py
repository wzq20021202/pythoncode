# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:36:23 2021

@author: huanglili
"""
'''
class CLanguage:
    pass

clangs = CLanguage()
#默认情况下，我们得到的信息只会是“类名+object at+内存地址”
print(clangs) 
'''

#通过重写类中的__repr__() 方法，从而实现当输出实例化对象时，输出我们想要的信息。
class CLanguage:
    def __init__(self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"
    def __repr__(self):
        return "CLanguage[name="+ self.name +",add=" + self.add +"]"
clangs = CLanguage()
print(clangs)