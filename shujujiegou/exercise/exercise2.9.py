# -*- codeing = utf-8 -*-
# @Time : 2021/10/23 13:02
# @Author : wzq
# @File : exercise2.9.py
# @Software : PyCharm
#逆置L中的所有结点
def Reverse(L):
    p = L.head.next
    L.head.next = None
    while p != None :
        q = p.next
        p.next = L.head.next
        L.head.next = p
        p = q