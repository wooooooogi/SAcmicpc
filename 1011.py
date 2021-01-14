# -*- coding: utf-8 -*-

#   Coded by Sungwook Kim
#   2021-01-02
#   IDE: Visual Studio Code

import sys
for T in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    t = y - x
    trig = 0
    i = 1
    res = 0
    while t > 0:
        if trig < 2:
            t -= i
            trig += 1
            res += 1
        elif trig == 2:
            trig = 0
            i += 1
    print(res)