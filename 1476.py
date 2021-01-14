# -*- coding: utf-8 -*-

#   Coded by Sungwook Kim
#   2020-12-30
#   IDE: Jupyter Notebook

e, s, m = map(int, input().split())
for i in range(1, 15 * 28 * 19 + 1):
    if i % 15 == e or (i % 15 == 0 and e == 15):
        if i % 28 == s or (i % 28 == 0 and s == 28):
            if i % 19 == m or (i % 19 == 0 and m == 19):
                print(i)

### Alternative code
a = list(map(int, input().split()))
arr = [15, 28, 19]
N = arr[0] * arr[1] * arr[2]
n = [int(N / arr[0]), int(N / arr[1]), int(N / arr[2])]
u = [13, 17, 10]
x = 0
for i in range(3):
    x += (a[i] * n[i] * u[i])
res = x % N
if res == 0:
    print(N)
else:
    print(res)