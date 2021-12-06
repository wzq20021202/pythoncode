# -*- codeing = utf-8 -*-
# @Time : 2021/10/23 23:01
# @Author : wzq
# @File : exercise3.5.py
# @Software : PyCharm
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

def isPalindrome(str) :
    st = SqStack()
    n = len(str)
    i = 0
    while i < n//2 :
        st.push(str[i])
        i += 1
    if n % 2 == 1:
        i += 1
    while i < n :
        if st.pop() != str[i] :
            return False
        i += 1
        return True
print("测试1")
str = "abcda"
if isPalindrome(str) :
    print(str + "是回文")
else :
    print(str + "不是回文")

print("测试2")
str = "1221"
if isPalindrome(str) :
    print(str + "是回文")
else :
    print(str + "不是回文")