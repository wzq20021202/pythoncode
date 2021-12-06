# -*- codeing = utf-8 -*-
# @Time : 2021/10/23 23:42
# @Author : wzq
# @File : exercise3.11.py
# @Software : PyCharm
# -*- codeing = utf-8 -*-
# @Time : 2021/10/23 23:41
# @Author : wzq
# @File : exercise3.7.py
# @Software : PyCharm
MaxSize=100                             #全局变量，假设容量为100
class CSqQueue:      			        #循环队列类
    def __init__(self):                 #构造方法
        self.data=[None]*MaxSize        #存放队列中元素
        self.front=0                    #队头指针
        self.rear=0                     #队尾指针
    def empty(self):				    #判断队列是否为空
        return self.front==self.rear
    def push(self,e):				    #元素e进队
        assert (self.rear+1)%MaxSize!=self.front   #检测队满
        self.rear=(self.rear+1)%MaxSize
        self.data[self.rear]=e
    def pop(self):						#出队元素
        assert not self.empty()         #检测队空
        self.front=(self.front+1)%MaxSize
        return self.data[self.front]
    def gethead(self):					#取队头元素
        assert not self.empty()         #检测队空
        head=(self.front+1)%MaxSize     #求队头元素的位置
        return self.data[head]

    #例3.11增加的方法
    def size(self):					    #返回队中元素个数
        return ((self.rear-self.front+MaxSize)%MaxSize)


def Reverse(st) :
    a = []
    while not st.empty() :
        a.append(st.pop())
    for j in range(len(a)) :
        st.push(a[j])
    return st
def pushk(qu,k,e):                     #进队第k个元素e
    n=qu.size()
    if k<1 or k>n+1:
        return False					#参数k错误返回False
    if k<=n:
        for i in range(1,n+1):          #循环处理队中所有元素
            if i==k:
                qu.push(e)				#将e元素进队到第k个位置
            x=qu.pop()					#出队元素x
            qu.push(x)					#进队元素x
    else:
        qu.push(e)						#k=n+1时直接进队e
    return True

def popk(qu,k):	                        #出队第k个元素
    n=qu.size()
    assert k>=1 and k<=n                 #检测参数k错误
    for i in range(1,n+1):				#循环处理队中所有元素
        x=qu.pop()						#出队元素x
        if i!=k:
            qu.push(x)					#将非第k个元素进队
        else:
            e=x							#取第k个出队的元素
    return e

#主程序
qu=CSqQueue()
qu.push(1)
qu.push(2)
qu.push(3)
qu.push(4)
print("元素个数=%d" %(qu.size()))
pushk(qu,1,5)
popk(qu,2)
while not qu.empty():
    print(qu.pop(),end=' ')
print()