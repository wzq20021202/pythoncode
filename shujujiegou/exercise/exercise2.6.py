# -*- codeing = utf-8 -*-
# @Time : 2021/10/21 22:17
# @Author : wzq
# @File : exercise2.6.py
# @Software : PyCharm

# 计数法
def Middle1(L):
    j = 1
    n = L.getsize()
    p = L.head.next
    while j <= (n - 1) // 2:
        j += 1
        p = p.next
    return p.data

# 快慢指针法
def Middle2(L):
    slow = L.head.next
    fast = L.head.next
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow.data
