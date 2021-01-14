# -*- coding: utf-8 -*-

#   Coded by Sungwook Kim
#   2020-12-27
#   IDE: Jupyter Notebook

x = int(input())
res = 0
for i in range(6, -1, -1):
    if x >= 2**i:
        x -= 2**i
        res += 1
print(res)