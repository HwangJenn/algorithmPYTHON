### **깊이 우선 탐색(DFS, Depth-First Search)**

루트 노드(혹은 다른 임의의 노드)에서 시작해서 다음 분기(branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법

-   즉, 넓게(wide) 탐색하기 전에 깊게(deep) 탐색하는 것이다.
-   **모든 노드를 방문 하고자 하는 경우****에 이 방법을 선택한다.**  
    →너비 우선 탐색보다 좀 더 간단하다.  
      
    ➕참고
    -   스택(Stack) 자료구조를 이해 해야 힌다.

DFS 동작 과정과 구현

**\[탐색 방법\]**

1.  탐색 시작 노드를 스택에 삽입하고 방문처리 한다. (재방문 방지를 위함)
2.  스택 최상단 노드에 방문하지 않은 인접노드가 있다면 그 노드를 스택에 넣고 방문처리 한다. 인접노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3.  방문하지 않은 노드가 없을 때 까지 반복한다.

**\[동작 예시\]**

<img src = "https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/a3caddc6-7bf9-446f-b6fa-f5984a73ccac" width = "300" />

위 그래프를 DFS로 탐색한다.

👇**동작 상세 과정**

1\. 시작 노드인 1을 스택에 삽입하고 방문 처리한다.  
<img src = "https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/cf6025a9-83db-45bc-ba54-1719cbad0ee0" width = "350" />

2\. 스택 최상단 노드인 1 에게는 인접하지만 방문하지 않은 노드 2, 3 중 가장 작은 노드인 2를 스택에 넣고 방문 처리한다. (일반적으로 인접한 노드 중에서 방문하지 않은 노드가 여러개 있다면 번호가 낮은 순부터 처리한다.)  
<img width="350" alt="3" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/7dc656db-5234-4050-9468-a2e3980300fb">

3\. 스택의 최상단 노드인 2 에 방문하지 않은 인접 노드 4, 5 중 가장 작은 4 를 스택에 넣고 방문 처리 한다.  
<img width="352" alt="4" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/60d689f2-984d-4575-bbbb-db3edf63dd02">

4\. 스택 최상단 노드인 4 에 방문하지 않은 인접 노드 5 를 스택에 넣고 방문 처리한다.  
<img width="352" alt="5" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/19b41026-feef-4e1e-a9a4-e52fa7b894f5">

5\. 스택 최상단 노드인 5 에게는 방문하지 않은 인접 노드가 없기에 5 를 스택에서 제거한다.  
<img width="363" alt="6" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/126363f0-298f-47a3-a748-830ce4beb5b3">

6\. 스택 최상단 노드인 4 또한 방문하지 않은 인접 노드가 없기에 스택에서 제거한다.  
<img width="374" alt="7" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/5e9368eb-14a6-441a-bb22-0d9f2636b9b7">

7\. 스택 최상단 노드인 2 역시 4 와 동일하게 방문하지 않은 인접 노드가 없기에 스택에서 제거한다.  
<img width="379" alt="8" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/b8057beb-c2a7-48a3-8573-0094fdfdb7f1">

8\. 스택의 최상단 노드인 1 의 방문하지 않은 인접 노드 3 을 스택에 넣고 방문 처리 한다.  
<img width="364" alt="9" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/c38729b9-e255-47db-8cb7-b0724e9ca3ed">

9\. 스택 최상단 노드 3 의 방문하지 않은 인접 노드 6 을 스택에 넣고 방문 처리 한다.  
<img width="379" alt="10" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/ac14329a-0ea5-4d82-87a5-bb49837c1f2a">

10\. 스택 최상단 노드인 6 의 방문하지 않은 인접 노드 7 을 스택에 넣고 방문 처리 한다.  
<img width="375" alt="11" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/6423ccfe-db30-4c50-a71d-4652005a6ef6">

11\. 스택 최상단 노드 7 은 인접 노드가 없기에 스택에서 제거한다.   
<img width="376" alt="12" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/54efa1e8-40f5-44b0-ad71-c78565d64e59">

12\. 스택 최상단 노드 6 은 방문하지 않은 인접 노드가 없기에 스택에서 제거한다.  
<img width="386" alt="13" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/a6f785a2-3d01-4df1-b051-5cb9dbfbfa5c">

13\. 스택 최상단 노드 3 도 동일하게 방문하지 않은 인접 노드가 없기에 스택에서 제거한다.  
<img width="389" alt="14" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/ca2012df-aa7a-490a-af65-fb26711f5a7c">

14\. 스택 최상단 노드 1 도 동일하게 방문하지 않은 인접 노드가 없기에 스택에서 제거한다.  
<img width="376" alt="15" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/7bb046f0-dda3-454c-9a5c-9435def293ed">

15\. 모든 노드를 방문 했기에 탐색 종료 한다.  
<img width="376" alt="16" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/f615b552-1085-41de-9c40-30da6204c9f7">>


👉**노드의 탐색 순서(스택에 들어간 순서)  
1 - 2 - 4 - 5 - 3 - 6 - 7**

```
<구현>
# DFS는 BFS에 비해 구현이 간단하다. 시간 복잡도는 O(N)이며, 재귀 함수로 구현하면 굳이 스택을 사용하지 않아도 된다.
# 2차원 배열을 통해 노드 간의 연결 정보를 표현한다.
# 리스트 내 인덱스는 노드 번호를 의미하고 각 인덱스에 해당하는 원소에 해당 노드에 인접한 노드 번호가 담겨 있다.

graph = [
		[],      # 0
    [2, 3],  # 1 
    [4, 5],  # 2
    [6],     # 3
    [2, 5],  # 4
    [2, 4],  # 5
    [3, 7],  # 6
    [6]      # 7
]

#방문 정보를 기록하기 위한 리스트
visited = [False] * 8

def dfs(v):
		#방문 표시
		visited[v] = True
		#탐색 순서 출력
		print(v, end=' ')
		#그래프를 순환하면서 인접 노드들을 재귀적으로 방문처리
		for i in graph[v]:
					#만약 방문하지 않은 노드가 있다면
					if not visited[i]:
								#탐색 시작
								dfs(i)

#탐색 시작 노드 1을 넣어주며 dfs() 실행
dfs(1)
```

➕**왜 실제 그래프 내 노드 개수보다 2차원 배열에 원소 개수가 1개 더 많은가?**

노드 번호가 1부터 시작한다는 점에서, 리스트 내 원소의 인덱스와 노드 번호를 일치시키기 위해, 인덱스 0에 빈 리스트를 넣어줌으로써 기존 그래프 내 노드 개수보다 방문 정보를 담은 리스트 내 원소 개수를 1개 더 많게 세팅한다.

→ 인덱스와 노드 번호를 일치시켜 줌으로써 보다 직관적으로 노드 간의 연결 및 방문 정보를 파악 할 수 있도록 한다.

**DFS 장점**

-   현 경로상의 노드들만 기억하기 때문에 적은 메모리를 사용한다.(공간 복잡도)
-   목표 노드가 깊은 단계에 있는 경우 BFS 보다 빠르게 탐색 가능하다.

**DFS단점**

-   해가 없는 경로를 탐색 할 경우 단계가 끝날 때 까지 탐색한다.
    -   답이 아닌 경로가 매우 깊다면, 그 경로에 깊이 빠지게 된다.
    -   여러 경로 중 무한한 길이를 가지는 경로가 존재하고 해가 다른 경로에 존재하는 경우, 무한한 길이의 경로에서 빠져나오지 못해 영원히 종료 불가.
    -   효율성을 높이기 위해 미리 지정한 임의 깊이까지만 탐색하고(재귀함수로 구현한다고 했을 때 재귀 호출 횟수를 제한한다), 해를 발견하지 못하면 빠져나와 다른 경로를 탐색하는 방법을 사용해야 한다.
-   목표에 이르는 경로가 다수인 경우, DFS는 해에 도착하면 탐색을 종료하기에 얻어진 해가 최단 경로라는 보장이 없다.

### **너비 우선 탐색(BFS, Breadth-First Search)**

루트 노드(혹은 다른 임의의 노드)에서 시작해서 인접한 노드를 탐색하는 방법

-   즉, 깊게(deep) 탐색하기 전에 넓게(wide) 탐색하는 것이다.
-   **두 노드 사이의 최단 경로 혹은 임의의 경로를 찾고 싶을 때 이 방법을 선택한다.**
    -   예) 지구상에 존재하는 모든 친구 관계를 그래프로 표현한 수 두 친구 사이에 존재하는 경로를 찾는 경우.
    -   DFS의 경우 - 모든 친구 관계를 다 살펴봐야 할지도 모름.
    -   BFS의 경우 - 선택한 친구와 가까운 관계부터 탐색➕참고큐(Queue) 자료구조를 이해해야 한다.

