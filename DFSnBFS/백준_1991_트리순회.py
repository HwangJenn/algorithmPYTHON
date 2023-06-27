# 이진 트리를 입력받아 전위순화(preorder traversal), 중위순회(inorder traversal), 후위순회(postorder traversal) 결과 출력
# 입력 첫째 줄 -> 이진트리의 노드의 개수 N, 입력 둘쨰줄 ~ N+1 -> 각 노드, 그의 왼쪽 오른쪽 자식 노드가 주어지는데 이는 알파벳 대문자 순서이고 항상 A가 루트노드가 된다. 자식노드가 없으면 '.'으로 표현
# 출력 첫째 줄 -> 전위순회, 출력 둘째줄 -> 중위 순회, 출력 셋쨰줄 -> 후위 순회 결과, N애의 알파벳 공백없이 출력

# 전위 순회(preorder traversal) : 루트 왼쪽 오른쪽, 중위 훈쇠(inorder traversal) : 왼쪽 루트 오른쪽, 후위 순회(postorder traversal) : 왼쪽 오른쪽 루트 순으로 방문
# 전위 순회(루트 왼쪽 오른쪽)을 얘로 들면 루트인 A방문 후 왼쪽 자식들을 모두 방문하기 위해 dfs로 실행하는 재귀문을 만든다

n = int(input()) #노드개수입력받기

graph = [[[] for _ in range(2)] for _ in range(26)] #알파벳 범위

def pre_order(root): #전위순화 루트 왼 오
    print(chr(root + ord('A')), end='') #w정해진 루트 A 설정
    if graph[root][0]: #왼쪽자식
        pre_order(graph[root][0][0])
    if graph[root][1]: #오른쪽자식
        pre_order(graph[root][1][0])

def in_order(root): #중위순회
    if graph[root][0]: #왼쪽자식
        in_order(graph[root][0][0])
    print(chr(root + ord('A')), end='') #루트
    if graph[root][1]: #오른쪽자식
        in_order(graph[root][1][0])

def post_order(root): #후위순회
    if graph[root][0]: #왼쪽자식
        post_order(graph[root][0][0])
    if graph[root][1]: #오른쪽자식
        post_order(graph[root][1][0])
    print(chr(root + ord('A')), end='') #루트

for i in range(n): #노드개수만큼
    a, b, c = input().split() #a루트 b왼쪽 c오른쪽

    if b != ".":  #왼쪽 끝나면
        graph[ord(a) - ord('A')][0].append(ord(b) - ord('A'))
    if c != ".": #오른쪽끝나면
        graph[ord(a) - ord('A')][1].append(ord(c) - ord('A'))

pre_order(0)
print()
in_order(0)
print()
post_order(0)