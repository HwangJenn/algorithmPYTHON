# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력한다.
# 주어지는 정점 번호는 1 ~ N번까지이다. 단, 방문 할 정점이 여러개라면 작은것 부터 방문해야하고, 더이상 방문 할 정점이 없다면 종료한다.
# 입력 첫째줄 -> 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V, 입력 둘째줄 ~~ M번째 줄 -> 간선이 연결하는 두 정점이 번호
# 두 정점 사이에 여러개의 간선이 존재 가능하다. 입력으로 주어지는 간선은 양방향이다.
# 출력 첫째줄 -> DFS 수행 결과. 출력 둘째줄 ~~ -> BFS 수행 결과. V부터 방문된 점을 순서대로 출력한다.

# 풀이 2 -> 그래프를 인접행렬로 구현한다.
# 인접행렬은 알아서 앞에서 부터 탐색하기 때문에 정렬 할 필요 없다.
# 인접리스트에서 graph[a].append(b)로 구현한 부분을 graph[a][b] = graph[b][a]로 구현한다.

#파이썬 Queue는 deque로 사용해 구현한다
from collections import deque #파이썬에 내장된 collections 에서 deque 수입.

#dfs, bfs 함수 정의 처리 전 처리
n, m, v = map(int, input().split()) #입력받을 정점의 개수, 간선의 개수, 탐색의 시작점
graph = [[0] * n  for _ in range(n)] #n범위에 있을 그래프 초기화
visited = [False] * n #방문 정보 포함할 자료

for i in range(m): #간선의 개수만큼 반복한다
    a, b = map(int, input().split()) #두정점 입력받기
    #인접리스트와 다른 부분
    graph[a - 1][b - 1] = graph[b - 1][a - 1] = 1 #양방향 표현

#dfs
def dfs(v): #탐색을 시작할 정점의 번호를 매개변수로 가지는 dfs
    visited[v] = True #시작 정점 방문처리
    print(v + 1, end= '') #정점에 +! 꺼내오기

    for i in range(n): #정점의 개수만큼 반복
        if graph[v][i] == 1 and not visited[i]: #정점과 i 그래프에 속하거나 방문하지 않았으면
            dfs(i) #dfs 수행

#bfs
def bfs(start): #start를 매개변수로 가지는 bfs
    visited[start] = False #방문처리 하지 않음
    queue = deque() #queue를 deque선언
    queue.append(start) #queue에 start 집어넣기

    while queue: #queue안에 아무것도 안남을때까지 반복
        v = queue.popleft() #시작정점 popleft
        print(v + 1, end= '') #정점에 v+1 꺼내오기
        for i in range(n): #정점의 개수만큼 반복
            if graph[v][i] == 1 and visited[i]: #정점과 i 그래프에 속하고 방문했다면
                queue.append(i) #queue에 추가하고
                visited[i] = False #방문처리 하지 않는다

#출력
dfs(v - 1)
print()
bfs(v - 1)
