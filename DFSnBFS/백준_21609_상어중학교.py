# M * N 크기의 격자 게임이다.
# 초기 격자의 모든 블록(검정, 무지개, 일반), 일반 블록 M가지의 색상이 있다. =
# (i, j)ㅣ i번행, j번열 |r1 - r2| + |c1 - c2| = 1 은 두 블록(r1, c1)과 (r2, c2)와 인접한다.
# 블록 그룹은 연결된 블록의 집합이고
# -> 블록 그룹에는 일반 블록 적어도 하나있고 붙어있는건 색 상관이 없다. 블록의 개수는 2개 상이상이여야 하고 임의의 한 블록에서 그룹에 속한 인접 칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동 할 수 있어야 한다.
# 기준 블록은 무지개 지역에 있고 행의 번호는 최소이고 같은 행에선 열이 최소이다.
# 블록 그룹이 존재하는 한 계쏙 반복 되는 오토 플레이가 가능하다.
# 오토 플레이 가능 -> 블록 그룹이 존재하는 한 계속 반복한다.
# 1. 크기가 가장 큰 블록 크룹을 찾는다
# 2. 1에서 찾은 그룹의 모든 블록을 제거하고 블록그룹 중에서 블록수가 B일 때 B2 점 획득한다.
# 3. 격자에 맞는 중력이 작용한다.
# 4. 격자 90도 반시계 회전한다.
# 5. 다시 격자에 중력 작용한다. -> 중력 작용 시, 검정 제외 모든 블록 행 번호 큰 칸으로 이동한다.
# 다른 블록, 격자 만나기까지 반복한다.
# 입력 첫째줄 -> 격자 한변의 크기 N, 색상의 개수 M, 입력 둘째줄 ~~ -> N개의 줄에 격자의 칸에 들어있는 블록의 정보가 1번행 ~ N번행까지 순서대로 주어진다. 입력으로 주어지는 칸의 정보는 -1, 0, M이하의 자연수임.
# 출력 첫째줄-> 획득한 점수의 합 출력한다
# 제한조건 1 <= N <= 20, 1 <= M <= 5

# rotate(회전)함수: 반시계 방향으로 90도 회전한다. (0, 0) -> (n - 1, 0)으로 이동, (0, 1) -> (n - 2, 0)으로 이동. ~~> (x, y) -> (n - 1 - y, x)로 이동
# grabity(중력)함수: 벽(검정)이나 경계를 만날 때까지 아래 빈칸으로 떨어진다. 밑의 행부터 시작해 차례대로 while문을 통해 내려갈 수 있는 곳 까지 내려간다.

# BFS코드 (find_group 함수)
# 문제에서 조건1에 해당하는 '크기가 가장 큰 블록 그룹찾기' 부분은 함수안에 같이 구현한다.
# while 문을 통해 그룹을 짓는다 -> 크기가 2보다 작으면(조건) 그룹 생성 불가 -> return
# 크기가 같다면 무지개 블록수가 많은게 최대 그룹이고 그마저 같다면 기준 행과 열을 비교해 선정한다.

#파이썬 Queue는 deque로 사용해 구현한다
from collections import deque #파이썬에 내장된 collections 에서 deque 수입.

#입력
n, m = map(int, input().split()) #격자크기 n, 블록 색상 개수 m 입력받기
graph = [] #격자(그래프) 초기화
#이동 할 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n): #격자 크기만큼 반복
    graph.append(list(map(int, input().split()))) #칸에 입력받은 값 추가

