# -*- codeing = utf-8 -*-
# @Time : 2021/12/10 11:08
# @Author : wzq
# @File : exercise3.13.py
# @Software : PyCharm
from LinkQueue import LinkQueue
qu = LinkQueue()
def Jsequence(n,m):
    for i in range(1,n+1) :
        qu.push()
    for i in range(1,n+1):
        j = 1
        while j <= m-1 :
            qu.push(qu.pop())
            j += 1
        x = qu.pop()
        print(x,end = '')
print()