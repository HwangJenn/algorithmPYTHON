# 1 부터 N 까지 자연수 중에서 중복 없이 M개 고른다.
# 입력 첫째줄 -> 자연수 M, M
# 출력 첫째줄 ~~ -> 문제의 조건을 만족하는 수열
# 중복되는 수열 여러번 출력 불가, 각 수열은 공백으로 구분, 오름차순으로 출력

# N 과 M (1) 문제와 동일함
# n = 4, m =2의 경우 (1, 2), (1, 3), (1, 4), (2, 1) ...에서 (2, 1), (3, 1) ... 은 내림차순으로 불가함
# 순열로 풀 수 있으나 의도에 따라 dfs의 백트래킹을 이용한킹

#dfs 전 입력받을 값 정리
n, m = map(int, input().split()) #입력받을 자연수 n, m

visited = [False] * (n + 1) #방문기록 초기화
answer = [] #수열 초기화

def dfs(start, a): #start, a를 매개변수로 가지는 dfs
    if a == 0: #a가 0이라면
        print(" ".join(map(str, answer))) #쪼개진 문자열을 합친다
        return

    #백트래킹
    for i in range(start, n + 1): #start와 n+1 범위 내에서
        if not visited[i]: #방문하지 않았으면
            answer.append(i) #i를 수열 맨 뒤 입력
            visited[i] = True #방문처리
            dfs(i, a - 1) #dfs 수행
            answer.pop() #수열 꺼내기
            visited[i] = False #재방문을 위해 방문처리 하지 않음

#dfs 수행
dfs(1, m)