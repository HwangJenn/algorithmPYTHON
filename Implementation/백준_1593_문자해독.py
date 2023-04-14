# 마야 문자는 규칙 대신, 그들이 보기에 좋게 보이도록 단어를 이루는 글자들을 아무렇게나 배열함. 고고학자들은 W라는 특정 단어를 발굴 기록으로부터 찾고 있음. 그 단어를 구성하는 각 글자들은 무엇인지 알고 있지만, 이것이 고대 기록에 어떤 형태로 숨어 있는지는 다 알지 못함.
# W를 이루고 있는 g개의 그림문자와, 연구 대상인 벽화에 기록된 마야 문자열 S가 주어졌을 때, 단아 W가 마야 문자열 S에 들어있을 수 있는 모든 가짓수를 계산하는 프로그램을 작성하라.
# 즉, 문자열 S인에서 문자열 W의 순열 중 하나가 부분 문자열로 들어있는 모든 경우의 수를 계산하라는 뜻
# 입력 첫쨰줄 -> 고고학자들이 찾고자 하는 단어 W의 길이 g와 발굴된 벽화에서 추출한 문자열 S의 길이 |S|가 빈칸을 사이에 두고 주어진다.
# 입력 둘째줄 -> 모든 문자열은 알파벳으로 이루어지고, 대소문자를 구분한다.
# 출력 첫쨰줄 -> W의 순열이 S안에 있을 수 있는 형태의 개수를 출력

# W의 각각의 알파벳의 등장횟수를 그 알파벳에 해당하는 칸에 +1해준다. w와 s에 등장하는 알파벳의 횟수가 일치한다면 w의 순열로 s를 만들 수 있다는 뜻이기 때문에 정답을 +1해준다.
# 길이만큼 비교한 후, s의 비교 시작부분을 한 칸씩 뒤로 옮기면서 비교를 이어나간다.

import sys
from itertools import permutations #iterable에서 순열을 뽑기 위해 permutations 불러오기

g, s = map(int, input().split()) #W을 이루고 있는 g개의 그림문자, s의 길이 입력받기
W = sys.stdin.readline().strip()
S = sys.stdin.readline().strip()

wl = [0] * 52
sl = [0] * 52

#W의 각 알파벳마다 등장하는 부분에 +1
for i in range(g):
    if 'a' <= W[i] <= 'z':
        wl[ord(W[i]) - ord('a')] += 1 #인자로 받은 문자를 해당하는 유니코드 정수로 반환하는 ord
    else:
        wl[ord(W[i]) - ord('A') + 26] += 1

start = 0
length = 0
count = 0

for i in range(s):
    if 'a' <= S[i] <= 'z':
        sl[ord(S[i]) - ord('a')] += 1
    else:
        sl[ord(S[i]) - ord('A') + 26] += 1
    length += 1

    if length == g:
        if wl == sl:
            count += 1
        if 'a' <= S[start] <= 'z':
            sl[ord(S[start]) - ord('a')] -= 1
        else:
            sl[ord(S[start]) - ord('A') + 26] -= 1
        start += 1
        length -= 1

print(count)