# 3가지의 연산문자 +, -, * 만으로 이루어진 연산수식이 주아지고 수식에 포함된 연산자의 우선순위를 재정의해 가장 큰 숫자를 제출한다.
# 단, 같은 순위의 연산자는 없다. 수식에 포함된 우선순위 조합은 n!가지의 조합이 가능하다. 음수 일 경우 절댓값 변환을 한다.

# 순열(permutations)을 통해 만들 수 있는 우선순위 조합 가짓수 수행
# 문자열 수식을 숫자와 기호로 분리해주기 위해 수식expression을 처음부터 끝까지 돌면서 리스트로 분리한다.
# 리스트를 돌면서 우선순위에 맞게 수식계산을 한다.
# 최댓값 저장

''' def solution(expression):
    answer = 0
    return answer '''

from itertools import permutations

def solution(expression):
    answer = 0
    oper = ["+", "-", "*"]
    myMax = int(-1e9)

    for per in permutations(oper,3):
        perm = list(per)
        exp = ''
        tmp = []
        for i in range(len(expression)):
            if str(0) <= expression[i] <= str(9):
                exp += expression[i]
            else:
                tmp.append(exp)
                tmp.append(expression[i])
                exp = ''
            if i == len(expression) - 1:
                tmp.append(exp)

        for j in range(len(perm)):
            i = 0
            while i < len(tmp):
                if tmp[i] == perm[j]:
                    tmp[i - 1]= eval(str(tmp[i - 1]) + perm[j] + str(tmp[i + 1]))
                    del tmp[i]
                    if i < len(tmp):
                        del tmp[i]
            else:
                i += 1
        myMax = max(myMax, abs(tmp[0]))

    return myMax

print(solution("100-200*300-500+20"))