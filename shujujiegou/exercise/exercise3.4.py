# -*- codeing = utf-8 -*-
# @Time : 2021/10/23 22:38
# @Author : wzq
# @File : exercise3.4.py
# @Software : PyCharm
#顺序栈
class SqStack:
    def __init__(self):             #构造函数
        self.data=[]                #存放栈中元素，初始为空

    def empty(self):                #判断栈是否为空
        if len(self.data)==0:
            return True
        return False

    def push(self,e):               #元素e进栈
        self.data.append(e)

    def pop(self):                  #元素出栈
        assert not self.empty()     #检测栈为空
        return self.data.pop()

    def gettop(self):               #取栈顶元素
        assert not self.empty()     #检测栈为空
        return self.data[len(self.data)-1]

#判断表达式中括号是否配对
def isMatch(str) :
    st = SqStack()
    i = 0
    while i < len(str) :
        e = str[i]
        if e == '(' or e == '[' or e == '{' :
            st.push(e)
        else :
            if e == ')' :
                if st.empty() or st.gettop() != '(':
                    return False
                st.pop()
            if e == ']' :
                if st.empty() or st.gettop() != ']' :
                    return False
                st.pop()
            if e == '}' :
                if st.empty() or st.gettop() != '{' :
                    return False
                st.pop()
        i += 1
    return st.empty()
print("测试1")
str = "([)]"
if isMatch(str) :
    print(str + "方括号是匹配的")
else:
    print(str + "方括号不匹配")
print("测试2")
str = "([])"
if isMatch(str) :
    print(str + "方括号是匹配的")
else:
    print(str + "方括号不匹配")
