# '('와')'의개수가 같으면 균형잡힌, 짝이 맞으면 올바른 문자열이라고 한다. 균형잡힌 문자열 w가 주어졌을 때 올바른 문자열로 변환하라
# 변환과정 1. 빈문자열은 빈문자열을 반환한다. 2. w를 u(균형잡히고 더이상 분리안될때 까지)와 v(빈문자열가능)으로 분리한다.
# 3. u가 올바르면 v에 대해 1단계부터 다시 수행한다. 3-1. 수행결과를 문자열 u에 붙여 반환한다.
# 4. u가 올바르지 않으면, 4-1. 빈문자에 '(', 4-2. v에 대해 1단계부터 재귀적으로 수행결과를 붙인다. 4-3. ')'를 다시 붙인다. 4-4. u의 첫번째와 마지막을 제거하고 나머지 문자열 괄호 뒤집에서 붙인다. 4-5. 반환한다.
# 균형 잡힌 문자열 'p'를 매개변수로 주어진다.

def solution(p):
    if p == '':
        return p
    u, v = divide(p)
    if check(u):
        return u + solution(v)
    else:
        tmp = '(' + solution(v) + ')'
        for x in u[1: -1]:
            if x == '(':
                tmp += ')'
            else:
                tmp += '('
            return tmp

def divide(p):
    left, right = 0, 0
    for k in range(len(p)):
        if p[k] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return p[:k+1], p[k+1:]
def check(u):
    q = []
    for x in u:
        if not q:
            q.append(x)
        else:
            if x == ')' and q[-1] == '(':
                q.pop()
            else:
                q.append(x)
    if q:
        return False
    return True