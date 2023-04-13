# 토마토 보관 창고. M x N 크기의 격자 모양 상자 칸에 토마토를 하나 씩 넣고 높이 H만큼 쌓는다. 보관 하루 후, 익은 토마토들은 대각선을 제외한 위, 아래, 좌, 우, 앞, 뒤 인접한 안익은 토마토에 영향을 주어 익게 만든다.
# 혼자 저절로 익는 토마토 들은 없고, 상자 일부 칸에는 토마토가 없을 수 도 있다. 보관된 토마토들이 다 익는 최소 일수는?
# 입력 첫째줄 -> 상자의 크기 M(가로 킨 수), N(세로 킨 수), H(상자 올려지는 상자 수), 입력 둘쨰 줄 ~~ -> 가장 아래부터 가장 위의 상자 까지의 저장된 토마토 정보. 익은 토마토 1, 익지 않은 토마토 0, 토마토가 존재하지 않는 칸 -1.
# 출력 첫째줄 ~~ -> 토마토가 모두 익을 때 까지 최소 며칠이 걸리는가? 만약 저장될 대부터 모든 토마토가 익어 있다면 0, 모두 익지 않았다면 -1 출력

# 3차원 문제이므로 상하좌우면 신경쓰는 2차원 문제와 다르게 위아래의 방향도 추가해야 한다. -> 토마토 좌표 graph[x][y][z]
# today_queue 는 오늘 익은 토마토 좌표 저장 큐로, next_queue 는 내일 익을 토마토 좌표 저장 큐로 설정한다.
# 1) find_start()을 통해 제일 처음에 익은 토마토들의 위치를 찾아낸 후, next_queue 첫좌표로 저장한다. -> 카운트 시작 전날인 0일이며 익은 토마토 또한 저장한다.
# 2) 그 지점들로 부터 BFS 수행하고 일수를 표현하는 count하나씩 높인다.
# 3) 전날 next_queue 를 today_queue 로 복사해 오늘의 할당량을 준비한ㄷ.
# 4) 오늘의 할당량에서 하나씩 꺼내며 탐색한다. 이 때, next_queue 에서도 꺼내 다음날 똑같은 자리를 재탐색한다. 탐색하며 주변에 아직 익지 않은 토마토들의 상태를 익은것으로 저장하고 next_queue에 저장한다.

#파이썬 Queue는 deque로 사용해 구현한다
from collections import deque #파이썬에 내장된 collections 에서 deque 수입.
import copy #오늘 완료한 것이 내일 할당량에 포함됨으로 copy 사용을 위해 copy 수입

#입력
m, n, h = map(int, input().split())
graph = [[] for _ in range(h)]

#상하좌우앞뒤 이동
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

#전날 한걸 deque로 선언
next_queue = deque()
count = 0 #일수 초기화
flag = 0 #지점 초기화

#토마토를 담을 격자모양의상자
for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, input().split())))

#제일 처음에 익을 토마토 찾기
def find_start():
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    next_queue.append((i, j, k))

#bfs
def bfs():
    global count #전역변수로 익을 날짜 카운트 하기
    today_queue = copy.deepcopy(next_queue) #오늘한건 어제 한거를 카피해서 준비한다

    #오늘 익을 토마토
    while today_queue:
        x, y, z = today_queue.popleft()
        next_queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue
            if graph[nx][ny][nz] == 0: #안익고
                graph[nx][ny][nz] = 1 #익으면
                next_queue.append((nx, ny, nz)) #전날거에 추가
        count += 1 #하루 카운트

find_start() #젤첨익은건
while next_queue: #전날게 다 사라질때까지
    bfs() #bfs 수행

for i in range(h):
    for j in range(n):
        if 0 in graph[i][j]:
            flag = 1

if flag == 1: #만약 다 익지 못하면
    print(-1) #-1 출력
else:
    print(count - 1)