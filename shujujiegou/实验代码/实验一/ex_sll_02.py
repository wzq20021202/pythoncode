# -*- codeing = utf-8 -*-
# @Time : 2021/11/19 21:24
# @Author : wzq
# @File : ex_sll_02.py
# @Software : PyCharm
from ex_sll_01 import LinkList

def Merge2(SLLa,SLLb):                    #求解算法
    p=SLLa.head.next                #p指向A的首结点
    q=SLLb.head.next                #q指向B的首结点
    SLLc=LinkList();                   #新建立单链表C
    t=SLLc.head                   #t为C的尾结点
    while p!=None and q!=None:     #两个单链表都没有遍历完
        if p.data<q.data:        #将较小结点p链接到C的末尾
            t.next=p
            t=p
            p=p.next
        else:                 #将较小结点q链接到C的末尾
            t.next=q
            t=q
            q=q.next
    t.next=None                   #尾结点next置空
    if p!=None: t.next=p;
    if q!=None: t.next=q;
    return C

A=LinkList()
a=[18,39,66]
A.CreateListR(a)
print("A: ",end=''),A.display()

B=LinkList()
b=[28,4,95,86,170]
B.CreateListR(b)
print("B: ",end=''),B.display()

print("合并")
L=Merge2(A,B)
print("L: ",end=''),L.display()