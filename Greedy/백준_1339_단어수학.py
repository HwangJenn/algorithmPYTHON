# n개의 단어로 이루어진 단어수학문제. 각 단어는 알파벳 대문자로만 이루어져 있다.
# 각 알파벳 대문자를 0 부터 9까지의 숫자 중 하나로 바꿔서 n개의 수를 합한다. 같은 알파벳은 같은 숫자로, 두개 이상의 알파벳이 같은 숫자로 바뀌면 안된다.
# n개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램?
# 입력 첫째줄 -> 단어의 개수 n, 입력 둘째줄 ~ -> 알파벳 대문자로만 이루어진 단어가 한줄에 하나씩
# 출력 첫째줄 -> 단어의 합의 최댓값

# 알파벳을 딕셔너리에 저장하고 단어 길이에 따라 알파벳의 자릿수가 정해지기에 자릿수를 체크해 그 자리에 맞는 값을 매칭
# 매칭을 완료한 후에 가장 큰 비율을 차지하는 것 부터 등장하게 하기 위해 dict의 value만 가져와서 리스트에 내림차순으로 정렬한다.
# 이 리스트의 첫 수부터 9를 곱하고 8 7 ...으로 내려간다.

import sys

n = int(sys.stdin.readline()) #입력받을 단어의 개수

alphabet = [] #알파벳 정렬
alphabet_dic = {} #알파벳 저장할 딕셔너리
numList = [] #수 저장할 리스트

for i in range(n): #단어 수 만큼
    alphabet.append(sys.stdin.readline().rstrip()) #단어 입력받음

for i in range(n): #입력 받은 단어 수만큼
    for j in range(len(alphabet[i])): #단어 길이만큼
        if alphabet[i][j] in alphabet_dic: #단어의 알파벳이 딕셔너리에 있으면
            alphabet_dic[alphabet[i][j]] += 10 ** (len(alphabet[i]) - j - 1) #자리에 맞게 추가
        else: #없으면
            alphabet_dic[alphabet[i][j]] = 10 ** (len(alphabet[i]) - j - 1) #새로 추가

for value in alphabet_dic.values():
    numList.append(value) #딕셔너리에 저장된 수들을 모두 리스트에 추가

numList.sort(reverse= True) #내림차순 정렬

sum = 0
pows = 9
for i in numList: #내림차순 정렬으로 맨 앞에 있는 수가 가장 크다
    sum += pows * i #9부터 곱해주고
    pows -= 1 #내려갈수록 -1해서 곱해준다
print(sum)