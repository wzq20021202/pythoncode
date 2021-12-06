# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 20:20:55 2021
@author: 30337
"""
# 变位词判断问题
from timeit import Timer
def anagramSolution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s1[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    j = 0
    stillok = True
    while j < 26 and stillok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillok = False
    return stillok

print(anagramSolution4('python', 'tython'))
t1 = Timer("anagramSolution4('python','tython')",
           "from __main__ import anagramSolution4")
print("concat %f second\n" % t1.timeit(number=1000))
