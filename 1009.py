# -*- coding: utf-8 -*-

#   Coded by Sungwook Kim
#   2020-12-13
#   IDE: Jupyter Notebook

def F(a, b):
    if a == 1:
        return 1
    elif a > 10:
        while a > 10:
            aStr = str(a)
            aLen = len(aStr)
            a = a - pow(10, aLen - 1)
    if a == 0 and b != 0:
        return 10
    elif a == 6 and b != 0:
        return 6
    elif a == 5 and b != 0:
        return 5
    else:
        a = a
        if b == 0:
            return 1
        elif b > 100:  # a가 2, 4, 8, 9 가능 3, 7은 4번 마다, 5, 6, 1은 무조건 가능. 10은 조정 해놓음
            while b > 100:
                bStr = str(b)
                bLen = len(bStr)
                b = b - pow(10, bLen - 1)
        res = pow(a, b)
        if res >= 10:
            while res >= 10:
                resStr = str(res)
                resLen = len(resStr)
                res = res - pow(10, resLen - 1)
        if res == 0:
            return 10
        else:
            return res

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(F(a, b))