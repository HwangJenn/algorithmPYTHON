# 두개의 단어 begin, target과 단어의 집합 words가 있다. 규칙 1) 한번에 한개의 알파벳만 바꿀 수 있다. 2) word에 있는 단어로만 변환할 수 있다 는 규칙이 있을 때 begin에서 target으로 변환하는 가장 짧은 변환 과정은?

# 규칙 1)은 현재 선택한 단어와 한글자 차이가 있는 알파벳만 모두 얻게 하는 bfs를 이용한다. begin과 단 한글자 차이만 있는 단어들을 모두 stack에 넣는다
# 규칙 2)에 의해 1에서 넣은 단어들과 단 한 글자 차이만 있는 단어들을 stack에 넣는다. bfs를 통해 stack에서 꺼낸 원소가 target과 일치하는지 확인하라

def bfs(begin, target, word, visited):
    count = 0
    stack = [(begin, 0)]
    while stack:
        cur, depth = stack.pop()
        if cur == target:
            return depth

        for i in range(len(word)):
            if visited[!] == True:
                continue
            count = 0
            for a, b in zip(cur, words[i]):
                if a != b:
                    count += 1
            if count == 1:
                visited[i] = True
                stack.append((words[i], depth + 1))

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0

    visited = [False] * (len(words))

    answer = bfs(begin, target, words, visited)

    return answer