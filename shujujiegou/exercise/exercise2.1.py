# -*- codeing = utf-8 -*-
# @Time : 2021/10/21 9:38
# @Author : wzq
# @File : exercise2.1.py
# @Software : PyCharm

def Reverse(L):
    i = 0
    j = L.getsize() - 1
    while i < j:
        L[i], L[j] = L[j], L[i]
        i += 1
        j -= 1
