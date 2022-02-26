# -*- codeing = utf-8 -*-
# @Time : 2021/12/23 19:01
# @Author : wzq
# @File : ex_07_01.py.py
# @Software : PyCharm
class SqList:
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

#直接插入排序
def cmp(x, y):
    if x >= y:
        return True
    else:
        return False
def InsertSort(R):                  # 对R[0..n-1]按递增有序进行直接插入排序
    for i in range(1, len(R)):      # 从第2个元素即R[1]开始
        if cmp(R[i], R[i - 1]):     # 反序时
            tmp = R[i]              # 取出无序区的第一个元素
            j = i - 1               # 在有序区R[0..i-1]中从右向左找R[i]的插入位置
            while True:
                R[j + 1] = R[j]     # 将大于tmp的元素后移
                j -= 1              # 继续向前比较
                if j < 0 or not cmp(tmp, R[j]): break  # 若j<0或者R[j]<=tmp,退出循环
            R[j + 1] = tmp          # 在j+1处插入R[i]


#希尔排序
def ShellSort(R):				    #对R[0..n-1]按递增有序进行希尔排序
    d=len(R)//2					    #增量置初值
    while d>0:
        for i in range(d,len(R)):   #对所有相隔d位置的元素组采用直接插入排序
            if R[i]<R[i-d]:     	#反序时
                tmp=R[i]
                j=i-d
                while True:
                    R[j+d]=R[j]			#将大于tmp的元素后移
                    j=j-d               #继续向前找
                    if j<0 or R[j]<=tmp: break  #若j<0或者R[j]<=tmp,退出循环
                R[j+d]=tmp              #在j+d处插入tmp
        d=d//2						    #递减增量

#冒泡排序
def BubbleSort(R):  				    #对R[0..n-1]按递增有序进行冒泡排序
    for i in range(len(R)-1):
        exchange=False					#本趟前将exchange置为false
        for j in range(len(R)-1,i,-1):	#一趟中找出最小关键字的元素
            if R[j]<R[j-1]:         	#反序时交换
                R[j],R[j-1]=R[j-1],R[j] #R[j]和R[j-1]交换,将最小元素前移
                exchange=True			#本趟发生交换置exchange为true
        if exchange==False: return	    #本趟没有发生交换，中途结束算法

#快速排序
def Partition1(R,s,t):				#划分算法1
    base=R[s]						#以表首元素为基准
    i,j=s,t
    while i<j:						#从表两端交替向中间遍历,直至i=j为止
        while i<j and R[j]>=base:
            j-=1					#从后向前遍历,找一个小于基准的R[j]
        while i<j and R[i]<=base:
            i+=1					#从前向后遍历,找一个大于基准的R[i]
        if i<j:
            R[i],R[j]=R[j],R[i]     #将R[i]和R[j]进行交换
    R[s],R[i]=R[i],R[s]             #将基准R[s]和R[i]进行交换
    return i

def Partition1_1(R,s,t):			#划分算法1的优化算法
    base=R[s]						#以表首元素值为基准
    i,j=s,t+1
    while True:						#从表两端交替向中间遍历
        i+=1
        while R[i]<base:            #从前向后遍历,找一个大于基准的R[i]
            if i==t: break
            i+=1
        j-=1
        while base<R[j]:            #从后向前遍历,找一个小于基准的R[j]
            if j==s: break
            j-=1
        if i>=j: break
        R[i],R[j]=R[j],R[i]         #将R[i]和R[j]进行交换
    R[s],R[j]=R[j],R[s]             #R[s..j-1]≤R[j]≤R[j+1..t]
    return j

def Partition2(R,s,t):			    #划分算法2
    i,j=s,t
    base=R[s]						#以表首元素为基准
    while i!=j:						#从表两端交替向中间遍历,直至i=j为止
        while j>i and R[j]>=base:
            j-=1					#从后向前遍历,找一个小于基准的R[j]
        if j>i:
            R[i]=R[j]				#R[j]前移覆盖R[i]
            i+=1
        while i<j and R[i]<=base:
            i+=1					#从前向后遍历,找一个大于基准的R[i]
        if i<j:
            R[j]=R[i]				#R[i]后移覆盖R[j]
            j-=1
    R[i]=base						#基准归位
    return i						#返回归位的位置

def Partition3(R,s,t):   			#划分算法3
    i,j=s,s+1
    base=R[s]						#以表首元素为基准
    while j<=t:						#j从s+1开始遍历其他元素
        if R[j]<=base:				#找到小于等于基准的元素R[j]
            i+=1					#扩大小于等于base的元素区间
            if i!=j:
                R[i],R[j]=R[j],R[i] #将R[i]与R[j]交换
        j+=1						#继续扫描
    R[s],R[i]=R[i],R[s]             #将基准R[s]和R[i]进行交换
    return i


def QuickSort(R):			    #对R[0..n-1]的元素按递增进行快速排序
    QuickSort1(R,0,len(R)-1)

def QuickSort1(R,s,t):			#对R[s..t]的元素进行快速排序
    if s<t: 				 	#表中至少存在两个元素的情况
        i=Partition1_1(R,s,t)		#可以使用前面3种划分算法中的任意一种
        QuickSort1(R,s,i-1)		#对左子表递归排序
        QuickSort1(R,i+1,t)		#对右子表递归排序

