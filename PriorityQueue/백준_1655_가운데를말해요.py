# 정수를 하나씩 외칠때 마다 말한 수 중에서 중간값을 말해야한다. 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다
# 입력 첫쨰줄 -> 외칠 정수의 개수 N, 입력 둘째줄 ~ n+1 -> 외치는 정수 차례로 입력
# 출력 첫쨰줄 -> 한줄에 하나씩 N 줄에 걸처 외쳐야 할 중간값

# 우선순위 큐를 이융해 풀이를 한다. 중간값보다 작은 값으 leftleap에 큰 값은 rightleap에 저장한다.
# left와 right에 번갈아 값을 넣어줌으로써 두 합의 개수에 대한 균형을 유지핟록 한다
# left는 최대합 right은 최소합으로 구성을 함으로써 left의 첫원소를 중간값으로 한다
# right에 left보다 작은 값을 넣게 된다면 left의 첫 원소와 right 첫 원소를 교체해 균형을 유지한다

import heapq
import sys

n = int(sys.stdin.readline()) #외칠 정수의 개수

leftHeap = [] #저장할 값들
rightHeap = []
for i in range(n):
    num = int(sys.stdin.readline())

    if len(leftHeap) == len(rightHeap): #두 합의 개수가 균형이 맞다면
        heapq.heappush(leftHeap, -num) #바로 left에서 중간값 pop
    else:
        heapq.heappush(rightHeap, num)

    if rightHeap and rightHeap[0] < -leftHeap[0]: #right자리에 left보다 적은걸 넣는다면
        leftValue = heapq.heappop(leftHeap)
        rightValue = heapq.heappop(rightHeap)

        #양방향의 첫 원소들을 교체 해준다
        heapq.heappush(leftHeap, -rightValue)
        heapq.heappush(rightHeap, - leftValue)

    print(-leftHeap[0])