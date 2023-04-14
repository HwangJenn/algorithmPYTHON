# 베르트랑 공준은 임의의 자연수 n에 대해, n 보다 크고, 2n 보다 작거나 같은 소수는 적어도 하나 존재한다.
# 자연수 n이 주어졌을 때, n 보다 크고, 2n 보다 작거나 같은 소수의 개수를 구하라.
# 입력 첫째줄 ~~ -> 테스트 케이스들 각줄엔 n, 입력 마지막줄 -> 0
# 출력 첫째줄 ~~ -> 입력 테스트 케이스에 대해 n보다 크고, 2n보다 작거나 같은 소수의 개수 출력

# 소수를 골라내야한다
# 제곱근을 기준으로 대칭을 이루기에 제곱근까지만 확인한다
# n 보다 큼: n + 1, 부터 2n까지 범위에서 소수 구하기

import math #math 모듈 불러오기

def isPrime(x): #x 소수 판별하기
    if x == 1: #x가 1이라면
        return False #거짓
    for i in range(2, int(math.sqrt(x) + 1)): #i의 범위가 2보다 크고 제곱근 +1이라면
        if x % i == 0: #x를 i로 나누었을 때 0이라면
            return False #거짓
    else: #위 두 거짓 조건에 부합하지 않으면
        return True #참

while True: #참이 될때까지 반복한다
    n = int(input()) #자연수 n 입력받기
    if n == 0: #입력 마지막줄에 n 이 0이면 탈출조건이였음
        break
    count = 0 #count 초기하
    for i in range(n + 1, 2 * n + 1): #문제 조건에 따라 n보다 크고 2n보다 작거나 같은 범위
        if isPrime(i): #소수 판별
            count += 1 #카운트 1
    print(count)