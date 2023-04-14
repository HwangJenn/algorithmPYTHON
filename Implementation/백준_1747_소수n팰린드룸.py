# 79197, 324423과 같이 어떤 수와 그 수의 숫자 순서를 뒤집은 수가 일치하는 수를 팰린드룸이라 부른다.
# 어떤 수 N이 주어졌을 때, N보다 크거나 같고, 소수이면서 팰린드룸인 수 중에서, 가장 작은 수는?
# 입력 첫째줄 -> N
# 출력 첫째줄 -> 조건을 만족하는 수

# 소수를 구하는 방법 중 하나는 i를 2부터 루트n 까지 돌면서 i로 나누어 떨어지는 경우가 존재하지 않는걸 찾는다.
# 팰린드룸은 문자열을 뒤집었을 때 일치하면 True 처리를 해준다.

import math #Math 모듈 불러오기

n = int(input()) #n값 입력받기

#소수 구하는 함수
def isPrime(x): #임의의 매개변수 x를 가지는 험수
    if x == 1: #x가 1이면
        return False #False
    for i in range(2, int(math.sqrt(x) + 1)): #x가 2보다 크고 x의 제곱근+1 범위에서
        if x % i == 0: #x를 i로 나누었을 때 0이라면
            return False #소수가 아님
    return True #해당 사항이 없다면 소수임

def isPalindrom(x): #팰린드룸인지 확인하는 함수
    xs = str(x) #x를 준자열 형태로 만들어 준다
    xsr = xs[::-1] #xs를 뒤집기
    if xs == xsr: #둘 비교해서
        return True #같으면 팰린드룸
    else: #아니면
        return False #팰린드룸이 아니다

start = n #입력 받은 n 숫자부터 시작
while True: #True가 나올 때 까지 반복
    if isPalindrom(start) and isPrime(start): #두가지 함수를 충족하면
        print(start) #해당숫자 입력
        break #탈출
    else: #아니면
        start += 1 #다음숫자