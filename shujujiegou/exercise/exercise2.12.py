# -*- codeing = utf-8 -*-
# @Time : 2021/10/23 13:35
# @Author : wzq
# @File : exercise2.12.py
# @Software : PyCharm
#建立一个新的递增有序整数单链表
class LinkNode:                         #单链表结点类
    def __init__(self,data=None):       #构造函数
        self.data=data                  #data属性
        self.next=None                  #next属性

class LinkList:                         #单链表类
    def __init__(self):                 #构造函数
        self.head=LinkNode()            #头结点head
        self.head.next=None


    def CreateListF(self, a):		    #头插法：由数组a整体建立单链表
        for i in range(0,len(a)):       #循环建立数据结点s
            s=LinkNode(a[i])			#新建存放a[i]元素的结点s
            s.next=self.head.next		#将s结点插入到开始结点之前,头结点之后
            self.head.next=s

    def CreateListR(self, a):			#尾插法：由数组a整体建立单链表
        t=self.head						#t始终指向尾结点,开始时指向头结点
        for i in range(0,len(a)):		#循环建立数据结点s
            s=LinkNode(a[i]);			#新建存放a[i]元素的结点s
            t.next=s					#将s结点插入t结点之后
            t=s
        t.next=None						#将尾结点的next成员置为null

    def geti(self, i):		            #返回序号为i的结点
        p=self.head
        j=-1
        while (j<i and p is not None):
            j+=1
            p=p.next
        return p

    def Add(self, e):						    #在线性表的末尾添加一个元素e
        s=LinkNode(e)		                    #新建结点s
        p=self.head
        while p.next is not None:				#查找尾结点p
            p=p.next
        p.next=s;								#在尾结点之后插入结点s

    def getsize(self):                          #返回长度
        p=self.head
        cnt=0
        while p.next is not None:				#找到尾结点为止
            cnt+=1
            p=p.next
        return cnt

    def __getitem__(self,i):                    #求序号为i的元素
        assert i>=0                             #检测参数i正确性的断言
        p=self.geti(i)
        assert p is not None                    #p不为空的检测
        return p.data

    def __setitem__(self, i, x):                #设置序号为i的元素
        assert i>=0                             #检测参数i正确性的断言
        p=self.geti(i)
        assert p is not None                    #p不为空的检测
        p.data=x

    def GetNo(self,e):							#查找第一个为e的元素的序号
        j=0
        p=self.head.next
        while p is not None and p.data!=e:
            j+=1									#查找元素e
            p=p.next
        if p is None:
            return -1						    #未找到时返回-1
        else:
            return j							#找到后返回其序号

    def Insert(self, i, e):					    #在线性表中序号i位置插入元素e
        assert i>=0                             #检测参数i正确性的断言
        s=LinkNode(e)		                    #建立新结点s
        p=self.geti(i-1)				        #找到序号为i-1的结点p
        assert p is not None                    #p不为空的检测
        s.next=p.next							#在p结点后面插入s结点
        p.next=s

    def Delete(self,i): 						#在线性表中删除序号i位置的元素
        assert i>=0							    #检测参数i正确性的断言
        p=self.geti(i-1)					    #找到序号为i-1的结点p
        assert p.next is not None               #p.next不为空的检测
        p.next=p.next.next;						#删除p结点的后继结点

    def display(self):					        #输出线性表
        p=self.head.next
        while p is not None:
            print(p.data,end=' ')
            p=p.next;
        print()
def Commnodes(A,B):
    p = A.head.next
    q = B.head.next
    C = LinkList()
    t = C.head
    while p != None and q != None :
        if p.data < q.data :
            p = p.next
        elif q.data < p.data :
            q = q.next
        else :
            s = LinkNode(p.data)
            t.next = s
            t = s
            p = p.next
            q = q.next
    t.next = None
    return C