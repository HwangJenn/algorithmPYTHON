# 수열A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하라
# 입력 첫쨰 줄 -> 수열 A의 크기 N이 주어진다.입력 둘째 줄 -> 수열 A를 이루고 있는 Ai
# 출력 첫째 줄 -> 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력

# 이진탐색으로 수열이 들어갈 자리를 찾는다

n = int(input())
array = list(map(int, input().split())) #수열A
stack = [0] #부분수열

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2 #중간지점

        if stack[mid] < target: #설정한 부분이 기준 원소보다 작으면
            start = mid + 1 #오른쪽으로 연장
        else: #아니라면
            end = mid - 1 #왼쪽으로 연장
    return start

for i in array: #수열A
    if stack[-1] < i: #들어갈자리가 있다면
        stack.append(i) #연장
    else:
        stack[binary_search(i, 0, len(stack) - 1)] = i

print(len(stack) - 1)