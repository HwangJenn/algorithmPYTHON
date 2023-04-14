# 골드바흐의 추측은 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다. 이 수를 골드바흐의 수라고 표현한다.
# 짝수를 두 소수의 합으로 나타낸 표현을 그 수의 골드바흐 파티션이라고 한다.
# 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하라. 만약 가능한 n의 골드바흐 파티션이 여러가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.
# 입력 첫째줄 -> 테스트 케이스의 개수 T, 입력 둘째줄 ~~ -> 각 테스트 케이스인 짝수 n
# 출력 첫째줄 ~~ -> 각 테스트 케이스에 대해 주어진 n의 골드바흐파티션. 작은것 부터 출력하고 공백 구

# 소수 판별 잘하면 된다.
# 골드파티션은 a + b의 형식으로 나타내고 a는 2부터 x/2 까지의 수 중 소수인 수임(짝수), b는 x - a 이며 소수이다.
# 문제의 조건에서 골드파티션이 여러가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력하라 했으므로 대소관계 구별을 해 값을 갱신시키면 된다.

import math #math 모듈 불러오기

def isPrime(x): #소수판별하기
    if x == 1: #x값이 1이면
        return False #거짓
    for i in range(2, int(math.sqrt(x) + 1)): #2부터 x의 제곱근+1한 값까지
        if x % i == 0: #i로 나눈 값이 0이면
            return False #거짓
    return True #이외 참

def goldPartition(x): #골드파티션 정의하기
    result = [] #골드파티션 표현할 결과값 초기화
    for i in range(2, x//2 + 1): #2부터 x를 2로 나눈(짝수) +1한 값 까지(짝수 포함_
        if isPrime(i) and isPrime(x - i): #i + x - i = x
            if not result: #result가 아닌 경우 출력
                result.append(i) #i를 result에 추가
                result.append(x-i) #x - i를 result에 추가
            else: #reslt 라면
                if result[1] - result[0] > x - 2 * i: #result[1] - result[0]이 x - 2 * i 보다 크다면(대소관계)
                    result[0] = i #result의 앞요소 i
                    result[1] = x - i #result의 뒷요소 x - u
    return result
t = int(input()) #테스트케이스 입력받기

for i in range(t): #테스트 케이스 개수만큼 반복
    n = int(input()) #n 입력받기
    answer = goldPartition(n) #골드파티션을 통해 출력할 값값

    print(*answer) #result 출력할 때 []떼고 출력함