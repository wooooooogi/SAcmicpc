# -*- coding: utf-8 -*-

#   Coded by Sungwook Kim
#   2019-07-29
#   IDE: Spyder 3

def fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [1]
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

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
    while True:
        try:
            N = int(input())
            print("N은 0보다 크거나 같고 40보다 작거나 같은 정수입니다.")
            if (N < 0 or N > 40):
                print("가능한 N의 범위를 벗어났습니다. 다시 입력해 주세요.")
            else:
                b = 0
                a = fibonacci(N)
                for j in a:
                    if j == 0:
                        b += 1
                print(b, len(a) - b)
                break
        except:
            pass

        
#   재귀 프로그래밍은 큰 연산에서 시간이 많이 걸리기 때문에 동적 프로그래밍 (Dynamic programming)을 사용한다.