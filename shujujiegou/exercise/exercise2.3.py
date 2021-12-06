# -*- codeing = utf-8 -*-
# @Time : 2021/10/21 11:44
# @Author : wzq
# @File : exercise2.3.py
# @Software : PyCharm

# 解法一
def Deletex1(L, x):
    k = 0
    for i in range(L.getsize()):
        if L[i] != x:
            L[k] = L[i]
            k += 1
    L.size = k
# 解法二


def Deletex2(L, x):
    k = 0
    for i in range(L.getsize()):
        if L[i] != x:
            L[i - k] = L[i]
        else:
            k += 1
    L.size -= k

# 解法三


def Deletex3(L, x):
    i = -1
    j = 0
    while i < L.getsize():
        if L[j] != x:
            i += 1
            if i != j:
                L[i], L[j] = L[j], L[i]
        j += 1
    L.size = i + 1
