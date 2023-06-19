# aabbaccc -> 2a2ba3c,ababcdcdababcdcd -> 2ab2cd2ab2cd, abcabcdede -> 2abcdede 처럼 문자열 s가 주어질 때 압축한 문자열의 길이 return

def solution(s):
    result = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)+1):
        b = ''
        count = 1
        tmp = s[:i]
    for j in range(i, len(s) + i, i):
        if tmp == s[j: j + i]:
            count += 1
        else:
            if count != 1:
                b = b + str(count) + tmp
            else:
                b = b + tmp
            tmp = s[j: j + i]
            count = 1
        result.appent(len(b))
    return min(result)