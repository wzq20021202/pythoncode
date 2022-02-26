# -*- codeing = utf-8 -*-
# @Time : 2021/12/16 19:37
# @Author : wzq
# @File : ex_DFS.py
# @Software : PyCharm
import copy
MAXV=100							    #表示最多顶点个数
INF=0x3f3f3f3f				            #表示∞
class MatGraph:				            #图邻接矩阵类
    def __init__(self,n=0,e=0):         #构造方法
        self.edges=[]		            #邻接矩阵数组
        self.vexs=[]		            #存放顶点信息，暂时未用
        self.n=n                        #顶点数
        self.e=e			            #边数
    def CreateMatGraph(self,a,n,e):  	#通过数组a、n和e建立图的邻接矩阵
        self.n=n                        #置顶点数和边数
        self.e=e
        self.edges=copy.deepcopy(a)     #深拷贝
    def DispMatGraph(self):			    #输出图
        for i in range(self.n):
            for j in range(self.n):
                if self.edges[i][j]==INF:
                    print("%4s"%("∞"),end=' ')
                else:
                    print("%5d" %(self.edges[i][j]),end=' ')
            print()
MAXV=100                                    #全局变量，表示最多顶点个数
visited=[0]*MAXV
def DFS(g,v):       	                #邻接矩阵g中从顶点v出发的深度优先遍历
    print(v,end=" ")					#访问顶点v
    visited[v]=1					    #置已访问标记
    for w in range(g.n):
        if g.edges[v][w]!=0 and g.edges[v][w]!=INF:
            if visited[w]==0:		    #存在边<v,w>并且w没有访问过
                DFS(g,w)				#若w顶点未访问,递归访问它
def DFSA(G):
    for i in range(G.n):
        if visited[i] == 0:
            DFS(G,i)
if __name__ == '__main__':
    g=MatGraph()
    n,e=9,10
        #A, B, C, D, E ,F, G ,H ,I
    a=[ [0, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],]
    g.CreateMatGraph(a,n,e)
    g.DispMatGraph()
    print('深度优先遍历序列为')
    DFSA(g)