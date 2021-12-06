# -*- codeing = utf-8 -*-
# @Time : 2021/10/23 12:41
# @Author : wzq
# @File : exercise2.8.py
# @Software : PyCharm
#删除最大结点
def Delmaxnodes(L) :
    p = L.head.next
    maxe = p.data
    while p.next != None :
        if p.next.data > maxe :
            maxe = p.next.data
        p = p.next
    pre = L.head
    p = pre.next
    while p != None :
        if p.data == maxe :
            pre.next = p.next
            p = pre.next
        else :
            pre = pre.next
            p = pre.next
