# 바이러스 확산을 막기 위해 연구소에 벽 세우기. N x M 크기의 직사각형 연구소임. 1 x 1 크기의 정사각형이 모여있는 구조이고 빈칸, 벽으로 이루어 져있다. 벽은 칸 한칸을 차지한다.
# 바이러스는 상하좌우 인접한 빈칸으로 모두 퍼져나갈 수 있고 새로 세울 수 있는 벽은 3개이고, 꼭 3개만 세워야 한다. 연구소 지도가 주어졌을 때 앋을 수 있는 안전 영역 크기의 최댓값?
# 입력 첫째줄 -> 지도의 세로 크기 N, 가로 크기 M, 입력 둘째줄 ~~ -> 지도 모양이 주어짐. 0은 빈칸, 1은 벽, 2는 바이러스.
# 출력 첫째줄 -> 얻을 수 있는 안전 영역의 크기

# 바이러스는 상하좌우에 인접한 빈칸으로 이동가능하기에 바이러스칸을 모두 큐에 넣어 준 후, BFS를 통해 큐에서 하나씩 꺼내 확장시키는 방식으로 진행한다.
# 바이러스가 있는 칸에서 시작해 빈칸인 칸들을 모두 바이러스가 존재하는 칸으로 만드는 방식이다.
# 어디에 뱌ㅕㄱ을 세워야 최댓값이 나올지 알 수 없기에 벽을 세울 수 있는 모든 경우의 수에 대해 수행 해보아야 한다
# (1, 1) 칸 부터 (n, m)칸 까지 중 빈칸을 하나씩 3개를 선택해 벽을 세우고 BFS를 수행한 후 벽을 지우고 그 다음 칸에 대해 반복한다.
# 백트래킹을 이용해 3개의 벽을 모든 칸에 세워본다.
# 최댓값을 저장 한 후, 모든 탐색이 끝난 후 최댓값을 출력한다.

#파이썬 Queue는 deque로 사용해 구현한다
from collections import deque #파이썬에 내장된 collections 에서 deque 수입.
import copy #오늘 완료한 것이 내일 할당량에 포함됨으로 copy 사용을 위해 copy 수입

#입력받기
n, m = map(int, input().split())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    graph.append(list(map(int, input().split())))

#bfs
def bfs():
    queue = deque() #queue에 deque 선언
    tmp_graph = copy.deepcopy(graph) #지도를 복사해서 계속 반복하기 위함
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2: #바이러스있는곳
                queue.append((i, j))

    while queue: #바이러스 있는만큼 반복
        x, y = queue.popleft()

        for i in range(4): #움직일 수 있는 방향
            #신규좌표 = 기존좌표 + 이동좌표
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_graph[nx][ny] == 0: #빈칸
                tmp_graph[nx][ny] = 2 #바이러스
                queue.append((nx, ny))

    global answer
    cnt = 0 #안전 영역 크기 카운트

    for i in range(n):
        cnt += tmp_graph[i].count(0)

    answer = max(answer, cnt)


def makeWall(cnt):#안전영역확보하기위한
    if cnt == 3:
        bfs()
        return
    #백트래킹
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                graph[i][j] = 0

answer = 0
makeWall(0)
print(answer)


