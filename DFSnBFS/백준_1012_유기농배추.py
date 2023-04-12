# 지도에서 1은 배추가 있고, 0은 배추가 없는 곳이다.
# 어떤 배추에 배추흰지렁이가 한마리라도 살고 있으면 대각선을 제외한 상하좌우에 있는 배추를 지킬 수 있다. 몇 마리의 지렁이가 필요?
# 입력 첫째 줄 -> 테스트 케이스의 개수 T, 케이스 첫째 줄 -> 배추밭의 가로길이 M, 세로길이 N, 배추가 심어져 있는 위치의 개수 K, 케이스 둘째줄 ~~ -> 배추의 위치 X, Y
# 출력 -> 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리수

# 백준_2667_단지번호 문제와 동일한 방법으로 풀이가 가능하다.
# BFS 이용으로 전체를 돌면서 탐색한다.
# 1이 인접 칸들 연결한다 -> 한 구역을 선택해 가정한다 -> 구역 당 지렁이 1마리가 필요한다. -> 1 인 칸 발견 -> BFS 수행 -> 해당 구역 0으로 바꾸고 카운트 +1 한 다음 재방문X

# 파이썬 Queue는 deque로 사용해 구현한다
from collections import deque # 파이썬에 내장된 collections 에서 deque 수입.

#각 배추로 이동 할 좌표
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

t = int(input()) #테스트 케이스 개수 입력 받기

#bfs(graph, a, b)함수 정의 전 처리
for i in range(t): #테스트 케이스 개수만큼 반복
    count = 0 #지렁이 수 초기화
    n, m, k = map(int, input().split()) #입력 지도의 가로, 세로 길이, 배추의 위치의 개수
    graph = [[0] * m for _ in range(n)] #입력받은 지도의 길이 범위내에서 그래프 그리기

    for j in range(k): #배추 위치의 개수 범위만큼 반복
        x, y = map(int, input().split()) #배추의 위치 입력받기
        graph[x][y] = 1 #배추의 위치에 1 입력하기

#bfs
def bfs(graph, a, b): #매개변수 graph, a, b를 가지는 bfs 함수 정의
    queue = deque() #queue는 deque()로 초기화
    queue.append((a,b)) #queue에 a,b 삽입 한다
    graph[a][b] = 0 #이차원 그래프 표현

    while queue: #queue에 아무것도 남지 않을 때 까지 반복한다.
        x, y = queue.popleft() #queue에서 popleft한 요소들을 x, y에 배치
        for i in range(4): #현재 위치에서 4방향으로 이동 가능
            #신규위치 = 현재위치 + 이동위치
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: #지도 안에 없으면
                continue #반복문 돌아간다
            if graph[nx][ny] == 1: #배추가 있는곳에 방문하면
                graph[nx][ny] = 0 #재방문 방지를 위해 0 처리
                queue.append((nx, ny)) #queue에 신규위치 추가
    return


for a in range(n): #배추 밭 세로 길이 범위와
        for b in range(m): #배추 밭 가로길이 범위에서
            if graph[a][b] == 1: #배추가 있다고 하면
                bfs(graph, a, b) #bfs 실행
                count += 1 #지렁이 수 카운트

print(count) #지렁이 수 출력
