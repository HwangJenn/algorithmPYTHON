# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력한다.
# 주어지는 정점 번호는 1 ~ N번까지이다. 단, 방문 할 정점이 여러개라면 작은것 부터 방문해야하고, 더이상 방문 할 정점이 없다면 종료한다.
# 입력 첫째줄 -> 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V, 입력 둘째줄 ~~ M번째 줄 -> 간선이 연결하는 두 정점이 번호
# 두 정점 사이에 여러개의 간선이 존재 가능하다. 입력으로 주어지는 간선은 양방향이다.
# 출력 첫째줄 -> DFS 수행 결과. 출력 둘째줄 ~~ -> BFS 수행 결과. V부터 방문된 점을 순서대로 출력한다.

# 풀이 1 -> 그래프를 인접리스트로 구현한다.
# graph[a].append(b)의 의미는 a에 b번 연결시킨다는 뜻임. -> 1번에 2, 3, 4가 연결되어 있으면 graph의 1번행에 2, 3, 4가 추가된다.
# 그리고 문제에서, 번호가 작은 것 부터 탐색하라 했으므로 정렬해야한다.

#파이썬 Queue는 deque로 사용해 구현한다
from collections import deque #파이썬에 내장된 collections 에서 deque 수입.

#dfs, bfs 함수 정의 처리 전 처리
n, m, v = map(int, input().split()) #입력받을 정점의 개수, 간선의 개수, 탐색의 시작점
graph = [[] * (n + 1) for _ in range(n + 1)] #n+1 값을 무시할 graph
visited = [False] * (n + 1) #방문 정보 포함할 자료

#두 정점을 연결함
for i in range(m): #간선의 개수만큼 반복한다.
    a, b = map(int, input().split()) #입력 받은 두 정점
    #양방향 연결
    graph[a].append(b) #a에 b연결
    graph[b].append(a) #b에 a연결
    #오름차순 정렬
    graph[a].sort()
    graph[b].sort()

#dfs
def dfs(graph, visited, v): #graph, visited, v를 매개변수로 가지는 dfs정의
    visited[v] = True #탐색시작점 방문처리
    print(v, end= '') #정점 v에서 list 요소 꺼내오기

    for i in range(len(graph[v])): #탐색 시작점 크기만큼 시작으로 반복한다.
        if not visited[graph[v][i]]: #방문하지 않은 곳이 있다면
            dfs(graph,visited,graph[v][i]) #dfs 수행한다

#bfs
def bfs(graph, visited, v): #graph, visited, v를 매개변수로 가지는 bfs정의
    queue = deque() #queue에 deque선언
    queue.append(v) #queue 맨 뒤에 탐색시작점을 삽입한다.
    visited[v] = False #탐색시작점 방문처리 하지 않는다.

    while queue: #queue내에 아무것도 남지 않을 때 까지 반복한다
        cur = queue.popleft() #queue의 맨왼쪽 popleft
        print(cur, end= '') #cur로 꺼내오기
        for i in range(len(graph[cur])): #cur그래프 크기 내에서
            if visited[graph[cur][i]]: #cur i 이차원 그래프 방문하면
                queue.append(graph[cur][i]) #queue 맨 뒤에 추가한다
                visited[graph[cur][i]] = False #방문처리 하지 않는다

#출력하기
dfs(graph, visited, v)
print()
bfs(graph, visited, v)