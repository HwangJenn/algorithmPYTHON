## 큐(Queue)

선입선출(FIFO, First In First Out). 즉, 먼저 입력/삽입 된 데이터부터 출력/제거 하는 방식이다.

한쪽은 입력, 한쪽은 출력이 가능한 단방향 구조이다.

<img src = "https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/781e2b75-8d1b-491a-8201-ac4eaedb5767" width = "500" />

-   큐는 데이터 삽입(append)와 데이터 삭제(popleft) 이 핵심적인 함수로 동작한다.
    -   append 함수: 리스트 내, 좌측에서 우측 순서대로(index 증가) 데이터를 추가해 준다.
    -   popleft 함수: 리스트 내, 가장 좌측에 있는 데이터 한개를 삭제해 준다.
-   큐 사용할 때, 오버플로우(overflow)와 언더플로우(underflow) 발생에 유의해야 한다.
    -   오버플로우(overflow): 큐에 저장할 수 있는 데이터의 크기를 초과한 상태에서 데이터 삽입을 수행할 때 발생한다.
    -   언더플로우(underflow): 큐에 데이터가 전혀 없는 상태에서 데이터 삭제를 수행할 때 발생한다.
-   앞뒤에서 데이터 삽입 삭제가 바로 이루어 지기 때문에 원소 삽입, 삭제의 시간 복잡도는 O(1)이다.
-   데이터 접근, 삽입, 삭제가 빠르며 중간에 있는 데이터에 대한 접근이 불가능하다.
-   BFS 알고리즘, 프로세스 관리, 대기 순서 관리 등에서 활용 된다.

```
<구현>

# deque의 데이터 입출력 속도가 list(자료형)보다 효율적이기에 queue 라이브러리 대신 deque 라이브러리를 사용해 queue 자료구조 구현을 한다
from collections import deque

#큐 자료구조 구현을 위해 deque 라이브러리를 가져온다
queue = deque()

# append 함수를 이용해 데이터를 입력하고 popleft 합수를 사용해 데이터를 삭제한다.
queue.append('''입력할 데이터''') # 데이터 입력. 리스트 내에 좌측부터 입력된다.
...
queue.popleft() # 먼저 입력된 데이터 차례로 삭제 
...

print(queue) # 먼저 입력된 데이터부터 차례대로 출력
print(queue.reverse()) # 나중에 입력된 데이터부터 차례대로 출력
```
#
## 스택(Stack)

선입후출(Last In First Out). 즉, 마지막에 들어온 데이터부터 출력/제거 하는 방식이다.

가장 먼저 넣은 데이터가 맨 아래에 위치하는 박스 쌓기와 비슷한 형태이다.

<img src = "https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/6a8f2432-473f-4f42-ba55-5c74eab38d1c" width = "200" />

입력 순 A - B - C라고했을 때, 출력은 C - B - A 순으로 출력 된다.

-   스택은 데이터 삽입(push)와 데이터 삭제(pop)이 핵심적인 함수로 동작한다.
-   스택 사용할 때, 오버플로우(overflow)와 언더플로우(underflow) 발생에 유의해야 한다.
    -   오버플로우(overflow): 스택에 저장할 수 있는 데이터의 크기를 초과한 상태에서 데이터 삽입을 수행할 때 발생한다.
    -   언더플로우(underflow): 어떠한 자료구조에 데이터가 전혀 없는 상태에서 데이터 삭제를 수행할 때 발생한다.
-   top을 통해 접근하기 때문에 데이터 접근, 삽입, 삭제가 빠르고 시간 복잡도는 O(1)이다.
-   top 위치 이외에 데이터에 접근할 수 없으므로 탐색할 수 앖다. 탐색하려면 모든 데이터를 꺼내면서 진행해야 한다.
-   재귀 알고리즘, DFS 알고리즘, 역순 문자열 만들기, 웹 브라우저 방문 기록 등에서 활용된다.

```
<구현>

stack = []

# append 함수를 이용해 데이터를 입력하고 pop함수를 이용해 데이터를 삭제한다.
stack.append('''입력할 데이터''') # 데이터 입력. 리스트 내에 좌측부터 입력된다.
...
stack.pop() #가장 죄근에 입력 된 데이터부터 삭제
...

print(stack) # 스택 내 최하단 원소부터 데이터 출력 -> 남은 데이터 중 제일 먼저 입력 된 데이터 부터 출력
print(stack[::-1]) # 스택 내 최상단 데이터 출력 -> 남은 데이터 중 제일 나중에 입력 된 데이터 부터 출력
```

