# 0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하라
# 행렬을 변환하는 연산은 어떤 3x3 크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다.
# 입력 첫째줄 -> 행렬의 크기 n m, 입력 둘째줄 ~ -> 행렬 A 부터 그다음줄부터 n개의 줄에는 행렬 b
# 출력 첫째줄 -> 정답 출력, 만약 A를 B로 바꿀 수 없다면 -1 출력한다

# 행렬 a와 b가 일치하지 않으면 그 부분부터 3x3 범위안의 행렬을 뒤집어준다

n, m = map(int, input().split()) #입력받을 행렬의 크기 n, m
graph1 = [] #변환전
graph2 = [] #변환후
count = 0 #행렬 a를 행렬 b로 전환하는데 필요한 횟수

def convertgraph(i, j): #뒤집기 함수
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            graph1[x][y] = 1 - graph1[x][y]

for i in range(n): #변환전
    graph1.append(list(map(int, input())))

for i in range(n): #변환후
    graph2.append(list(map(int, input())))

for i in range(n - 2):
    for j in range(m - 2):
        if graph1[i][j] != graph2[i][j]: #일치하지 않는 다면
            convertgraph(i, j) #뒤집기
            count += 1 #횟수 1 카운트

flag = 0 #변환 할 수 있는지 나타내는 변수

for i in range(n): #변환 후 일치 여부
    for j in range(m):
        if graph1[i][j] != graph2[i][j]:
            flag = 1 #변환 불가능
            break

if flag == 1: #변환 불가 -> 일치
    print(-1) #-1 출력
else:
    print(count)