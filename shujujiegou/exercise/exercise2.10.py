# -*- codeing = utf-8 -*-
# @Time : 2021/10/23 13:10
# @Author : wzq
# @File : exercise2.10.py
# @Software : PyCharm
#拆分链表
def Split(L,A,B) :
    p = L.head.next
    t = A.head
    while p != None:
        t.next = p
        t = p
        p = p.next
        if p != None :
            q = q.next
            p.next = B.head.next
            B.head.next = p
            p = q
    t.next = None