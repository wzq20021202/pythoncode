# -*- codeing = utf-8 -*-
# @Time : 2021/12/16 19:37
# @Author : wzq
# @File : ex_bit_03.py
# @Software : PyCharm
from ex_bit_01 import *
print("构造二叉树bt1:")
pres = ['A','B','D','G','C','E','F']#先序序列
ins =  ['D','G','B','A','E','C','F']#中序序列
bt1=BTree()
bt1=CreateBTree1(pres,ins)
print("先序遍历:", end=' ');PreOrder(bt1)
print("\n中序遍历:", end=' ');InOrder(bt1)
print("\n后序遍历:", end=' ');PostOrder(bt1)
print("\n层次遍历:", end=' ');LevelOrder(bt1)
#基于先序遍历输出叶子结点
def Displeaf1(bt):
    _Displeaf1(bt.b)
    return
def _Displeaf1(t):
    if t!=None:
        if t.lchild==None and t.rchild==None:
            print(t.data,end='')		    #输出叶子结点
        _Displeaf1(t.lchild)				#遍历左子树
        _Displeaf1(t.rchild)			    #遍历右子树
#基于先序遍历求结点个数
def NodeCount1(bt):
    return _NodeCount1(bt.b)
def _NodeCount1(t):
    if t==None:									#空树结点个数为0
        return 0
    k=1											#根结点计数1，相当于访问根结点
    m=_NodeCount1(t.lchild)						#遍历求左子树的结点个数
    n=_NodeCount1(t.rchild)						#遍历求右子树的结点个数
    return k+m+n
print("\nbt1:",end='')
print(bt1.DispBTree())
print("所有叶子结点:",end='')
Displeaf1(bt1)
print("\n结点个数:%d"%(NodeCount1(bt1)))
print("深度=%d"%(bt1.Height()))