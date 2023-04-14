# 크기가 N*M인 지도가 있음. 지도의 오른쪽은 동쪽, 위쪽은 북쪽임. 이 지도의 위에 주사위가 하나 있고 주사위의 전개도도 있다.
# 지도의 좌표는 (r, c)로 나타내며, r은 북쪽으로부타 떨어진 칸의 개수, c는 서쪽으로부터 떨어진 칸의 개수임.
# 주사위는 지도 위에 윗 면이 1이고 동쪽을 바라보는 방향이 3인 상태로 놓여져 있다. 놓여져 있는 곳의 좌표는 (x, y)임. 가장 처음에 주사위에는 모든 면에 0이 적혀있다.
# 지도의 각 칸에는 정수가 하나씩 쓰여져 있다. 굴렸을 때 이동칸에 쓰여 있는 수가 0이라면 주사위의 바닥 면에 쓰여 있는 수가 칸에 복사.
# 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사, 칸에 쓰여 있는 수는 0이된다.
# 주사위를 놓는 곳의 좌표와 이동시키는 명령이 주어졌을 때, 주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하라.
# 딘, 주사위는 지도의 바깥으로 이동시킬 수 없다. 바깥으로 이동시키려고 하는 명령은 무시하고 출력도 안한다.
# 입력 첫쨰줄 -> 지도의 세로 N, 가로 M, 주사위를 놓는 곳의 좌표 x, y, 명령의 개수 k가 주어진다.
# 입력 둘쨰줄 ~~ -> 지도에 쓰여 있는 수가 북쪽부터 남쪽으로, 각 줄은 서쪽부터 동쪽 순서대로 주어짐다. 각 줄은 서쪽에서 동쪽 순서대로 주어진다. 주사위를 놓은 칸에 쓰여 있는 수는 항상 0이다. 지도의 각 칸에 쓰여 있는 수는 10 미만의 자연수 또는 0이다.
# 입력 마지막줄 -> 이동하는 명령이 순서대로 주어진다. 동쪽은 1 서쪽은 2 북쪽은 3 남쪽은 4로 주어진다.
# 출력 첫쨰줄 ~~ -> 이동할 때마다 주사위의 윗 면에 쓰여 있는 수를 출력한다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시하고 출력도 안한다.

# 주사위 굴린 방향에 따라 인덱스가 어떻게 변했는지 알아야 한다.
# turn 함수에 정의 해 놓고 굴려야 할 때 함수 실행해야한다.

n, m, x, y, k = map(int, input().split()) #지도 세로, 가로, 좌표, 명령의 개수 입력받기

board = [] #지도 초기화
dx = [0, 0, -1, 1] #x좌표
dy = [1, -1, 0, 0] #y좌표
dice = [0, 0, 0, 0, 0, 0] #주사위 초기화

def turn(dir): #동서남북으로 구를 주사위 변화 함수
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else: #남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

for i in range(n): #세로길이 범위까지
    board.append(list(map(int, input().split()))) #지도 북~남

comm = list(map(int, input().split())) #이동하는 명령 입력받기

nx, ny = x, y #서쪽, 동쪽
#명령 수행
for i in comm:
    nx += dx[i - 1]
    ny += dy[i - 1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m: #범위에 속하는지 확인
        nx -= dx[i - 1]
        ny -= dy[i - 1]
        continue
    turn(i)
    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1]
    else:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0

    print(dice[0])