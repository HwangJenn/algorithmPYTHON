# 수빈이의 현재 위치 N, 동생의 현재 위치 K(0 <= N,K <= 100,000) 일때, N -> K 는 몇 초 걸리는가?
# 초당, 걸을 때 (x - 1) 또는 (x + 1) , 순간이동 2x 이동한다.
# 힌트) 5 10 9 18 17 순으로 4초만에 찾을 수 있다.

#파이썬 Queue는 deque로 사용해 구현한다
from collections import deque #파이썬에 내장된 collections 에서 deque 수입.

#bfs()함수 정의 전 처리
MAX = 10 ** 5 #최댓값 설정으로 수 제한
dist = [0] * (MAX + 1)  #dist 변수 설정 -> 최댓값에 1을 더한만큼 [0, 0, 0 ... 0] 리스트 생성
n, k = map(int, input().split()) #정수 입력받을 n, k 변수 설정

#bfs
def bfs(): #def로 bfs함수 정의
    q = deque() # 변수를 deque()로 초기화
    q.append(n) #q.append(n)을 통해 q = deque([힌트n값 5]) 시작점 deque에 추가
    while q: #q가 정수일 때 계속해서 반복하는 while 반복문
        x = q.popleft() #deque() 왼쪽에 있는 수를 빼주는 popleft()함수 -> x = 5, q = deque([])
        if x == k: #수빈이와 동생 위치가 같아지면
            print(dist[x]) #걸린 시간 dist[x]를 print하고
            break #while문 탈출
        for nx in (x - 1, x + 1, x * 2): #q.append(5)에서 popleft된 x = 5 -> nx = 4, 6,10
            if 0 <= nx <= MAX and not dist[nx]: #0 <= 4, 6, 10 <= MAX와 not dist[4, 6, 10]이 거짓이면 (dist[nx] = 0) 조건이 언제나 거짓인 if "not" dist[nx] 만족한다
                dist[nx] = dist[x] + 1 #dist[4, 6, 10] = dist[5] + 1 = 0 + 1 =1
                q.append(nx) #q = deque([4, 6, 10])
        # for문 반복 (힌트 5 - 10 - 9 - 18 - 17)
        # popleft x = 10, nx = 9, 11, 20 / dist[9, 11, 20] = dist[10] + 1 = 1 + 1 = 2
        # popleft x = 9, nx = 8, 10, 18 / dist[8, 10, 18] = dist[9] + 1 = 2 + 1 = 3
        # popleft x = 18, nx = 17, 19, 36 / dist[17, 19, 36] = dist[18] + 1 = 3 + 1 = 4
        # ~> q = deque([17, 19, 36])에서 x = q.popleft() -> x = 17, q = deque([19, 36])
        # ~> if문 x == k -> dist[17] ~> 4출력


bfs() #def로 정의한 bfs함수 실행( ()이 실행 버튼이다.)

