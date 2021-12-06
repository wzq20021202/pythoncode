# -*- codeing = utf-8 -*-
# @Time : 2021/10/23 16:01
# @Author : wzq
# @File : exercise2.15.py
# @Software : PyCharm
#求循环列表值为x的结点个数
def Count(L,x) :
    cnt = 0
    p = L.head.next
    while p != L.head :
        if p.data == x :
            cnt += 1
        p = p.next
    return cnt