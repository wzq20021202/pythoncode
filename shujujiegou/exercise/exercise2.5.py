# -*- codeing = utf-8 -*-
# @Time : 2021/10/21 22:07
# @Author : wzq
# @File : exercise2.5.py
# @Software : PyCharm
def Middle(A,B):
    i = j = k = 0
    while i < A.getsize() and j < B.getsize() :
        k += 1
        if A[i] < B[j] :
            if k == A.getsize() :
                return A[i]
            i += 1
        else :
            if k == B.getsize() :
                return B[j]
            j += 1
