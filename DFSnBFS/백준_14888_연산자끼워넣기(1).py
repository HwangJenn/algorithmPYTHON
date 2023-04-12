# 입력 첫째 줄 -> 수의 개수 N, 입력 두벌째 줄 -> N개의 수, 입력 세번째 줄 -> 합이 N - 1인4개의 정수. 차례대로 +, -, *, / 의 개수
# 출력 첫째 줄 -> 만들 수 있는 식의 결과의 최댓값, 출력 둘째 줄 -> 최솟값
# 식의 계싼은 연산자 우선 순위 무시하고 앞에서 부터 진행한다.
# 힌트) input: 6 / 1 2 3 4 5 6 / 2 1 1 1  , output: 54 / -24 애서 최댓값: 1 - 2 / 3 + 4 + 5 * 6, 최솟값: 1 + 2 + 3 / 4 - 5 * 6

# DFS와 백트래킹을 이용해서 풀이한다. 문제 조건에 의해 숫자의 순서는 유지하고 연산자만 바꾸어주면 된다.
# 첫번째 숫자에 첫 연산자를 넣고 DFS를 수행 -> 백트래킹으로 원래 상태로 돌린다
# 두번째 연산자를 넣고 DFS 수행 -> 백트래킹
# 반복해서 모든 경우의 수를 찾아내고 찾아낸 모든 경우의 수에서 최대값, 최솟값 찾아서 출력한다.


#입력 받을 수, 범위 설정 (초기 설정)
n = int(input()) #수의 개수 입렵 받기
number = list(map(int, input().split())) #숫자 입력받기
op = list(map(int, input().split())) #연산자 수 입력받기
#최대, 최소 범위 (-10억 to 10억) 설정
minR = int(1e9)
maxR = -int(1e9)

answer = number[0] #만들 수 있는 결과 값 초기화

#dfs
def dfs(idx): #idx를 매개변수로 가지는 dfs 정의
    #함수 바깥에서도 사용하기 위한 전역변수 설정
    global answer
    global minR, maxR

    if idx == n: #if 조건문
        # 최댓값
        if answer > maxR:
            maxR = answer
        # 최솟값
        if answer < minR:
            minR = answer
        return #반환

    #백트레킹
    for i in range(4): #사칙연산 계산하기
        tmp = answer #임시 값 설정
        if op[i] > 0: #연산자가 있으면
            if i == 0: #더하기
                answer += number[idx]
            elif i == 1: #빼기
                answer -= number[idx]
            elif i == 2: #곱하기
                answer *= number[idx]
            else: #나누기
                if answer >= 0: #양수
                    answer //= number[idx]
                else: #음수/양수
                    answer = (-answer // number[idx])* -1

            #반복
            op[i] -= 1
            dfs(idx + 1)
            answer = tmp
            op[i] += 1

#결과
dfs(1)
print(maxR)
print(minR)
