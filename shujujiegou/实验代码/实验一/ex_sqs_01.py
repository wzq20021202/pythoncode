# -*- codeing = utf-8 -*-
# @Time : 2021/11/19 21:26
# @Author : wzq
# @File : ex_sqs_01.py
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
if __name__ == '__main__':
    SQS=SqStack()
    print(SQS.empty())
    SQS.push(1)
    SQS.push(3)
    SQS.push(5)
    SQS.gettop()
    while not SQS.empty():
        print(SQS.pop(),end='\n')
    print(SQS.empty())