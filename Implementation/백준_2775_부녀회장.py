# 각 집에 거주민 수 구하기. 거주 조건 - a층의 b호에 살려면 자신의 아레 층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야함
# 아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 있다. 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇명이 살고 있는지 출 이 아파트는 0층부터 있고 각 층에는 1호부터, 0층 i호에는 i명이 산다
# 입력 첫째줄 -> 테스트 케이스의 개수 t, 입력 둘쨰줄 ~ t + 1줄 -> 첫번째줄 정수 k, 두번쨰줄 정수 n

# 0층 n호에는 n명이 살고 있다. 0층 [1,2,3,4,...], 1층의 n호에는 0층 1호 ~ n호 까지의 사람수만큼 살고 있으므로 sum(0층의 1호 ~ n호) 식으로 1층부터는 이전층의 사람들을 누적합 구한다

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    graph = [[0] * n for _ in range(k + 1)]

    graph[0] = [i + 1 for i in range(n)]

    for i in range(1, k + 1):
        for j in range(n):
            graph[i][j] = sum(graph[i - 1][:j + 1])

    print(graph[k][n - 1])