BFS 동작 과정과 구현

**\[탐색 방법\]**

1.  탐색 시작 노드를 큐에 삽입하고 방문처리 한다. 재방문 방지를 위함)
2.  큐에서 노드를 꺼내 해당 노드의 방문하지 않은 모든 인접들을 모두 큐에 삽입하고 방문처리 한다.
3.  2번의 과정을 더 이상 수행할 수 없을 때 까지 반복한다.

**\[동작 예시\]**

<img src = "https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/88083a77-80ed-4179-8d4f-ca7eb5d9a071" width = "300" />

위 그래프를 BFS로 탐색한다.

👇**동작 상세 과정**

1\. 시작 노드인 1 을 큐에 삽입하고 방문 처리한다.  
<img width="378" alt="18" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/0e194085-3a43-4e81-a814-772d869b35ea">

2\. 1 을 큐에서 꺼내고, 꺼낸 노드의 인접 노드 2 와 3 을 큐에 삽입하고 방문 처리한다.  
<img width="374" alt="19" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/85271a93-4d45-414e-8611-41adb5411ad4">

3\. 큐에서 2 를 꺼내고 방문하지 않은 인접 노드 4 와 5 를 큐에 삽입하고 방문 처리한다.  
<img width="379" alt="20" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/c2f2796c-6e48-419d-86e7-9dbb4e9fe009">

