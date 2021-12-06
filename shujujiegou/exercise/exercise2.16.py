# -*- codeing = utf-8 -*-
# @Time : 2021/10/23 20:54
# @Author : wzq
# @File : exercise2.16.py
# @Software : PyCharm
#约瑟夫问题
class Child :
    def __init__(self,nol):
        self.no = nol
        self.next = None
class Joseph :
    def __init__(self,n1,m1):
        self.n = n1
        self.m = m1
        self.first = Child(1)
        t = self.first
        for i in range (2,self.n + 1) :
            p = Child(i)
            t.next = p
            t = p
        t.next = self.first
    def Jsequence(self) :
        for i in range(1,self.n + 1) :
            p = self.first
            j = 1
            while j < self.m - 1:
                j +=1
                p = p.next
            q = p.next
            print(q.no,end=' ')
            p.next = q.next
            self.first = p.next
        print()
m = 3
n = 6
L = Joseph(n,m)
print("n=%d,m=%d的约瑟夫序列："%(n,m))
L.Jsequence()