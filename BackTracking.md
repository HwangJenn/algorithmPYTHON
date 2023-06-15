## 백트래킹, BackTracking
**백트래킹(BackTracking)의 정의**

현재 상태에서 가능한 모든 후보군을 따라 들어가며 탐색한다.

해가 아니거나 다시 돌아가서(=back) 최적의 해를 찾는다.

**백트래킹의 구현**

-   보통 백트래킹의 구현은 BFS와 DFS와 함께 구현한다.
-   재귀로 보통 구현되고, 재귀 함수가 호출되고 조건에 맞지 않으면 종료되고 그전에 호출된 재귀로 돌아오므로, 백트래킹에서 말하는 ‘가능성이 없으면 후보를 포기해 정답을 찾아가는’ 방식이다.
-   안되는 조건은 없애면서 탐색하기 때문에 시간복잡도가 선형적으로 증가할 법한 문제에서 백트래킹을 적용하면 시간복잡도를 줄일 수 있다.
-   모든 경우의 수에서 한정 조건을 만족하는 경우를 탐색하는 것이기 때문에 완전 탐색 기법인 BFS와 DFS가 모두 구현이 가능하다.
-   하지만 한정 조건에 부합하지 않는다면(Node 가 유망하지 않다면) 이전 수행(이전 Node)로 돌아와야 하기 때문에 BFS와 DFS의 구현이 더 편하다.
-   따라서 백트래킹을 구현할 때 가장 중요한 것이 한정 조건이다.
-   한정 조건을 걸어 완전탐색에서 유망하지 않은 시도를 걸러내는 것이 바로 백트래킹의 본질이다.

**백트래킹 동작 과정**

DFS와 백트래킹을 이용해 'AIR'라는 단어를 찾는 예시임.

<img src = "https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/18bc4b9a-9aa9-4b0e-86c1-c7c78bbacdc7" width = "300" />

1\. 현재 트리에 대해 DFS를 수행한다. -> 단어가 일치하거나, 모든 노드를 방문할 때 까지 진행한다.  
2\. 가지 치기(Pruning)을 통해 적합 하지 않은 부분(AN, AIM) 제거한다.3\. 가지 치기한 결과 트리에 대해 1의 과정을 다시 진행한다.

-   **가지 치기(Pruning)**
    -   불필요한 탐색 부분을 제거하는 방법
    -   트리 구조에서 나무 가지를 치듯이 가망성이 없는 부분을 제거해 나가는 것
    -   최종 결정에 영향을 주지 않는 부분을 쳐 내면서, 경우의 수를 줄여 나간다.
-   **Backtracking 과 Branch-&-Bound 비교** 
    -   공통점
        -   불필요한 탐색 부분을 제거하는 방법이다.
    -   차이점
        -   Backtracking은 가보고 더 이상 진행이 되지 않으면 돌아온다.
        -   Branch-&-Bound는 최적해를 찾을 가능성이 없으면 분기는 하지 않는다.

**백트래킹 구현 예시(백준 9663번 N-Queen)**

문제)

<img src = "https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/b15350c3-01c3-4edc-ae83-15db964a157b" width = "700" />

풀이)

예제 입력 값을 예로 들면 좋겠지만 풀이가 너무 길어질 것 같으니 N의 값을 4로 예를 들어 풀이한다.

4 x 4인 체스판 위에 퀸 4개를 서로 공격할 수 없도록 놓는 경우의 수를 구한다.

문제 조건과 예제 입력에 따라 다음과 같은 조건을 가진다.

1.  퀸이 놓였을 때 자신을 기준으로 가로 및 세로와 대각선 방향에는 아무것도 놓여있으면 안된다.
2.  열 위치가 같거나 행 위치가 같다면 같은 가로 및 세로 선상에 있기에 넘어간다.
3.  행 번호 차이 = 열 번호 차 이면 같은 대각선 상에 있다\->(2,1)의 행번호 2와 다른 퀸들의 열번호 차이가 ((1,0)와 (0,2) 열번호 차이 2)가 같다.

<img src = "https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/6890db64-3f75-4ffc-bcf5-8a986eaa896f" width = "300" />

```
<구현>
# 풀이에서 만든 조건의 2번에 따라 1차원 배열을 가지고 퀸들의 정보를 담는다.
# 만약 rows[i] = j 라는 값을 가진다면 이는 i행의 j열에 퀸이 놓여있다는 의미가 된다.
n = int(input())
annswer = 0
rows = [0] * n

#현재 놓은 퀸 자리가 유효한지 체크하는 함수
def is_valid(r):
		for i in range(r): #r범위 에서
				if rows[i] == rows[r]: #같은 세로(행)에 위치하면
						return False #유효하지 않다
				if abs(r - i) == abs(rows[r] - rows[i]): #같은 가로(열)에 위치하면
						return False #유효하지 않다
		return True #if 문을 통과하면 반환한다.

#r행에 퀸을 놓는다
def put_queen(r): #r행에 퀸을 놓는 함수를 설정한다.
		global answer #전역변수 설정
		ir r == n: #퀸을 n행까지 조건에 맞게 다 채워 넣은 경우
			answer += 1 #퀸을 놓기
			return #반환

		for i in range(n): #1부터 n까지의 범위에서
				rows[r] = i #r행에 i열에 퀸을 둔다
				if is_valid(r): #그 자리에 퀸을 놓을 수 있다면
					put_queen(r + 1) #다음행으로

put_quuen(0) #0행부터 시작
print(answer)#퀸들 출력
```

👇**백트래킹과 DFS의 차이**

| 백트래킹 | DFS |
| --- | --- |
| 탐색하는 알고리즘 | 탐색하는 알고리즘 |
| 불필요한 탐색은 하지 않는다. | 모든 경우의 수를 탐새한다. |
| 일단 가보고 후보해가 될 수 없으면 다음 단계로 진행하지 않고 되돌아 나온다. 유망하지 않은 경우의 수를 줄이는 것을 목표로 한다. | 완점 탐색을 기본으로 하는 그래프 순회 기법으로, 모든 노드를 방문하는 것을 목표로 한다. |

예) a = \[123, 142, 432\] 에서 123이라는 값을 찾고 있다고 했을 때,

| 백트레킹 | DFS |
| --- | --- |
| 숫자가 다르면 탐색을 더이상 진행하지 않고 다음 수로 넘어간다. | 원하는 수가 아니여도 트리의 바닥에 도달할 때 까지 탐색을 계속 한다. |

---

**\[참조\]**

> [https://wikidocs.net/131177](https://wikidocs.net/131177) #백트래킹  
> [https://blog.encrypted.gg/732](https://blog.encrypted.gg/732) #백트래킹 개념  
> [https://chanhuiseok.github.io/posts/baek-1/](https://chanhuiseok.github.io/posts/baek-1/) #문제 예시 백준 9663  
> [https://80000coding.oopy.io/85650ea5-e541-4b12-9b86-a958a99b7533](https://80000coding.oopy.io/85650ea5-e541-4b12-9b86-a958a99b7533) #백트래킹 정의  
> [https://velog.io/@seanlion/bfsdfs](https://velog.io/@seanlion/bfsdfs) #BFS,DFS,Backtracking  
> [https://gamedevlog.tistory.com/49](https://gamedevlog.tistory.com/49) #백트래킹 과정 예시