4\. 큐에서 3 을 꺼내고 방문하지 않은 인접 노드 6 을 큐에 삽입하고 방문 처리한다.  
<img width="377" alt="21" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/70c301d4-edeb-4152-aa1d-a63848ef956b">

5\. 큐에서 4 를 꺼내고, 방문하지 않은 인접 노드가 없으므로 무시한다.  
<img width="377" alt="22" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/69a76c4c-041d-4c11-a152-6c649fec358b">

6\. 큐에서 5 를 꺼내고 방문하지 않은 인접 노드가 없으므로 무시한다.  
<img width="373" alt="23" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/df458afd-b17e-4220-a02f-3aac34cb62bc">

7\. 큐에서 6 울 꺼내고 방문하지 않은 인접 노드 7 을 큐에 삽입하고 방문 처리한다.  
<img width="376" alt="24" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/1d7c9dd2-da3a-47fb-8052-640faa2e462d">

8\. 큐에서 7 을 꺼내고 방문하지 않은 인접 노드가 없으므로 무시한다.  
<img width="372" alt="25" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/bbca7f13-e4d9-4b59-abe4-50df4f611ecf">

9\. 모든 노드를 방문했으므로 종료한다.  
<img width="374" alt="26" src="https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/023a85c3-7605-47ad-bfab-97bd420d06c4">


👉**노드의 탐색 순서(큐에 들어간 순서)**

**1 - 2 - 3 - 4 - 5 - 6 - 7**