#bfs를 이용한 find_group함수
def find_group(a, b): #매개변수 a, b를 가지는 함수 선언

    #그룹찾기위해
    visited = [[False] * n for _ in range(n)] #방문기록 초기화
    groupQ = [] #찾을 그룹 선언
    if graph[a][b] == -1 or graph[a][b] == -2: #그룹 크기 비교해서 음수이면
        return #그룹생성 불가로 return
    if graph[a][b] > 0: #그룹이 양수이면
        myColor = graph[a][b] #색입략
    else: #아니면
        myColor = 0
    count = 1 #카운트

    #bfs
    queue = deque() #queue를 deque 선언
    queue.append((a, b)) #a,b를 추가
    visited[a][b] = True #방문처리

    while queue: #queue가 없어질때까지 비교
        x, y = queue.popleft() #x,y 값 popleft
        groupQ.append((x, y)) #groupQ에 추가

        for i in range(4): #4방향 이동
            #신규위치 = 현재위치 + 이동위치
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]: #범위에 속하지 않는다면
                continue
            if graph[nx][ny] == -1 or graph[nx][ny] == -2: #그룹이 조건에 의해 작다면
               continue
            if graph[nx][ny] > 0: #그룹에 조건에 부합하다면
                if myColor == 0: #무지개블록
                    myColor = graph[nx][ny] #무지개블록 비교
                elif myColor != graph[nx][ny]: #무지개 블록 크기 다르면
                    continue
            count += 1 #하나 카운트
            queue.append((nx, ny)) #nx, ny추가
            visited[nx][ny] = True #방문처리

    if count < 2: #2보다 작다면
        return #리턴

    global groupCount, maxQ #전역변수 설정

    if count > groupCount: #그룹 카운트가 앞선 카운트보다 작으면
        groupCount = count #카운트 값 같음
        maxQ = groupQ #최댓값
    elif count == groupCount: #둘다 같으면
        thisZeroCount, maxZeroCount = 0, 0 #제로카운트
        for i in range(count): #카운트 범위안에서 반복
            if graph[groupQ[i][0]][groupQ[i][1]] == 0: #행비교
                thisZeroCount += 1
        for i in range(groupCount): #열비교
            if graph[maxQ[i][0]][maxQ[i][1]] == 0:
                maxZeroCount += 1
        if thisZeroCount == maxZeroCount: #카운트 비교
            #정렬
            groupQ.sort(key=lambda x: x[1])
            groupQ.sort(key=lambda x: x[0])
            maxQ.sort(key=lambda x: x[1])
            maxQ.sort(key=lambda x: x[0])
            gx, gy, mx, my = 0, 0, 0, 0
            for i in range(count): #카운트 범위안에서 반복
                if graph[groupQ[i][0]][groupQ[i][1]] != 0:
                    gx = groupQ[i][0]
                    gy = groupQ[i][1]
                    break
            for i in range(groupCount): #그룹카운트에서 반복
                if graph[maxQ[i][0]][maxQ[i][1]] != 0:
                    mx = maxQ[i][0]
                    my = maxQ[i][1]
                    break

            if gx > mx:
                maxQ = groupQ
            elif gx == mx:
                if gy > my:
                    maxQ = groupQ

        elif thisZeroCount > maxZeroCount:
            maxQ = groupQ

    return

#중력함수
def gravity():
    for i in range(n-2, -1, -1): #중력함수로 인해 바뀔 요소
        for j in range(n):
            if graph[i][j] != -1: #벽이 있으면
                tmp = i #그대로
                while tmp + 1 < n and graph[tmp+1][j] == -2: #내려갈 수 있는 곳 까지 내려감
                    graph[tmp+1][j] = graph[tmp][j]
                    graph[tmp][j] = -2
                    tmp += 1


#회전함수
def rotate():
    newGraph = [[0] * n for _ in range(n)] #반시계방향으로 격자가 회전함
    for i in range(n):
        for j in range(n):
            newGraph[n - 1 - j][i] = graph[i][j] #회전하면서 바뀔 좌표
    return newGraph


answer = 0

#오토플레이
while True:
    groupCount = 0
    maxQ = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                find_group(i, j)
    if not maxQ:
        break
    answer += len(maxQ)**2
    for x, y in maxQ:
        graph[x][y] = -2
    gravity()
    graph = rotate()
    gravity()

#출력
print(answer)