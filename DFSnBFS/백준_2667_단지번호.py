# 지도에서 1은 집이 있고, 0은 집이 없는 곳이다.
# 대각선 연결을 제외하고 좌우, 위아래 연결 된 집을 묶어 단지라고 부른다. 단지 몇개? 각 단지 별 집 몇개?
# 입력 첫째 줄 -> 지도의 크기 N, 입력 둘째 줄 ~~ -> N개의 자료(0 또는 1)
# 출력 첫째 줄 -> 총 단지 수, 출력 둘째 줄 ~~ -> 각 단지내 집의 수, 오름차순으로 정렬

# BFS 이용으로 전체를 돌면서 탐색한다.
# 탐색 중 1인 부분은 방문 후 0으로 바꿔 다시 방문하지 않는다. 한번의 탐색이 끝나면 단지 하나로 카운트 한다.

# 파이썬 Queue는 deque로 사용해 구현한다
from collections import deque # 파이썬에 내장된 collections 에서 deque 수입.

#각 집으로 이동 할 좌표
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

#bfs(graph, a, b)함수 정의 전 처리
n = int(input()) #테스트 케이스 개수 입력 받기
graph = [] #이동횟수를 기록 할 그래프
for i in range(n): #테스트 개수만큼 반복 한다.
    graph.append(list(map(int, input()))) #위치를 입력받고 그래프에 추가한다.

#bfs
def bfs(graph, a, b): #매개변수 graph, a, b를 가지는 bfs 함수 정의
    n = len(graph) #지도의 크기 -> len을 이용해 공백 포함 한 그래프로 변환한다.
    queue = deque() #queue를 deque로 초기화
    queue.append((a, b)) #queue 맨 끝에 새로운 요소 a, b 추가
    graph[a][b] = 0 #2차원 배열의 그래프
    count = 1 #단지 수 초기화

    while queue: #queue내에 아무것도 안남을 때 까지 반복한다.
        x, y = queue.popleft() #x,y는 queue에서 popleft한 값이다.
        for i in range(4): #햔재 위치 기준으로 4방향 모두 구하기
            #햔재 값 + 이동위치 = 신규위치
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: #범위 안에 위치안하면
                continue #while문으로 돌아감
            if graph[nx][ny] == 1: #방문했으면
                graph[nx][ny] = 0 #다시 방문하지 않게 0으로 바꾼다
                queue.append((nx, ny)) #현재 위치를 queue에 추가하고
                count += 1 #단지 수를 1카운트 한다.
    return count #단지 수 반환하기

count = [] #단지
for i in range(n): #케이스 개수만큼 반복한다.
    for j in range(n):
        if graph[i][j] == 1: #이차원 리스트 그래으가 1이면
            count.append(bfs(graph, i, j)) #bfs함수 실행한 횟수를 추가한다.

count.sort() #단지내 집의 수 오름차순 정렬
print(len(count)) #단지 수 출력
for i in range(len(count)): #단지 후 만큼
    print(count[i]) #단지내 집의 수 출력.
