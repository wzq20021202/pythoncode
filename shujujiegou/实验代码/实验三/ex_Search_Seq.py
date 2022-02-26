# -*- codeing = utf-8 -*-
# @Time : 2021/12/23 19:00
# @Author : wzq
# @File : ex_Search_Seq.py
# @Software : PyCharm
class StaticTable:
    def __init__(self):  # 构造函数
        self.initcapacity = 5  # 初始容量设置为10
        self.capacity = self.initcapacity  # 容量设置为初始容量
        self.data = [None] * self.capacity  # 设置顺序表的空间
        self.size = 0  # 长度设置为0

    def empty(self):
        if len(self.data) == 0:
            return True
        return False

    def resize(self, newcapacity):  # 改变顺序表的容量为newcapacity
        assert newcapacity >= 0  # 检测参数正确性的断言
        olddata = self.data
        self.data = [None] * newcapacity
        self.capacity = newcapacity
        for i in range(self.size):
            self.data[i] = olddata[i]

    def CreateList(self, a):  # 由数组a中元素整体建立顺序表
        for i in range(0, len(a)):
            if self.size == self.capacity:  # 出现上溢出时
                self.resize(2 * self.size) # 扩大容量
            self.data[self.size] = a[i]
            self.size += 1  # 添加后元素个数增加1

    def Add(self, e):  # 在线性表的末尾添加一个元素e
        if self.size == self.capacity:  # 顺序表空间满时倍增容量
            self.resize(2 * self.size)
        self.data[self.size] = e  # 添加元素e
        self.size += 1  # 长度增1

    def getsize(self):  # 返回长度
        return self.size

    def __getitem__(self, i):  # 求序号为i的元素
        assert 0 <= i < self.size  # 检测参数i正确性的断言
        return self.data[i]

    def __setitem__(self, i, x):  # 设置序号为i的元素
        assert 0 <= i < self.size  # 检测参数i正确性的断言
        self.data[i] = x

    def GetNo(self, e):  # 查找第一个为e的元素的序号
        i = 0
        while i < self.size and self.data[i] != e:
            i += 1  # 查找元素e
        if (i >= self.size):  # 未找到时返回-1
            return -1
        else:
            return i  # 找到后返回其序号

    def Insert(self, i, e):  # 在线性表中序号i位置插入元素e
        assert 0 <= i <= self.size  # 检测参数i正确性的断言
        if self.size == self.capacity:  # 满时倍增容量
            self.resize(2 * self.size)
        for j in range(self.size, i, -1):  # 将data[i]及后面元素后移一个位置
            self.data[j] = self.data[j - 1]
        self.data[i] = e  # 插入元素e
        self.size += 1  # 长度增1

    def Delete(self, i):  # 在线性表中删除序号i的元素
        assert 0 <= i <= self.size - 1  # 检测参数i正确性的断言
        for j in range(i, self.size - 1):
            self.data[j] = self.data[j + 1]  # 将data[i]之后的元素前移一个位置
        self.size -= 1  # 长度减1
        if self.capacity > self.initcapacity and self.size <= self.capacity / 4:
            self.resize(self.capacity // 2)  # 满足要求容量减半

    def display(self):  # 输出顺序表
        for i in range(0, self.size):
            print(self.data[i], end=' ')
        print()

def SeqSearch1(R,k):				#顺序查找算法1
    n=len(R)
    i=0
    while i<n and R[i]!=k:
        i+=1	                    #从表头往后找
    if i>=n:
        return -1		            #未找到返回-1
    else:
        return i					#找到后返回其序号i
if __name__ == '__main__':
    R = (3, 6, 2, 10, 1, 8, 5, 7, 4, 9)
    k = 5
    list = StaticTable()
    print(list.empty())
    for i in R:
        list.Add(i)
    print("线性表list: ", end=''),list.display()
    print(SeqSearch1(R,k))

