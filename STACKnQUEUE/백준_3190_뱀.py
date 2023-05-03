# 뱀이 사과를 먹으면 뱀 길이가 늘어나고 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝난다
# 게임은 n x n 정사각 보드위에서 진행되고 몇몇 칸에는 사과가 놓여있따. 보드 상하좌우 끝에 벽이 있고 게임이 시작할 때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1이다.
# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다. 만약 이동한 칸에 사과가 없어지고 꼬리는 움직이지 않는다. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라
# 입력 첫째줄 -> 보드의 크기 n, 입력 둘째줄 -> 사과의 개수 k, 입력 셋째줄 ~ k -> 사과의 위치. 첫번째 정수는 행, 두번째 정수는 위치, 사과의 위치는 모두 다르다. 입력 k+1줄 -> 뱀의 방향 변환 횟수 l, 입력 k+2줄 ~ -> 뱀의 방향정보
# 출력 첫째줄 -> 게임이 몇 초에 끝나는가

# 큐를 이용한 구현문제이다
# 그래프를 0으로 모두 채우고 사과 위치는 모두 2로 채운다. 뱀이 차지하고 있는 부분은 1로 채운다
# 뱀이 이동할 때 마다 머리와 꼬리는 한 칸씩 전진하고 몸 길이는 그대로이다
# 이동했을 때 사과를 먹으면 몸의 길이가 한 칸 늘어나 머리는 전진하지만 꼬리는 그대로이다.
# 방향 전환을 해야 하는 타이밍에 맞춰 L이면 왼쪽 D이면 오른쪽으로 방향전환을 한다.

from collections import deque #collections에서 deque 수입

n = int(input()) #입력받을 보드의 크기
k = int(input()) #사과의 개수

graph = [[0] * n for _ in range(n)] #그래프(보드)
dx = [0, 1, 0, -1] #뱀이 이동할 방향
dy = [1, 0, -1, 0]

for i in range(k): #사과
    a, b = map(int, input().split()) #입력받은 사과 위치
    graph[a - 1][b - 1] = 2 #사과자리에 2로 채워준다

l = int(input()) #뱀의 방향변환횟수
dirDict = dict() #저장할 방향
queue = deque() #queue는 deque로 정의
queue.append((0, 0)) #뱀의 초기 위치

for i in range(l): #뱀의 방향변환횟수만큼
    x, c = input().split() #압력받은 뱀의 방향 변환 횟수
    dirDict[int(x)] = c #방향저장

x, y = 0, 0
graph[x][y] = 1 #뱀 크기
count = 0
direction = 0

def turn(alpha): #방향전환
    global direction
    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

while True:
    count += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= n or y < 0 or y >= n:
        break

    if graph[x][y] == 2:
        graph[x][y] = 1
        queue.append((x, y))
        if count in dirDict:
            turn(dirDict[count])

    elif graph[x][y] == 0:
        graph[x][y] = 1
        queue.append((x, y))
        tx, ty = queue.popleft()
        graph[tx][ty] = 0
        if count in dirDict:
            turn(dirDict[count])

    else:
        break

print(count)