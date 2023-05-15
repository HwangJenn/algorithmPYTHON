# 압력 첫쨰줄 -> N, N은 항상 3*2k 수이다.
# 출력 첫쨰줄 ~ N-> 별출력
# 별의 개수에 상관 없이 별이 없는 칸은 무조건 공백이 나오도록 코드를 짜야한다.

# n = 3인 기본 모양을 바탕으로 양옆으로 좌표만을 계산해 재귀적으로 그린다

n = int(input()) #입력받을 n
graph = [[' '] * 2 * n for _ in range(n)] #별을 출력할 그래프

def star(x, y, n): #입력받은 n에 따른 가로, 세로
    if n == 3: #기준 n 값 3
        graph[x][y] = '*'
        graph[x + 1][y - 1] = graph[x + 1][y + 1] = '*'
        for i in range(-2, 3):
            graph[x + 2][y + i] = '*'
    else: #출력 예에 따른 공백 모양
        nextn = n // 2
        star(x, y, nextn)
        star(x + nextn, y - nextn, nextn)
        star(x + nextn, y + nextn, nextn)

star(0, n - 1, n)
for i in graph:
    print("".join(i))
