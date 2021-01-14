# -*- coding: utf-8 -*-

#   Coded by Sungwook Kim
#   2020-12-14
#   IDE: Jupyter Notebook

N = int(input())
def num(N):
    b = N
    while True:
        if b >= 10:
            b = b - 10
        else:
            break
    return b
k = -1
res = 0
trig = False
while True:
    if trig == False:
        b = num(N)
        a = int((N -b) / 10)
        c = a + b
        d = num(c)
        k = b * 10 + d
        trig = True
    else:
        if N == k:
            break
        else:
            b = num(k)
            a = int((k - b) / 10)
            c = a + b
            d = num(c)
            k = b * 10 + d
    res += 1
print(res)