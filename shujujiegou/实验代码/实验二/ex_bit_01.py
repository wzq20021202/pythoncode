# -*- codeing = utf-8 -*-
# @Time : 2021/12/16 18:49
# @Author : wzq
# @File : ex_bit_01.py
# @Software : PyCharm
from collections import deque


class BTNode:                       # 二叉链中结点类
    def __init__(self, d=None):     # 构造方法
        self.data = d               # 结点值
        self.lchild = None          # 左孩子指针
        self.rchild = None          # 右孩子指针


class BTree:                        # 二叉树类
    def __init__(self, d=None):     # 构造方法
        self.b = None               # 根结点指针

    def SetRoot(self, r):           # 设置根结点为r
        self.b = r

    def DispBTree(self):            # 返回二叉链的括号表示串
        return self._DispBTree1(self.b)

    def _DispBTree1(self, t):       # 被DispBTree方法调用
        if t == None:               # 空树返回空串
            return ""
        else:
            bstr = t.data  # 输出根结点值
            if t.lchild != None or t.rchild != None:
                bstr += "("  # 有孩子结点时输出"("
                bstr += self._DispBTree1(t.lchild)  # 递归输出左子树
                if t.rchild != None:
                    bstr += ","  # 有右孩子结点时输出","
                bstr += self._DispBTree1(t.rchild)  # 递归输出右子树
                bstr += ")"  # 输出")"
            return bstr

    def FindNode(self, x):  # 查找值为x的结点算法
        return self._FindNode1(self.b, x)

    def _FindNode1(self, t, x):  # 被FindNode方法调用
        if t == None:
            return None  # t为空时返回null
        elif t.data == x:
            return t  # t所指结点值为x时返回t
        else:
            p = self._FindNode1(t.lchild, x)  # 在左子树中查找
            if p != None:
                return p  # 在左子树中找到p结点，返回p
            else:
                return self._FindNode1(t.rchild, x)  # 返回在右子树中查找结果

    def Height(self):  # 求二叉树高度的算法
        return self._Height1(self.b)

    def _Height1(self, t):  # 被Height方法调用
        if t == None:
            return 0  # 空树的高度为0
        else:
            lh = self._Height1(t.lchild)  # 求左子树高度lchildh
            rh = self._Height1(t.rchild)  # 求右子树高度rchildh
            return max(lh, rh) + 1


def PreOrder(bt):  # 先序遍历的递归算法
    PreOrder1(bt.b)

def PreOrder1(t):  # 被PreOrder方法调用
    if t != None:
        print(t.data, end=' ')  # 访问根结点
        PreOrder1(t.lchild)  # 先序遍历左子树
        PreOrder1(t.rchild)  # 先序遍历右子树
def InOrder(bt):  # 中序遍历的递归算法
    InOrder1(bt.b)
def InOrder1(t):  # 被InOrder方法调用
    if t != None:
        InOrder1(t.lchild)  # 中序遍历左子树
        print(t.data, end=' ')  # 访问根结点
        InOrder1(t.rchild)  # 中序遍历右子树
def PostOrder(bt):  # 后序遍历的递归算法
    PostOrder1(bt.b)
def PostOrder1(t):  # 被PostOrder方法调用
    if t != None:
        PostOrder1(t.lchild)  # 后序遍历左子树
        PostOrder1(t.rchild)  # 后序遍历右子树
        print(t.data, end=' ')  # 访问根结点
def LevelOrder(bt):  # 层次遍历的算法
    qu = deque()  # 将双端队列作为普通队列qu
    qu.append(bt.b)  # 根结点进队
    while len(qu) > 0:  # 队不空循环
        p = qu.popleft()  # 出队一个结点
        print(p.data, end=' ')  # 访问p结点
        if p.lchild != None:  # 有左孩子时将其进队
            qu.append(p.lchild)
        if p.rchild != None:  # 有右孩子时将其进队
            qu.append(p.rchild)
