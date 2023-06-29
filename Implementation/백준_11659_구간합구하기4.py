# 수 n개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하라
# 입력 첫쨰줄 -> 수의 개수 n과 합을 구해야 하는 횟수 m, 입력 둘째줄 -> n개의 수, 입력 셋째줄 ~ m+2 -> 합을 구해야하는 구간 i, j

# 누적합으로 풀기. n개의 수를 입력받으면 n길이의 리스트를 만들고 리스트 각 자리에 그 자리까지의 누적합을 저장 후 각 자리의 누적합에서 빼는 구간합 구하기
# 맨처음 리스트에 0을 넣어 인덱스를 맞춘다

import sys
input = sys.stdin.readline

n, m = map(int, input().split()) #입력받을 n, m
nums = list(map(int, input().split())) #입력 받은 수 리스트에 저장
pre = [0] #맨처음 리스트에는 0
mysum = 0 #누적합 초기화

for i in range(n): #수개수만큼
    mysum += nums[i] #누적합
    pre.append(mysum) #저장

for i in range(m): #합 구해야하는 수 만큼
    i, j = map(int, input().split()) #구간
    print(pre[j] - pre[i - 1]) #누적합에서 빼주는 식으로 구간합 구하기