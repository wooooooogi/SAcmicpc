# -*- coding: utf-8 -*-

#   Coded by Sungwook Kim
#   2020-12-13
#   IDE: Jupyter Notebook

def Fact(a):
    res = 1
    for i in range(a):
        res = res * (i + 1)
    return res

T = int(input())
for i in range(T):
    r, n = map(int, input().split())

    a = Fact(n)
    b = Fact(r)
    c = Fact(n-r)

    print(int(a / (c * b)))