# -*- codeing = utf-8 -*-
# @Time : 2021/10/21 9:56
# @Author : wzq
# @File : exercise2.2.py
# @Software : PyCharm

def Deletek(L, i, k):
    assert i >= 0 and k >= 1 and i + k >= 1 and i + k <= L.getsize()
    for j in range(i + k, L.getsize()):
        L[j - k] = L[j]
    L.size -= k
