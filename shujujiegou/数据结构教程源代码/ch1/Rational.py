# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 15:28:38 2021

@author: huanglili
"""

class Rational:
    def __init__(self, num, den=1):
        self._num = num
        self._den = den
        
    def __add__(self,another): # mimic + operator
        den = self._den * another.GetDen()
        num = self._num * another.GetDen() + self._den * another.GetNum()
        return Rational(num,den)
    
    def __mul__(self,another): # mimic * operator
        den = self._den * another.GetDen()
        num = self._num *  another.GetNum()
        return Rational(num,den)
    
    def __floordiv__(self,another): # mimic // operator
        if another.GetNum() == 0:
            raise ZeroDivisionError
        den = self._den * another.GetNum()
        num = self._num *  another.GetDen()
        return Rational(num,den)
    
    def GetNum(self):
        return self._num
    
    def GetDen(self):
        return self._den
    
# .......................
# 其他元素安抚可以类似定义：
# -:__sub__; /:__truediv__;%:__mod__, etc.


        