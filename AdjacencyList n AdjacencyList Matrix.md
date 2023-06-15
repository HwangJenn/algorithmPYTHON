## 인접 리스트(Adjacency List)와 인접 행렬(Adjacency Matrix)
간선으로 연결되어 있는 노드들은 인접하다(adjacent)라고 표현하며, 그래프를 구현하는 방식은 다음과 같다.
#
## 인접리스트(Adjacency List)

그래프를 표현하는 가장 일반적인 방법. 

연결 리스트를 활용해 표현하는 방식.

-   모든 정점을 인접 리스트에 저장한다. 즉, 각각의 정점에 인접한 정점들을 리스트로 표시한다.
    -   배열(해시테이블)과 배열의 각 인덱스 마다 존재하는 또 다른 리스트(배열, 동적 가변 크기 배열(ArrayList), 연결리스트(LinkedList) 등)를 이용해서 인접 리스트를 표현
    -   정점의 번호만 알면 이 번호를 배열의 인덱스로 하여 각 정점의 리스트에 쉽게 접근할 수 있다.

```
예)
0: 1
1: 2
2: 0, 3
3: 2
4: 6
5: 4
```

-   무방향 그래프에서 (a, b) 간선은 두번 저장된다.
    -   한 번은 a 정점에 인접한 간선을 저장하고 다른 한 번은 b에 인접한 간선을 저장한다.
    -   정점의 수: N, 간선의 수: E인 무방향 그래프의 경우 → N개의 리스트, N개의 배열, 2E의 노드가 필요.
-   트리에선 특정 노드 하나(루트 노드)에서 다른 모든 노드로 접근이 가능 **→** **Tree 클래스 불필요**
    -   그래프에선 특정 노드에서 다른 모든 노드로 접근이 가능하지는 않음 **→** **Graph 클래스 필요**

```
class Graph { public Node[] nodes; }
//트리의 노드 클래스와 동일
class Node {
	public String name;
	public Node[] children;
}
```

-   C나 Java같은 언어들은 배열을 사용할 때 미리 배열의 크기를 지정하고 선언해야하는 반면, 파이썬의 리스트는 append()와 같은 메소드를 가지고 있으므로 배열과 연결 리스트의 기능이 모두 제공된다. 따라서 파이썬으로는 2차원 배열로도 그래프를 표현하기 충분하다.

인접리스트 예시)

<img src = "https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/93929126-4d8e-4805-a037-7fadf2d86cec" width = "300" />

```
<구현>
graph = [[] for _ in range(4)]

#노드 A
graph[0].append('B')
graph[0].aooebd('C')

#노드 B
graph[1].append('A')

...

graph = [['B','C'], ['A', 'C', 'D'], ['A', 'B'], ['B']]
```

➕참고

배열을 선언할 때부터 길이가 이미 정해져 있어 변경이 불가하다. 따라서 이를 해결하기 위해 동적인 메모리 구성이 등장했다.

쉽게 설명하면, 변수를 생성할 때마다 ‘데이터를 저장할 장소’와 ‘다음 변수의 위치를 저장하는 장소’를 구분하여 생성한 뒤, 데이터와 위치를 모두 저장하는 것이다.
#
## 인접행렬(Adjacency Matrix)

인접 행렬은 NxN 크기의 불린 행렬(Boolean Matrix)로써 matrix\[i\]\[j\]가 true라면 i → j 로의 간선이 있다는 것을 뜻함.

2차원 배열을 활용해 그래프를 표현하는 방식.

-   0과 1을 이용한 정수 행렬(Integer Matrix)을 사용할 수 있다.

<img src = "https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/8a375c91-60b2-426f-8714-b86c4bab01c1" width = "400" />

```
<구현>
if(간선 (i, j)가 그래프에 존재)
	matrix[i][j] = 1;
else
	matrix[i][j] = 0;
```

```
graph = [
		[0, 1, 1, 0],
		[1, 0, 1, 1],
		[1, 1, 0, 0],
		[0, 1, 0, 0]
}
```

-   정점의 개수가 N인 그래프를 인접 행렬로 표현
    -   간선의 수와 무관하게 항상 n^2개의 메모리 공간이 필요
-   무방향 그래프를 인접 행렬로 표현한다면 이 행렬은 대칭 행렬(Symmetric Matrix)이 된다.
    -   물론 방향 그래프는 대칭 행렬이 안될 수 있다.
-   인접 리스트를 사용한 그래프 알고리즘들(예: BFS) 또한 인접 행렬에서도 사용이 가능.
    -   그러나 인접 행렬은 효율성이 떨어진다.
    -   인접 리스트는 어떤 노드에 인접한 노드들을 쉽게 찾을 수 있으나 인접 행렬에서는 인접한 노드를 찾기 위해서는 모든 노드를 전부 순회해야 한다.

#
### **연결 리스트와 인접 행렬 중 선택방법**

**인접리스트**→ 그래프 내에 적은 숫자의 간선만을 가지는 희소 그래프(Sparse Graph)의 경우

-   장점
    -   어떤 노드에 인접한 노드들을 쉽게 찾을 수 있다
    -   그래프에 존재하는 모든 간선의 수는 O(N + E)안에 알 수 있다. → 인접 리스트 전체를 조사한다.
-   단점
    -   간선의 존재 여부와 정점의 차수: 정점 i의 리스트에 있는 노드의 수 → 정점 차수만큼의 시간이 필요.

**인접행렬**

→ 그래프에 간선이 많이 존재하는 밀집 그래프(Dense Graph)의 경우

-   장점
    -   두 정점을 연결하는 간선의 존재 여부(M\[i\]\[j\]를 O(1)안에 즉시 알 수 있다.
    -   정점의 차수는 O(N)안에 알 수 있다. → 인접 배열의 i 번째 행 또는 열을 모두 더한다.
-   단점
    -   어떤 노드에 인접한 노드들을 찾기 위해서는 모든 노드를 전부 순회해야한다.
    -   그래프에 존재하는 모든 간선의 수는 O(N^2) 안에 알 수 있다 → 인접 행렬 전체를 조사한다.

---

**\[참조\]**

> [https://veggie-garden.tistory.com/28](https://veggie-garden.tistory.com/28) 
> #인접 리스트와 인접 행렬 [https://sarah950716.tistory.com/12](https://sarah950716.tistory.com/12) #인접 리스트와 인접 행렬