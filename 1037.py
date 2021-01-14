# -*- coding: utf-8 -*-

#   Coded by Sungwook Kim
#   2020-12-27
#   IDE: Jupyter Notebook

num = int(input())
arr = list(map(int, input().split()))
if len(arr) == 1:
    print(arr[0]**2)
else:
    print(min(arr) * max(arr))