#
## 덱(Deque)

Double-Ended Queue. 즉, 단방향 입출력만 가능한 스택과 큐와 달리 양쪽에서 입출력이 가능하다.

<img src = "https://github.com/JXHXXN/algorithmPYTHON/assets/76980015/377b8cf5-4539-4b5e-a723-00d332c4c151" width = "500" />

-   메모리 앞, 뒤에서 데이터 입출력이 가능하다.
-   삽입, 삭제 연산은 O(1)의 시간 복잡도를 가지고, 스택/큐와 달리 index를 통해 요소들에 탐색할 수 있으므로 O(1)의 시간 복잡도를 가진다.
-   데이터의 삽입 삭제가 빠르고 앞, 뒤에서 삽입 삭제가 모두 가능하다.
-   가변적 크기이다.
-   새로운 원소 삽입 시, 메모리를 재할당 하고 복사하지 않고 새로운 단위의 메모리 블록을 할당해 삽입한다.
-   중간에서의 삽입 삭제가 어렵다.
-   스택, 큐에 비해 비교적 구현이 어렵다.
-   중간 데이터 삽입은 앞, 뒤에서의 삽입 삭제 성능에 비해 좋지 않다.

```
<Deque 사용법 및 구현>

#collections 모듈 및 deque import
from collections import deque

#deque 생성
dq = deque()
print(dq) 
#출력 결과: deque([])

#append(): deque 오른쪽(뒤)에 값 추가
dq.append(5)
dq.append(6)
print(dq)
#출력 결과: deque([5,6])

#appendleft(): deque 왼쪽(앞)에 값 추가
dq.appendleft(4)
dq.appendleft(3)
print(dq)
#출력 결과: deque([3,4,5,6])

#extend(): deque 오른쪽에 iterable 객체(반복이 가능한 객체 ex)리스트)를 순환하며 값들을 차례로 추가
dq.extend([7, 8, 9])
print(dq)
#출력 결과: deque([3,4,5,6,7,8,9])

#extendleft(): deque 왼쪽에 iterable 객체를 순환하며 값들을 차례로 추가
dp.extendleft([2,1,0])
print(dq)
#출력 결과: deque([0,1,2,3,4,5,6,7,8,9])

#remove(): deque 안의 특정 값 삭제
dq.remove(7)
dq.remove(8)
dq.remove(9)
print(dq)
#출력 결과: deque[(0,1,2,3,4,5,6)]

#pop(): deque 오른쪽의 값 삭제 후 반환
popValue = dq.pop()
print(popValue)
#출력 결과: 6
print(dq)
#출력 결과: deque([0,1,2,3,4,5)]

#popleft(): deque 왼쪽의 값 삭제 후 반환
popValue = dq.popleft()
print(popValue)
#출력 결과: 0
print(dq)
#출력 결과: deque([1,2,3,4,5])

#rotate(): deque 안의 값들 회전 -> rotate()힘수의 인자로 전달한 값만큼 회전하며 음수를 전달하면 거꾸로 회전한다.
print(dq)
#출력 결과: deque([1.2.3.4.5])
dq.rotate(1)
print(dq)
#출력 결과: deque([5,1,2,3,4,])
dq.rotate(-1)
print(dq)
#출력 결과: deque([1,2,3,4,5])
dq.rotate(-1)
print(dq)
#출력 결과: deque([2,3,4,5,1])
```
#
### **list로도 구현이 가능한데 deque을 사용하는 이유**

-   pop, popleft, append, appendleft 를 사용해 list와 deque 중 덱이 속도가 훨씬 빠르기 때문이다. 

---

**\[참조\]**

> [https://heytech.tistory.com/54](https://heytech.tistory.com/54) #큐  
> [https://heytech.tistory.com/46](https://heytech.tistory.com/46) #스택  
> [https://velog.io/@nnnyeong/자료구조-스택-Stack-큐-Queue-덱-Deque](https://velog.io/@nnnyeong/자료구조-스택-Stack-큐-Queue-덱-Deque) #스택, 큐, 덱  
> [https://velog.io/@dramatic/Python-Deque](https://velog.io/@dramatic/Python-Deque) #덱을 사용하는 이유  
> [https://hellominchan.tistory.com/156](https://hellominchan.tistory.com/156) #덱 사용법
