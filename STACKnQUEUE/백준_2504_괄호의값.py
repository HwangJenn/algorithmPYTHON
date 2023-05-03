# 4의 기호 ( ) [ ]을 이용해 만들어지는 괄호열 중에서 올바른 괄호열의 정의
# 한 쌍의 괄호로만 이루어진 ()와 []은 올바른 괄호이다. 만일 x가 올바른 괄호열이면 (x)이나 [x]도 모두 올바른 괄호열이된다. x와 y 모두 올바른 괄호열이라면 이들을 결합한 xy도 올바른 괄호열이된다.
# 괄호값 정의
# ()은 2, []은 3, (x)은 2 x 값(x), [x]은 3 x 값(x), 올바른 괄호열 x와 y가 결합된 xy 괄호값으 값(xy) = 값(x) + 값(y)으로 계산된다
# 주어진 괄호열을 읽고 그 괄호값을 앞에서 정의한대로 계산해 출력하라
# 입력 첫째줄 -> 괄호열을 나타내는 문자열이 주어진다.
# 출력 첫째줄 -> 그 괄호열의 값을 나타내는 정수를 출력한다. 입력이 올바르지 못한 괄호열이면 반드시 0을 출력하라

# 스택을 이용해 푼다. 열린 괄호를 만나면 스택에 넣어주고 닫힌 괄호를 만나면 스택의 top을 꺼낸다.
# 꺼낸 괄호가 닫는 괄호일 때 괄호 입력 배열에서의 그 괄호의 바로 직전의 괄호가 쌍이 맞는 경우에만 곱하기를 한다.

bracket = list(input()) #괄호열을 나탙내는 문자열 입력받기

stack = [] #스택
answer = 0 #괄호열의 값을 나타내는 정수
tmp = 1 #괄호값

for i in range(len(bracket)): #괄호열의 값 정리
    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2
    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3
    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if bracket[i - 1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if bracket[i - 1] == "[":
            answer += tmp

        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)