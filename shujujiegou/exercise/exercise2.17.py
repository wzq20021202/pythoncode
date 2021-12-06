# -*- codeing = utf-8 -*-
# @Time : 2021/10/23 21:26
# @Author : wzq
# @File : exercise2.17.py
# @Software : PyCharm
def Comb(A,B) :
    ta = A.dhead.prior
    tb = B.dhead.prior
    ta.next = B.dhead.next
    B.dhead.next.prior = ta
    tb.next = A.dhead
    A.dhead.prior = tb
    return A