```
<구현>
#BFS는 O(N)의 시간 복잡도를 가지고 있으며 queue를 사용하기에 deque 라이브러리를 사용한다. 일반적으로 BFS가 재귀로 구현한 DFS보다 조금 더 빠르게 동작한다.
from collections import deque

# DFS와 동일하게 그래프 구현
# 2차원 배열을 통해 노드 간의 연결 정보를 표현한다.
# 리스트 내 인덱스는 노드 번호를 의미하고 각 인덱스에 해당하는 원소에 해당 노드에 인접한 노드 번호가 담겨 있다.
graph = [
    [],      # 0
    [2, 3],  # 1 
    [4, 5],  # 2
    [6],     # 3
    [2, 5],  # 4
    [2, 4],  # 5
    [3, 7],  # 6
    [6]      # 7
]

# 노드별 방문 정보를 리스트로 표현
visited = [False] * 8

# BFS 메서드 정의
def bfs(v):
    # 큐 구현을 위해 deque 라이브러리 활용 및 노드 생성
    q = deque()
    q.append(v)
    # 방문 할 노드가 없을 때 까지 반복
    while q:
        # 큐에서 노드를 꺼내서 x에 저장
        x = q.popleft()
        print(x, end=' ')
        # 그래프를 탐색하다가 방문하지 않은 노드가 있다면
        for i in graph[x]:
            if not visited[i]:
                # 큐에 방문하라고 삽입하고 방문 처리
                q.append(i)
                visited[i] = True

# 탐색 시작 노드 1을 넣어주며 bfs() 실행
bfs(1)
```

➕**왜 실제 그래프 내 노드 개수보다 2차원 배열에 원소 개수가 1개 더 많은가?**

노드 번호가 1부터 시작한다는 점에서, 리스트 내 원소의 인덱스와 노드 번호를 일치시키기 위해, 인덱스 0에 빈 리스트를 넣어줌으로써 기존 그래프 내 노드 개수보다 방문 정보를 담은 리스트 내 원소 개수를 1개 더 많게 세팅한다.

→ 인덱스와 노드 번호를 일치시켜 줌으로써 보다 직관적으로 노드 간의 연결 및 방문 정보를 파악 할 수 있도록 한다.

**BFS 장점**

-   모든 경로를 탐색하기에 여러 해가 있을 경우에도 최단 경로임을 보장
-   최단 경로가 존재하면 깊이가 무한정 깊어져도 답을 찾을 수 있다.
    -   무한한 길이를 가지는 경로가 존재하더라도, 모든 경로를 동시에 탐색을 진행하기 때문에 탐색 가능하다.
-   노드의 수가 적고, 깊이가 얕은 해가 존재할 때 유리하다.
    -   탐색하는 트리 또는 그래프의 크기에 비례하는 시간 복잡도를 가진다.

**BFS 단점**

-   노드의 수가 많을수록 탐색 가지가 급격히 증가함에 따라 보다 많은 메모리를 필요로 한다.
    -   메모리 상의 확장된 노드들을 저장할 필요가 있기에 탐색하는 트리 또는 그래프의 크기에 비례하는 공간 복잡도를 가진다.

#### **DFS와 BFS의 차이점 정리**

| **DFS** | **BFS** |
| --- | --- |
| 스택 또는 재귀함수 | 큐 |
| 최적의 해라는 보장이 없다. | 항상 최적의 해임을 보장 |
| 그래프 규모가 클 때 사용 | 그래프 규모가 작을때 사용 |
| 특정 목표 노드를 찾을 때 사용 | 최단 경로를 찾을 때 사용 |

---

**\[참조\]**

> [https://veggie-garden.tistory.com/24](https://veggie-garden.tistory.com/24) #DFS  
> [https://heytech.tistory.com/56](https://heytech.tistory.com/56) #BFS  
> [https://heytech.tistory.com/55](https://heytech.tistory.com/55) #DFS  
> [https://veggie-garden.tistory.com/42](https://veggie-garden.tistory.com/42) #DFS와 BFS 예시



