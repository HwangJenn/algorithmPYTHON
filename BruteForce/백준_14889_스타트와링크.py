# 축구를 하기 위해 모인 사람은 총 n명이고 n은 짝수이다. n/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나누어야 한다.
# 사람의 번호를 1부터 n까지로 배정하고 능력치를 조사한다.능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 팀의 능력치는 모든 쌍 능력치의 합이다.
# Sij는 Sji와 다를 수 있고 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.
# 팀간 능력치의 차이의 최솟값을 출력하라
# 입력 첫째줄 -> n, 입략 둘째줄 ~ n+1 -> S가 주어짐.
# 출력 첫째줄 -> 스타트 팀과 링크 팀의 능력치의 차이의최솟값을 출력하라.

# 모든 능력치를 탐색한다.

from itertools import combinations #조합을 이용하기 위해 조합 불러오기

n = int(input()) #입력받을 n
graph = [] #입력 받을 배열로 주어지는 시너지
number = [i for i in range(n)]

minR = int(1e9) #최솟값 범위 설정

for i in range(n):
    graph.append(list(map(int, input().split()))) #시너지입력받기

for c in combinations(number, n//2): #조합 이용해 경우의 수 구하기
    visited = [False] * n
    teamS = []
    teamL = []
    for i in c:
        visited[i] = True
        teamS.append(i)

    for i in range(n):
        if not visited[i]:
            teamL.append(i)

    sumS = 0
    sumL = 0
    for i in range(n // 2): #각 경우의 수에 따른 시너지 구하기
        for j in range(n // 2):
            if graph[teamS[i]][teamL[j]] != 0:
                sumS += graph[teamS[i]][teamS[j]]
            if graph[teamL[i]][teamL[j]] != 0:
                sumL += graph[teamL[i]][teamL[j]]

    if abs(sumS - sumL) < minR:
        minR = abs(sumS - sumL)

print(minR)