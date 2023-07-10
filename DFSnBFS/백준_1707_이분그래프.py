# 그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할 할 수 있을 때, 그러한 그래프를 특별히 이분 그래프라고 부른다
# 그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하라
# 입력 찻째줄 -> 테스트 케이스의 개수 k, 입력 둘째줄(각 테스트 케이스 첫째줄) -> 그래프의 정점ㅇ의 개수 v, 간선의 개수 e, 입력 셋째줄(각 테스트 케이스 둘째줄 ~ e) -> 각 줄에 인접한 두 정점의 번호 u, v
# 출력 -> k줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 yes, 아니면 no

# 그래프의 정점을 두가지 색으로 칠할 때, 인접한 정점끼리는 다른 색을 가지고 있는 그래프
# visited[v] 1,2의 값을 줌으로 정점의 색 구분, 미방분 0으로. bfs 전에 인접행렬로 그래프 만들고 탐색한다.
# 연결 그래프는 시작점에서 bfs, 비연결 그래프의 경우 시작점과 연결되지 못한 정점은 탐색 수행을 하지 못해서 for k in range(1, v+1)를 통해 모든 정점에서 bfs


from collections import deque

k = int(input())

def bfs(graph, start):
    queue = deque()
    queue.append(start)
    if visited[start] == 0:
        visited[start] = 1
    while queue:
        v = queue.popleft()

        color = visited[v]
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                if color == 1:
                    visited[i] = 2
                else:
                    visited[i] = 1
            elif visited[i] == 1:
                if color == 1:
                    print("NO")
                    return False
            elif visited[i] == 2:
                if color == 2:
                    print("NO")
                    return False
    return True

for i in range(k):
    flag = 0
    v, e = map(int, input().split())
    graph = [[]for _ in range(v + 1)]
    visited = [0] * (v + 1)
    for j in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for k in range(1, v + 1):
        if not bfs(graph, k):
            flag = 1
            break
    if flag == 0:
        print("YES")