#直接选择排序
def SelectSort(R):				#对R[0..n-1]元素进行简单选择排序
    for i in range(len(R)-1):			#做第i趟排序
        minj=i							#minj先置为区间中的首元素序号
        for j in range(i+1,len(R)):		#从R[i..n-1]中选最小元素的R[minj]
            if R[j]<R[minj]:			#与区间中其他元素比较
                minj=j
        if minj!=i:						#R[minj]不是无序区首元素
            R[i],R[minj]=R[minj],R[i]   #交换R[i]和R[minj]
#堆排序
def siftDown(R,low,high):	    #R[low..high]的自顶向下筛选
    i=low
    j=2*i+1				        #R[j]是R[i]的左孩子
    tmp=R[i]					#tmp临时保存根结点
    while j<=high:				#只对R[low..high]的元素进行筛选
        if j<high and R[j]<R[j+1]:
            j+=1				#若右孩子较大,把j指向右孩子
        if tmp<R[j]: 			#tmp的孩子较大
            R[i]=R[j]			#将R[j]调整到双亲位置上
            i,j=j,2*i+1			#修改i和j值,以便继续向下筛选
        else: break				#若孩子较小，则筛选结束
    R[i]=tmp					#原根结点放入最终位置

def siftUp(R,j):		        #自底向上筛选:从叶子结点i向上筛选
    i=(j-1)//2   				#i指向R[j]的双亲
    while True:
        if R[j]>R[i]:           #若孩子较大
            R[i],R[j]=R[j],R[i]	#交换
        if i==0: break			#到达根结点时结束
        j=i
        i=(j-1)//2				#继续向上调整

def HeapSort(R):					#对R[0..n-1]按递增进行堆排序
    n=len(R)
    for i in range(n//2-1,-1,-1):	#循环建立初始堆
        siftDown(R,i,n-1)			#对R[i..n-1]进行筛选
    for i in range(n-1,0,-1):       #进行n-1趟排序,每一趟排序的元素个数减1
        R[0],R[i]=R[i],R[0]			#将区间中最后一个元素与R[0]交换
        siftDown(R,0,i-1)		    #对R[0..i-1]]继续筛选
#归并排序算法
def Merge(R,low,mid,high):              #R[low..mid]和R[mid+1..high]归并为R[low..high]
    R1=[None]*(high-low+1)              #分配临时归并空间R1
    i,j,k=low,mid+1,0   				#k是R1的下标,i、j分别为第1、2段的下标
    while i<=mid and j<=high:			#在第1段和第2段均未扫描完时循环
        if R[i]<=R[j]:			        #将第1段中的元素放入R1中
            R1[k]=R[i]
            i,k=i+1,k+1
        else:				            #将第2段中的元素放入R1中
            R1[k]=R[j]
            j,k=j+1,k+1
    while i<=mid:						#将第1段余下部分复制到R1
        R1[k]=R[i]
        i,k=i+1,k+1
    while j<=high:						#将第2段余下部分复制到R1
        R1[k]=R[j]
        j,k=j+1,k+1
    R[low:high+1]=R1[0:high-low+1]

def MergePass(R,length):			    #一趟二路归并排序
    n=len(R)
    i=0
    while i+2*length-1<n:               #归并length长的两相邻子表
        Merge(R,i,i+length-1,i+2*length-1)
        i=i+2*length
    if i+length<n:						#余下两个子表,后者长度小于length
        Merge(R,i,i+length-1,n-1)	    #归并这两个子表

def MergeSort1(R):					    #对R[0..n-1]按递增进行二路归并算法
    length=1
    while length<len(R):                #进行log2n(取上界)趟归并
        MergePass(R,length)
        length=2*length

def MergeSort2(R):				        #对R[0..n-1]按递增进行二路归并算法
    MergeSort21(R,0,len(R)-1)

def MergeSort21(R,s,t):         	    #被MergeSort2调用
    if s>=t: return						#R[s..t]的长度为0或者1时返回
    m=(s+t)//2						    #取中间位置m
    MergeSort21(R,s,m)					#对前子表排序
    MergeSort21(R,m+1,t)				#对后子表排序
    Merge(R,s,m,t)						#将两个有序子表合并成一个有序表

list = [45, 53, 18, 36, 72, 30, 48, 93, 15, 36]
sqlist = SqList()
for i in list:
    sqlist.Add(i)
print("sqlist:\n", end=''),sqlist.display()
InsertSort(list)
sqlist = SqList()
for i in list:
    sqlist.Add(i)
print("直接插入排序sqlist:\n", end=''),sqlist.display()
ShellSort(list)
sqlist = SqList()
for i in list:
    sqlist.Add(i)
print("希尔排序sqlist: \n", end=''),sqlist.display()
BubbleSort(list)
sqlist = SqList()
for i in list:
    sqlist.Add(i)
print("冒泡排序sqlist: \n", end=''),sqlist.display()
QuickSort(list)
sqlist = SqList()
for i in list:
    sqlist.Add(i)
print("快速排序sqlist: \n", end=''),sqlist.display()
SelectSort(list)
sqlist = SqList()
for i in list:
    sqlist.Add(i)
print("直接选择排序sqlist: \n", end=''),sqlist.display()
HeapSort(list)
sqlist = SqList()
for i in list:
    sqlist.Add(i)
print("堆排序sqlist: \n", end=''),sqlist.display()
MergeSort1(list)
sqlist = SqList()
for i in list:
    sqlist.Add(i)
print("归并排序sqlist: \n", end=''),sqlist.display()