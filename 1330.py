# -*- coding: utf-8 -*-

#   Coded by Sungwook Kim
#   2020-12-14
#   IDE: Jupyter Notebook

a, b = map(int, input().split())
if a < b:
    print('<')
elif a == b:
    print('==')
else:
    print('>')