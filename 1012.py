# -*- coding: utf-8 -*-

#   Coded by Sungwook Kim
#   2021-01-04
#   IDE: Visual Studio Code

import sys
sys.setrecursionlimit(10000)
def DFS(i, j):
    arr[i][j] = -1
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for k in range(4):
        if arr[i + dx[k]][j + dy[k]] == 1:
            DFS(i + dx[k], j + dy[k])
for T in range(int(sys.stdin.readline())):
    M, N, K= map(int, sys.stdin.readline().split())
    arr = [[0 for i in range(N + 2)] for j in range(M + 2)]
    for i in range(K):
        tarr = list(map(int, sys.stdin.readline().split()))
        arr[tarr[0] + 1][tarr[1] + 1] = 1
    res = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if arr[j][i] == 1:
                DFS(j, i)
                res += 1
    print(res)