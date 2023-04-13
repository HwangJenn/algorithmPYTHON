# 1 부터 N 까지 자연수 중에서 중복 없이 M개 고른다.
# 입력 첫째줄 -> 자연수 M, M
# 출력 첫째줄 ~~ -> 문제의 조건을 만족하는 수열
# 중복되는 수열 여러번 출력 불가, 각 수열은 공백으로 구분, 사전순으로 증가하는(오름차순) 출력

# 중복이 허락되지 않는다. n  = 4, m = 2 -> (1, 2), (1, 3), (1, 4) --- (4,3)
# DFS(깊이 우선 탐색을 통해 1부터 탐색한다.
# 백트래킹을 통해 방문한 후에는 방문 처리 안함으로 다음턴에서도 방문이 가능하다. -> 이미 방문한 곳도 방문 가능

#dfs 수행 전 처리
n, m = map(int, input().split()) #자연수 n, m 입력받기

visited = [False] * (n + 1) #방문하지 않은곳에 + 1
answer = [] #수열 초기화

#dfs
def dfs(a): #a를 매개변수로 가지는 dfs 정의
    if a == 0: #a값이 0ㅇ이라면
        print(" ".join(map(str, answer))) #쪼개진 문자열 합치기
        return
    #백트래킹
    for i in range(1, n + 1): #1부터 n+!까지 반복
        if not visited[i]: #방문안했으면
            answer.append(i) #수열에 추가
            visited[i] = True #방문함
            dfs(a - 1) #dfs 수행
            answer.pop() #수열 맨뒤에거 내주고 삭제
            visited[i] = False #재방문을 위해 방문처리 안함

#dfs
dfs(m)

#입력 3 1 출력 1 2 3