# -*- coding: utf-8 -*-

#   Coded by Sungwook Kim
#   2021-01-02
#   IDE: Visual Studio Code

import sys
res = 0
for N in range(int(sys.stdin.readline())):
    s = str(sys.stdin.readline())
    tarr = [s[0]]
    t = s[0]
    res += 1
    for i in range(1, len(s)):
        if t != s[i]:
            if s[i] in tarr:
                res -= 1
                break
            tarr.append(s[i])
            t = s[i]
print(res)