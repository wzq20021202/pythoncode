# -*- codeing = utf-8 -*-
# @Time : 2021/10/23 12:31
# @Author : wzq
# @File : exercise2.7.py
# @Software : PyCharm
#查找最大结点个数
def Delmaxnodes(L) :
    p = L.head.next
    maxe = p.data
    while p.next != None :
        if p.next.data > maxe :
            maxe = p.next.data
            cnt = 1
        elif p.next.data == maxe :
            cnt += 1
        p = p.next
    return cnt
