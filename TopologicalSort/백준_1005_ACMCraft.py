# 다이나믹한 게임 진행을 위해 건물 짓는 순서가 정해져있지 않기에 첫번째 게임과 두번째 게임이 건물을 짓는 순서가 다를 수 있다.
# 매 게임시작시 건물을 짓는 순서가 주어지고 모든 건물은 각각 건설을 시작해 완성이 될 때까지 Delay가 존재한다.
# 특정건물을 가장 빨리 지을 때까지 걸리는 최소 시간을 알아내는 프로그램을 작성하라
# 입력 첫째줄 -> 테스트케이스 개수 T, 입력 테스트케이스 첫째줄 ~ -> 건물의 개수 n과 건물간의 건설순서 규칙의 총 개수 k, 입력 테스트케이스 둘째줄 -> 각 건물당 건설에 걸리는 시간, 입력 테스트케이스 셋째줄 ~ k+2 -> 건설순서 x y, 입력 테스트케이스 마지막줄 -> 승리하기 위해 건설해야할 건물의 번호 w

# 선수관계 표현을 위해 위상정렬 알고리즘 사용
# 한 지점에 들어오는 경로가 두개이상이라면 그 경로중 최댓값을 저장하기 위해 dp를 이용한다

import sys
from collections import deque

t = int(sys.stdin.readline()) #입력받을 테스트케이스의 수 t

for _ in range(t): #테스트케이스의 수 만큼
    n, k = map(int, sys.stdin.readline().rstrip().split()) #입력받을 각 테스트 n, k
    d = list(map(int, sys.stdin.readline().rstrip().split())) #입력받을 각 건물당 건설에 걸리는 시간
    graph = [[] for _ in range(n + 1)] #건설순서를 저장하기 위해 배열 사용
    inDegree = [0 for _ in range(n + 1)] #간살에 걸리는 시간
    dp = [0 for _ in range(n + 1)] #경로중 최댓값을 저장하기 위해 사용하는 dp
    queue = deque() #선수괸계

    for i in range(k): #건설순서 규칙의 총 개수 만큼
        x, y = map(int, sys.stdin.readline().rstrip().split()) #입력받을 건설순서
        graph[x].append(y)
        inDegree[y] += 1

    w = int(sys.stdin.readline().rstrip()) #승리하기 위해 건설해야 할 건물의 번호

    for i in range(1, n + 1): #건물이 0이 아닌 1부터 시작이기에 n+1 해준다
        if inDegree[i] == 0:
            queue.append(i)
            dp[i] = d[i - 1]

    while queue: #순서에 따라 건물 짓기
        tmp = queue.popleft()

        for i in graph[tmp]:
            inDegree[i] -= 1
            dp[i] = max(dp[i], dp[tmp] + d[i - 1])
            if inDegree[i] == 0:
                queue.append(i)

    print(dp[w])