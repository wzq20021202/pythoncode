# -*- codeing = utf-8 -*-
# @Time : 2021/10/23 23:41
# @Author : wzq
# @File : exercise3.9.py
# @Software : PyCharm
class LinkNode:  # 单链表结点类
    def __init__(self, data=None):  # 构造方法
        self.data = data  # data域
        self.next = None  # next域


class LinkStack:  # 链栈类
    def __init__(self):  # 构造方法
        self.head = LinkNode()  # 头结点head
        self.head.next = None

    def empty(self):  # 判断栈是否为空
        if self.head.next == None:
            return True
        return False

    def push(self, e):  # 元素e进栈
        p = LinkNode(e)
        p.next = self.head.next
        self.head.next = p

    def pop(self):  # 元素出栈
        assert self.head.next != None  # 检测空栈的异常
        p = self.head.next;
        self.head.next = p.next
        return p.data

    def gettop(self):  # 取栈顶元素
        assert self.head.next != None  # 检测空栈的异常
        return self.head.next.data
def isSerial(a,b,n) :
    st = LinkStack()
    i,j = 0,0
    while i < n:  # 遍历a序列
        st.push(a[i])
        i += 1  # i后移
        while not st.empty() and st.gettop() == b[j]:
            st.pop()  # 出栈
            j += 1  # j后移
    return st.empty()