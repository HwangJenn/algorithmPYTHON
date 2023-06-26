# 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.
# 보드의 세로 크기는 N, 가로 크기는 M, 1x1크기의 칸으로 나누어져 있다. 가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다. 빨간구슬과 파란구슬은 보드 크기의 칸을 가득 채우는 사이즈이고 하나씩 들어가 있다.
# 빨간 구슬을 구멍을 통해 빼내야하는데 파란 구슬은 구멍에 들어가면 안된다. 좌우, 위아래로 기울여서 구슬을 굴려야한다.
# 공은 동시에 움직이고 빨간구슬이 구멍에 빠지면 성공이지만 파란 구슬이 구멍에 빠지거나 동시에 빠져도실패이다. 같은칸에 있을 수 없다. 구슬이 움직이지 않을 때까지 움직이고 최소 몇번을 움직여야 빨간 구슬을 구멍에서 빼는가

# 입력 첫술 -> 보드의 가로 n, 세로 m (3 < n, m <= 10), 입력 둘째줄 ~ n+1 -> 보드의 모양을 나타내는 m길이의 문자열. '.', '#(공이 이동할수 없는 장애물 또는 벽)', '0(구멍위치)', 'R(빨간구슬)', 'B(파란구슬)'
# 입력되는 모든 보드의가장자리에는 모두 #이 있다.구멍의 개수는 한개이고 빨강, 파랑 구슬은 항상 하나이다.

# 구슬을 굴리게 되면, 벽이나 구멍에 닿을 때 까지 구슬은 계속 굴러가고 방향하나를 정했을 때 그 방향으로 계속 굴러가도록 while문
# 구술이 굴러가다 다른색과 마주쳤을 때 앞에 구슬이 멈추면 내 구슬은 전칸에서 멈추니 각 구슬의 카운트를 통해 어떤 구슬이 앞에 있던 구슬인지 표기한 후 순서에 맞게 구슬을 배치하도록 한다.
# 빨간색 구슬과 파란색 구슬 좌표를 표현하기 위해 4차원 배열 사용. 4차원 visited 배열을 통해 발생한 상황은 다시 일어나지 않도록 방지한다.

from collections import deque #deque 불러오기

n, m = map(int, input().split()) #보드의 가로세로 크기 입력받기
graph = [] #graph로 표현
for i in range(n): #n의 크기만큼
    graph.append(list(input())) #그래프에 나타내기

dx = [0, 0, 1, -1] #구슬이 움직일 각 좌표
dy = [1, -1, 0, 0]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)] #이미 발생한 상황 방지처리하기 위해 m과 n의 범위 내에서 저장

def roll(x, y, direct): #구술 굴리기
    count = 0 #앞에 있던 구슬 저장

    while graph[x + dx[direct]][y + dy[direct]] != '#' and graph[x][y] != 'O': #그래프를 따라 구슬 굴리기. #은 공이 이동할수 없는 곳임
        x += dx[direct] #신규위치
        y += dy[direct]
        count += 1 #구슬 배치

    return x, y, count

def bfs(ra, rb, ba, bb): #구슬의 움직임 4차원으로
    queue = deque() #queue를 deque로 선언
    queue.append((ra, rb, ba, bb, 1)) #구슬방향 추가

    while queue:
        rx, ry, bx, by, count = queue.popleft() #구슬이 갈곳
        visited[rx][ry][bx][by] = True #이미 발생한 상황
        if count > 10: #10이상이면 (문제 조건)
            print(-1) #-1
            exit(0)

        for i in range(4): #위아래좌우 4방향
            nrx, nry, rcount = roll(rx, ry, i)
            nbx, nby, bcount = roll(bx, by, i)

            if graph[nbx][nby] != 'O': #구멍위치에 위치하는가
                if graph[nrx][nry] == 'O':
                    print(count)
                    exit(0)

                if nrx == nbx and nry == nby:
                    if rcount > bcount:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    queue.append((nrx, nry, nbx, nby, count+1))

    print(-1)
    return

rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            rx = i
            ry = j
        if graph[i][j] == 'B':
            bx = i
            by = j

bfs(rx, ry, bx, by)