# -*- codeing = utf-8 -*-
# @Time : 2021/12/16 19:38
# @Author : wzq
# @File : ex_BFS.py
# @Software : PyCharm
from ex_DFS import *
from collections import deque


MAXV=100                                #全局变量，表示最多顶点个数
visited=[0]*MAXV
def BFS(G,v):		                    #邻接表G中从顶点v出发的广度优先遍历
    qu=deque()                          #将双端队列作为普通队列qu
    print(v,end=" ")					#访问顶点v
    visited[v]=1						#置已访问标记
    qu.append(v)						#v进队
    while len(qu)>0:                    #队不空循环
        v=qu.popleft()					#出队顶点v
        for j in range(len(G.adjlist[v])):  #处理顶点v的第j个相邻点
            w=G.adjlist[v][j].adjvex        #取第j个相邻顶点w
            if visited[w]==0:			    #若w未访问
                print(w,end=" ")			#访问顶点w
                visited[w]=1				#置已访问标记
                qu.append(w)				#w进队



MAXV=100							    #表示最多顶点个数
INF=0x3f3f3f3f				            #表示∞
class ArcNode:                          #边结点
    def __init__(self,adjv,w):          #构造方法
        self.adjvex=adjv                #邻接点
        self.weight=w                   #边的权值

class AdjGraph:				            #图邻接表类
    def __init__(self,n=0,e=0):         #构造方法
        self.adjlist=[]		            #邻接表数组
        self.vexs=[]			        #存放顶点信息，暂时未用
        self.n=n                        #顶点数
        self.e=e			            #边数
    def CreateAdjGraph(self,a,n,e):  	##通过数组a、n和e建立图的邻接表
        self.n=n                        #置顶点数和边数
        self.e=e
        for i in range(n):				#检查边数组a中每个元素
            adi=[]                      #存放顶点i的邻接点
            for j in range(n):
                if a[i][j]!=0 and a[i][j]!=INF: #存在一条边
                    p=ArcNode(j,a[i][j])        #创建<j,a[i][j]>出边的结点p
                    adi.append(p)               #将结点p添加到adi中
            self.adjlist.append(adi)
    def DispAdjGraph(self):				        #输出图的邻接表
        for i in range(self.n):                 #遍历每一个顶点i
            print("  [%d]" %(i),end='')
            for p in self.adjlist[i]:
                print("->(%d,%d)" %(p.adjvex,p.weight),end='')
            print("->∧")

def BFSA(G):
    for i in range(G.n):
        if visited[i] == 0:
            BFS(G,i)

if __name__ == '__main__':
    g=AdjGraph()
    n,e=9,10
         #A, B, C, D, E ,F, G ,H ,I
    a = [[0, 1, 0, 1, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1, 0, 0, 0, 0],   #a的邻接矩阵
         [0, 1, 0, 0, 0, 1, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 1, 0, 0],
         [1, 1, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 1, 0], ]
    g.CreateAdjGraph(a,n,e)
    g.DispAdjGraph()
    print('广度优先遍历序列为')
    BFS(g,0)
