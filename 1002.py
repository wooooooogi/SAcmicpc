# -*- coding: utf-8 -*-


'''
문제
조규현과 백승환은 터렛에 근무하는 직원이다.
 하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다. 다음은 조규현과 백승환의 사진이다.



이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 
조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.

조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 
조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 
류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 이루어져 있다.

한 줄에 x1, y1, r1, x2, y2, r2가 주어진다. x1, y1, x2, y2는 -10,000보다 크거나 같고, 
10,000보다 작거나 같은 정수이고, r1, r2는 10,000보다 작거나 같은 자연수이다.

출력
각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다. 
만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.
'''

'''
조규현, 백승환의 좌표를 기준으로 하는 두 원을 구하고
두 원의 관계를 파악하는 문제
1. 무식한 방법
    -  -10000 ~ 10000까지 모든 좌표와 원의 중심의 좌표 사이의 거리를 구해 그 거리가 원의 반지름인 경우를 파악
    -  시간이 너무 많이 걸려서 실패
    for i in range(20001):
        for j in range(20001):
            tmpR = pow((i - 10000 - Jx), 2) + pow((j - 10000 - Jy), 2)
            if tmpR == Jr:
                JlistX.append(i-10000)
                JlistY.append(j-10000)
2. 사각형 내 계산
    -  앞의 방법을 응용한 것, 원의 중심에서 i, j값을 r만큼만 계산
    -  Resolution 을 설정해도 측정하지 못하는 부분이 생김. + Resolution 값이 너무 커지면 연산 속도 느
    resolution = 100
    for i in range(resolution * (2*Jr+1)):
        for j in range(resolution * (2*Jr+1)):
            tmpJr = pow(float(Jx + (i/resolution - Jr)), 2) + pow(float(Jy + (j/resolution - Jr)), 2)
            if tmpJr == Jr:
                Jlist.append([i-Jr, j-Jr])
                
    for i in range(resolution * (2*Br+1)):
        for j in range(resolution * (2*Br+1)):
            tmpBr = pow(float(Bx + (i/resolution - Br)), 2) + pow(float(By + (j/resolution - Br)), 2)
            if tmpBr == Br:
                Blist.append([i-Br, j-Br])  
3. 거리 계산 알고리즘 사용
    -  중심 사이 거리와 반지름에 관한 식 세우기
       중심 사이 거리 == 두 반지름의 합 -> k = 1
       중심 사이 거리 > 두 반지름의 합 -> k = 2
       중심 사이 거리 < 두 반지름의 합 -> k = -1
       # d1: distance between two centers
       # d2: sum of two radius
        d1 = (Jx - Bx)**2 + (Jy - By)**2
        d2 = (Jr + Br)**2
        # Which is faster, sqrt or **2?
        if d1 == d2:
            print(1)
        elif d1 > d2:
            print(-1)
        else:
            print(2)
        한 원이 다른 원 내부에 있을 때 문제가 생김
    -   한 원의 중심이 다른 원 내부에 있는지 파악. 성공
'''

#   Lee, Jo, Baek
import math
print("테스트 케이스를 입력하시오. (소수점 아래 숫자는 자동으로 버립니다.)")
while True:
    try:
        T = int(input())
        if (T <= 0):
            print("테스트 케이스는 정수입니다.")
        else:
            break
    except:
        pass
for i in range(T):
    k = 0
    while k < 6:
        print("조규현의 좌표(x1, y1)와 조규현이 계산한 류재명과의 거리(r1), 백승원의 좌표(x2, y2)와 백승완이 계산한 류재명과의 거리(r2)를 입력하시오.")
        k = 0
        try:
            Jx, Jy, Jr, Bx, By, Br = map(int, input().split())
            for i in [Jx, Jy, Bx, By]:
                if -10000 > i or i > 10000:
                    print("숫자 범위를 벗어났습니다. 다시 입력하시오.")
                else:
                    k += 1
            for i in [Jr, Br]:
                if 1 > i or i > 10000:
                    print("숫자 범위를 벗어났습니다. 다시 입력하시오.")
                else:
                    k += 1
        except:
            print("좌표와 거리를 다시 입력하시오")
    # d1: distance between two centers
    # d2: sum of two radius
    d1 = math.sqrt((Jx - Bx)**2 + (Jy - By)**2)
    d2 = (Jr + Br)
    # Which is faster, sqrt or **2?
    
    #   이 위에는 한 원의 중심이 다른 원 밖에 위치할 때 만족
    #   한 원의 중심이 다른 원 내부에 있는지 파악해야 함 
    if d1 < Jr or d1 < Br:
        if Br < Jr:
            if d1 + Br < Jr:
                print(0)
            elif d1 + Br == Jr:
                print(1)
            else:
                print(2)
        elif Br > Jr:
            if d1 + Jr < Br:
                print(0)
            elif d1 + Jr == Br:
                print(1)
            else:
                print(2)
        elif Br == Jr:
            if Bx == Jx and By == Jy:
                print(-1)
            else:
                print(2)
    else:
        if d1 == d2:
            print(1)
        elif d1 > d2:
            print(0)
        else:
            print(2)