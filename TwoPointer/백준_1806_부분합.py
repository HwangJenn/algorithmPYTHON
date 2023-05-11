# 10000이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S이상이 되는 것 중 가장 짧은 것의 길이를 구하는 프로그램을 작성하라
# 입력 첫째줄 -> N 과 S, 입력 둘째줄 -> 각 원소가 공백으로 구분되어진 수열
# 출력 첫쨰줄 -> 구하고자 하는 최소의 길이 또는 합을 만드는 것이 불가능하다면 0 출력

# 시작점과 끝점을 적절히 이동시키며 그 사이에 있는 부분들의 합을 이용해 정답을 찾는다
# 시작점과 끝점을 0으로 두고 시작점과 끝점을 움직이면서 구간의 길이를 조절한다
# 현재 구간이 S보다 작다면, 구간을 더 늘려야 하므로 끝점을 뒤로 움직여 구간을 늘려주고 현재 구간이 S보다 크다면, 구간을 더 줄여야 하므로 시작점을 뒤로 움직여 구간을 줄여준다

import sys
n, s = map(int, sys.stdin.readline().split()) #입력받을 n과 s
nlist = list(map(int, sys.stdin.readline().split())) #입력받을 수열

start, end = 0, 0 #시작점고 끝점은 0으로
flag = 0 #답을 찾을수 있는가 없는가에 대한 플래그
short = n #수열
mysum = nlist[0] #수열의 합

while end < n:
    if mysum < s: #현재 구간합이 s보다 작으면
        end += 1 #현재 구간의 끝점을 늘려준다
        if end < n: #끝이 n을 벗어나면 안되기 때문에 범위 고려
            mysum += nlist[end]
    else: #현재 구간합이 s보다 크거나 같을 경우
        flag = 1 #답을 찾을 수 있다는 표시
        if short > end-start: #현재까지의 최소거리보다 짧으면
            short = end-start + 1 #최소거리 갱신

        if start < end: #구간시작점이 끝점보다 앞에 있다면
            mysum -= nlist[start] #구간 시작점을 하나 늘린다
            start += 1
        else: #구간 시작점이 끝점과 같거나 뒤에 있으면
            end += 1 #구간 끝점을 하나 뒤 늘려서 end가 start뒤에 오도록 유지
            if end < n:
                mysum += nlist[end] #끝잠을 늘려가며 부분합 추가
if flag == 1:
    print(short)
else:
    print(0)