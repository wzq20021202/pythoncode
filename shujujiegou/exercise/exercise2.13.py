# -*- codeing = utf-8 -*-
# @Time : 2021/10/23 13:45
# @Author : wzq
# @File : exercise2.13.py
# @Software : PyCharm
#删除双链表L中第一个值为x的结点
def Delx(L,x):
    p = L.dhead.next
    while p != None and p.data != x :
        p = p.next
    if p != None :
        p.prior.next = p.next
        if p.next != None:
            p.next.prior = p.prior