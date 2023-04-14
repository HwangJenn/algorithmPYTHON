# N+1개의 I와 N개의 O으로 이루어져 있으면 I와 O 교대로 나오는 문자열을 Pn이라고 한다.
# I 와 O으로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 Pn이 몇군데 포함?
# 입력 첫째줄 -> N, 입력 둘째줄 -> S의 길이 M, 입력 셋째 줄 -> S
# 출력 첫째줄 -> S에 Pn이 몇군데 포함되어 있는가

# 문자열 S를 for문을 돌면서 I를 만날 경우 현재 인덱스를 stack에 넣어준다.
# stack의 각 원소들의 차이가 2인 경우는 i가 한칸 띄어져 있다는 말이므로 -> IOI, 이런 경우에 count를 하나씩 늘려준다.

import sys #sys 모듈 불러오기
n = int(input()) #n값 입력받기
m = int(input()) #m값 입력받기
s = sys.stdin.readline() #s값 입력받기

count = 0 #카운트 초기화
answer = 0 #answer 초기화
stack = [] #stack 초기화

for i in range(m): #길이 m 범위까지
    if s[i] == "O": #입력받은 문자열에 O가 포함되어 있다면
        continue
    else: #반대로 I가 포함되어 있다면
        stack.append(i) #stack에 i추가하기

for i in range(1, len(stack)): #stack에 들어 있는 i 위치까지
    if stack[i] - stack[i - 1] == 2: #i와 그 전 원소의 차이가 2라면
        count += 1 #카운트
    else: #아니라면
        count = 0 #카운트 하지 않음

    if count >= n: #카운트 한 수가 n 이상이라면
        answer += 1 #answer에 1추가

print(answer)