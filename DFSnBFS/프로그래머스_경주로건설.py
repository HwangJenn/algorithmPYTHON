# 자동차 경주로 건설. 경주로 부지 N x N크기의 정사각형 격자임. 각 격자의 크기는 1 x 1이고, 각 격자의 칸은 0(바워짐), 1(채워짐)
# 출발점은 좌측 상단인 (0, 0)이고 도착점은 우측하단인 (N-1, N-1) 까지 끊기지 않아야 한다.
# 경주로는 상 하 좌 우 로 인접한 두 빈칸을 연결하고, 벽(1)엔 경주로 건설을 하지 않는다. 인접한 두 빈칸은 직선도로이고 두 직선 도로가 서로 직각으로 만나는 지점은 코너이다.
# 직선도로 하나에 100원 코너 하나에 500원 추가이다
# 경주로 건설의 최소 비용은?
# 제한사항 board 배열의 크기 : 3이상 25 이하, board 배열 각 원소 값 0 또는 1, 가장 왼쪽 상단이나 가장 우츠하단은 비어있어 도로연결 가능. board는 항상 출발점에서 도착점까지 경주로 건설할 수 있는 형태로 주어짐. 출발점과 도착점 칸의 원소값은 항상 0으로 주어진다.

# bfs를 한번만 실행한다
# 시작지점에는 오른쪽 아래쪽 둘다 움직일 수 있으므로 예외사항이다. 5라는 방향을 주어 두 방향 모두 100원 추가한다.
# 단, 여기서 price칸 값 갱신할 때, "c"가 아닌 "c = " 해주어야한다.
#같은 칸에서 두 방향으로 온 값이 겹쳤을 때, 값이 같게 된다면 멈추지 않고 진행한다.

''' def solution(board):
    answer = 0
    return answer '''

#파이썬 Queue는 deque로 사용해 구현한다
from collections import deque #파이썬에 내장된 collections 에서 deque 수입.

#이동할 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

#bfs
def bfs(board):
    n = len(board)
    price = [[int(1e9) * n for _ in range(n)]]
    price[0][0] = 0 #시작점 초기화

    queue = deque()
    queue.append((0, 0, 0, 5))

    while queue:
        x, y, c, z = queue.popleft()

        if x == n - 1 and y == n - 1:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = i

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 1:
                continue
            if z == 5: #예외사항에 의해 5라는 방향을 주어
                nc = c + 100 #100원 추가
            elif nz == z:
                 nc = c + 100
            else:
                nc = c + 600

    return price[-1][1]

def solution(board):
    answer = 0
    return answer

