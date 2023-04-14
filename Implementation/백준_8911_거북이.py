# 2차원 평면 위에서 움직일 수 있는 거북이 로봇에게 명령을 내리자.
# F: 한 눈금 앞으로, B: 한 눈금 뒤고, L: 왼쪽으로 90도 회전, R: 오른쪽으로 90도 회전
# L, R은 이동하지 않고 방향만 바꾼다. 먕량을 나열할 것을 거북이 로봇 컨트롤프로그램이라고 함.
# 거북이가 이동한 영역을 계싼하려고 함. 항상 x축과 y축에 평행한 방향으로만 이동한다. 거북이가 지나간 영역을 모두 포함할 수 있는 가장 작은 직사각형의 넓이를 구하라.
# 제한: 직사각형의 모든 변은 x축이나 y축에 평행이아야함. 시작점은 (0, 0)이고 북쪽을 쳐다보고 있다. 축 하나로만 다니면 넓이는 0이다.
# 입력 첫쨰줄 -> 테스트케이스의 개수 T, 입력 둘쨰줄 ~~ -> 각 테스트 케이스
# 출력 첫쨰줄 ~~ -> 매 줄 거북이가 이동한 영역을 모두 포함하는 가장 직사각형의 넓이.

# L, R에선 움직이지말고 좌표 방향만 바꿔라.
# 각각에 케이스에 대해 이동좌표 모두 포함해 가장 작은 직사각형 출력이기에 하나하나 확인하기.

t = int(input()) #테스트 케이스 개수 입력받기

#움직일 방향. 북서남동순
dx = [0,-1,0,1]
dy = [1,0,-1,0]

for i in range(t): #테스트 케이스 수만큼 반복한다.
    pos_x = 0 #x축이동
    pos_y = 0 #y축이동
    pos_dir = 0  #방향, 0북 1서 2남 3동
    move = list(input()) #입력받은 각 테스트케이스
    trace = [(pos_x, pos_y)] #이동할 좌표
    for j in move: #이동명령처리
        if j == 'F': #F 입력. 한 눈금 앞으로
            pos_x = pos_x + dx[pos_dir] #x축 평행해서 양의방향으로
            pos_y = pos_y + dy[pos_dir] #y축 평행해서 양의방향으로
        elif j == 'B':#B 입력, 한 눈금 뒤로
            pos_x = pos_x - dx[pos_dir] #x축 평행해서 음의방향으로
            pos_y = pos_y - dy[pos_dir] #y축 평행해서 음의방향으로
        elif j == 'L': #L입력, 왼쪽으로 90도 회전
            if pos_dir == 3: #3(동)방향이면
                pos_dir = 0 #0(북)방향으로 회전
            else: #아니면
                pos_dir += 1 #1(서) 방향
        elif j == 'R': #R 입력, 오른쪽으로 90도 회전
            if pos_dir == 0: #0(북)이면
                pos_dir = 3 #3(동)으로 회전
            else: #아니면
                pos_dir -= 1 #1(서)

        trace.append((pos_x, pos_y)) #이동할 좌표에 추가하기
    #가로세로 길이 구하기
    width = max(trace, key = lambda x:x[0])[0] - min(trace, key = lambda x:x[0])[0]
    height = max(trace, key = lambda x:x[1])[1] - min(trace, key = lambda x:x[1])[1]
    print(width * height)