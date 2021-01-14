# -*- coding: utf-8 -*-

#   Coded by Sungwook Kim
#   2020-12-23
#   IDE: Jupyter Notebook

X = int(input())
t = 1
res = 0
if X == 1:
    print('1/1')
else:
    while True:
        res += t
        t += 1
        if X > res and X <= res + t:
            k = X - res
            if t % 2 != 0:
                print('{}/{}'.format(t - k + 1, k))
            else:
                print('{}/{}'.format(k, t - k + 1))
            break