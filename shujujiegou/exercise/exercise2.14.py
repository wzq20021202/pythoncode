# -*- codeing = utf-8 -*-
# @Time : 2021/10/23 15:42
# @Author : wzq
# @File : exercise2.14.py
# @Software : PyCharm
#将L中最后一个值为x的结点与其前驱节点交换
def Swap(L,x) :
    p = L.dhead.next
    q = None
    while p != None :
        if p.data == x :
            q = p
            p = p.next
    if q == None or L.dhead.next == q :
        return
    else :
        pre = q.prior
        pre.next = q.next
        if q.next != None :
            q.next.prior = pre
        pre.prior.next = q
        q.prior = pre.prior
        pre.prior = q
        q.next = pre