#由先序序列pres和中序序列ins构造二叉链
def CreateBTree1(pres,ins):
    bt=BTree()
    bt.b=_CreateBTree1(pres,0,ins,0,len(pres))
    return bt
def _CreateBTree1(pres,i,ins,j,n):          #被CreateBTree1调用
    if n<=0: return None
    d=pres[i]                                   #取根结点值d
    t=BTNode(d)							         #创建根结点(结点值为d)
    p=ins.index(d)                                  #在ins中找到根结点的索引
    k=p-j											#确定左子树中结点个数k
    t.lchild=_CreateBTree1(pres,i+1,ins,j,k)		    #递归构造左子树
    t.rchild=_CreateBTree1(pres,i+k+1,ins,p+1,n-k-1)	#递归构造右子树
    return t
#由后序序列posts和中序序列ins构造二叉链
def CreateBTree2(posts,ins):
    bt=BTree()
    bt.b=_CreateBTree2(posts,0,ins,0,len(posts))
    return bt
def _CreateBTree2(posts,i,ins,j,n):
    if n <= 0: return None
    d = posts[i+n-1]							        #取后序序列尾元素d
    t = BTNode(d) 						            #创建根结点(结点值为d)
    p = ins.index(d)                                  #在ins中找到根结点的索引
    k = p-j											#确定左子树中结点个数k
    t.lchild = _CreateBTree2(posts, i, ins, j, k)			#递归构造左子树
    t.rchild = _CreateBTree2(posts, i+k, ins, p+1, n-k-1)	#递归构造右子树
    return t
def PreOrderSeq(bt):
    return _PreOrderSeq(bt.b)
def _PreOrderSeq(t):
    if t == None :
        return ['#']
    s = [t.data]
    s += _PreOrderSeq(t.lchild)
    s += _PreOrderSeq(t.rchild)
    return s
def CreatBTree3(s):
     bt = BTree()
     it = iter(s)
     bt.SetRoot(_CreateBTree3(it))
     return bt
def _CreateBTree3(it):
    try :
        d =  next(it)
        if d =='#':
            return None
        t = BTNode(d)
        t.rchild = _CreateBTree3(it)
        t.lchild = _CreateBTree3(it)
        return t
    except StopIteration:
        return None
if __name__ == '__main__':
    '''第(1)问'''
    print("构造二叉树bt1:")
    pres = ['A','B','D','G','C','E','F']#先序序列
    ins =  ['D','G','B','A','E','C','F']#中序序列
    bt1=BTree()
    bt1=CreateBTree1(pres,ins)
    print("先序遍历:", end=' ');PreOrder(bt1)
    print("\n中序遍历:", end=' ');InOrder(bt1)
    print("\n后序遍历:", end=' ');PostOrder(bt1)
    print("\n层次遍历:", end=' ');LevelOrder(bt1)

    '''第(2)问'''
    print("\n构造二叉树bt2:")
    posts = ['D','E','C','B','H','G','F','A']
    ins   = ['B','D','C','E','A','F','H','G']
    bt2 = BTree()
    bt2 = CreateBTree2(posts,ins)
    print("先序遍历:", end=' ');PreOrder(bt2)
    print("\n中序遍历:", end=' ');InOrder(bt2)
    print("\n后序遍历:", end=' ');PostOrder(bt2)
    print("\n层次遍历:", end=' ');LevelOrder(bt2)
    '''第(3)问'''
    print("\n构造二叉树bt3:")
    s = 'ABC##DE#G##F###'
    bt3= BTree()
    bt3=CreatBTree3(s)
    print("先序遍历:", end=' ');PreOrder(bt3)
    print("\n中序遍历:", end=' ');InOrder(bt3)
    print("\n后序遍历:", end=' ');PostOrder(bt3)
    print("\n层次遍历:", end=' ');LevelOrder(bt3)