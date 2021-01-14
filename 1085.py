# -*- coding: utf-8 -*-

#   Coded by Sungwook Kim
#   2020-12-24
#   IDE: Jupyter Notebook

x, y, w, h = map(int, input().split())
if y / h > 0.5:
    t1 = h - y
else:
    t1 = y
if x / w > 0.5:
    t2 = w - x
else:
    t2 = x
if t1 > t2:
    print(t2)
else:
    print(t1)