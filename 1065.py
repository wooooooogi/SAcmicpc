# -*- coding: utf-8 -*-

#   Coded by Sungwook Kim
#   2020-12-15
#   IDE: Jupyter Notebook

N = int(input())
if N < 100:
    print(N)
else:
    res = 99
    for i in range(N - 99):
        s = str(N - i)
        if int(s[0]) - int(s[1]) == int(s[1]) - int(s[2]):
            res += 1
    print(res)