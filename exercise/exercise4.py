# -*- codeing = utf-8 -*-
# @Time : 2021/10/14 19:56
# @Author : wzq
# @File : 3.py
# @Software : PyCharm
# 中缀表达式转换为前缀和后缀形式
from exercise2 import Stack
def infixToPostfix(infixexpr):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    opStack = Stack()
    postfixlist = []
    tokenList = infixexpr.split()
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixlist.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixlist.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (
                    prec[opStack.peek()] >= prec[token]):
                postfixlist.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixlist.append(opStack.pop())
    return "".join(postfixlist)
