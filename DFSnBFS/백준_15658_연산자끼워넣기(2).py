# 입력 첫째 줄 -> 수의 개수 N, 입력 두벌째 줄 -> N개의 수, 입력 세번째 줄 -> 합이 N - 1인4개의 정수. 차례대로 +, -, *, / 의 개수
# 출력 첫째 줄 -> 만들 수 있는 식의 결과의 최댓값, 출력 둘째 줄 -> 최솟값
# 식의 계싼은 연산자 우선 순위 무시하고 앞에서 부터 진행한다.
# 힌트) input: 6 / 1 2 3 4 5 6 / 2 1 1 1  , output: 54 / -24 애서 최댓값: 1 - 2 / 3 + 4 + 5 * 6, 최솟값: 1 + 2 + 3 / 4 - 5 * 6

# 연산자끼워넣기(1)처럼 DFS와 백트레킹 풀이가 가능하다.
# 연산자끼워넣기(2)의 풀이는 변수로 변하는 모든 변수를 넘겨준다.
# 핵심은 주어진 숫자와 연산자로 조합할 수 있는 모든 경우의 수를 따져야 한다.

#입력 받을 수, 범위 설정 (초기 설정)
n = int(input()) #수의 개수 입렵 받기
num = list(map(int, input().split())) #숫자 입력받기
plus, minus, mul, div = map(int, input().split()) #연산자 입력받기

#최대, 최소 범위 (-10억 to 10억) 설정
myMAX = -int(1e9)
myMin = int(1e9)

#dfs
def dfs(index, result, plus, minus, mul, div): #dfs함수 정의, 매개변수 설정
    global myMAX, myMin #전역변수 설정
    if index == n: #수의 개수와 일치 할 때
        #최대, 최솟값
        myMAX = max(myMAX, result)
        myMin = min(myMin, result)
        return
    if plus > 0: #+계수가 0보다 크면
        dfs(index + 1, result + num[index], plus - 1, minus, mul, div)
    if minus > 0: #-계수가 0보다 크면
        dfs(index + 1, result - num[index], plus, minus - 1, mul, div)
    if mul > 0: #*계수가 0보다 크면
        dfs(index + 1, result * num[index], plus, minus, mul - 1, div)
    if div > 0: #/계수가 0보다 크면
        dfs(index + 1, int(result//num[index]), plus, minus, mul, div - 1)

#결과
dfs(1, num[0], plus, minus, mul, div)
print(myMAX)
print(myMin)