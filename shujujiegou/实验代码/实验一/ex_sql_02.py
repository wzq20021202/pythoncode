# -*- codeing = utf-8 -*-
# @Time : 2021/11/19 21:10
# @Author : wzq
# @File : ex_sql_02.py
# @Software : PyCharm
from ex_sql_01 import SqList
def Merge2(A, B):                           #求解算法
    C=SqList()                             #新建顺序表C
    i= A.getsize()
    j= B.getsize()
    x=abs(i-j)
    while 0 <= i < A.getsize() and 0 <= j <= B.getsize():
                                    #i用于遍历A,j用于遍历B
        if x!=0 :
            if i > j:
                C.Add(A[i])
                i-=1
            else:
                C.Add(B[j])
                j-= 1
        else:
                while A[i]>B[j]:
                    C.Add(A[i])                      #将较小的A中元素添加到C中
                    i-=1
                else:
                    C.Add(B[x])
                    j-= 1
        return C                                 #返回C

A=SqList()
a=[13,21,55,85,267]
A.CreateList(a)
print("A: ",end=''),A.display()
B=SqList()
b=[21,36,47,87,199]
B.CreateList(b)
print("B: ",end=''),B.display()
print("合并A和B得到C")
C=Merge2(A,B)
print("C: ",end=''),C.display()