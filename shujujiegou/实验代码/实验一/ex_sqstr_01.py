# -*- codeing = utf-8 -*-
# @Time : 2021/11/19 21:42
# @Author : wzq
# @File : ex_sqstr_01.py
# @Software : PyCharm
MaxSize=100                                 #假设容量为100
class SqString:                             #顺序串类
    def __init__(self):                     #构造方法
        self.data=[None]*MaxSize	        #存放串中字符
        self.size=0                         #串中字符个数
    #串的基本运算算法

    def StrAssign(self,cstr):		        #创建一个串
        for i in range(len(cstr)):
            self.data[i]=cstr[i]
        self.size=len(cstr)

    def Add(self, e):						    #在线性表的末尾添加一个元素e
        s=SqString(e)		                    #新建结点s
        p=self.head
        while p.next is not None:				#查找尾结点p
            p=p.next
        p.next=s;
    def StrCopy(self):			            #串复制
        s=SqString()
        for i in range(self.size):
            s.data[i]=self.data[i]
        s.size=self.size
        return s
    def getsize(self):			            #求串长
        return self.size
    def __getitem__(self,i):                #求序号为i的元素
        assert 0<=i<self.size               #检测参数i正确性的断言
        return self.data[i]
    def __setitem__(self,i,x):              #设置序号为i的元素
        assert 0<=i<self.size               #检测参数
        self.data[i]=x
    def Concat(self,t): 	                #串连接
        s=SqString()                        #新建一个空串
        s.size=self.size+t.getsize()
        for i in range(self.size):	        #将当前串data[0..str.size-1]->s
            s.data[i]=self.data[i]
        for i in range(t.getsize()):	    #将t.data[0..t.size-1]->s
            s.data[self.size+i]=t.data[i]
        return s						    #返回新串s
    def SubStr(self,i,j):	                #求子串
        s=SqString()                        #新建一个空串
        assert i>=0 and i<self.size and j>0 and i+j<=self.size   #检测参数
        for k in range(i,i+j):            #将data[i..i+j-1]->s
            s.data[k-i]=self.data[k]
        s.size=j
        return s				            #返回新建的顺序串
    def InsStr(self,i,t):	                #串插入
        s=SqString()            	        #新建一个空串
        assert i>=0 and i<self.size         #检测参数
        for j in range(i):					#将当前串data[0..i-1]->s
            s.data[j]=self.data[j]
        for j in range(t.getsize()):	    #将t.data[0..t.size-1]->s
            s.data[i+j]=t.data[j]
        for j in range(i,self.size):		#将当前串data[i..size-1]->s
            s.data[t.size+j]=self.data[j]
        s.size=self.size+t.getsize()
        return s							#返回新建的顺序串
    def DelStr(self,i,j):	                #串删除
        s=SqString()            	            #新建一个空串
        assert i>=0 and i<self.size and j>0 and i+j<=self.size #检测参数
        for k in range(i):					#将当前串data[0..i-1]->s
            s.data[k]=self.data[k]
        for k in range(i+j,self.size):	    #将当前串data[i+j..size-1]->s
            s.data[k-j]=self.data[k]
        s.size=self.size-j
        return s							#返回新建的顺序串
    def RepStr(self,i,j,t):                 #串替换
        s=SqString()        	            #新建一个空串
        assert i>=0 and i<self.size and j>0 and i+j<=self.size  #检测参数
        for k in range(i):                  #将当前串data[0..i-1]->s
            s.data[k]=self.data[k]
        for k in range(t.getsize()):	    #将s.data[0..t.size-1]→s
            s.data[i+k]=t.data[k]
        for k in range(i+j,self.size):	    #将当前串data[i+j..size-1]->s
            s.data[t.getsize()+k-j]=self.data[k]
        s.size=self.size-j+t.getsize()
        return s						    #返回新建的顺序串
    def DispStr(self):                      #输出串
        for i in range(self.size):
            print(self.data[i],end='')
        print()

if __name__ == '__main__':
    s = SqString()
    s1 = SqString()
    S = "abcdefghefghijklmn"
    S1 = "xyz"
    s.StrAssign(S)
    s1.StrAssign(S1)
    s.DispStr()
    s.getsize()
    s2 = s.InsStr(9,s1)
    print(s2)
    s2 = s.DelStr(2,5)
    print(s2)
    s2 = s.RepStr(2,5,s1)
    print(s2)
    s3 = s.SubStr(2,10)
    print(s3)
    s4 = S1 + S
    print(s4)