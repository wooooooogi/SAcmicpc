# -*- coding: utf-8 -*-

#   Coded by Sungwook Kim
#   2020-12-27
#   IDE: Jupyter Notebook

t = str(input())
if t[0] == '-':
    arr = t.split('-')
    res = 0
    for i in arr:
        if i == '':
            pass
        else:
            if '+' in i:
                tt = i.split('+')
                for j in tt:
                    res -= int(j)
            else:
                res -= int(i)
    print(res)
else:
    arr = t.split('-')
    res = 0
    for i in range(len(arr)):
        if i == 0:
            if '+' in arr[i]:
                tt = arr[i].split('+')
                for j in tt:
                    res += int(j)
            else:
                res += int(arr[i])
        else:
            if '+' in arr[i]:
                tt = arr[i].split('+')
                for j in tt:
                    res -= int(j)
            else:
                res -= int(arr[i])
    print(res)