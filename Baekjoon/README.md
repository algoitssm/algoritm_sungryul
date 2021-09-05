## ✅1343

- 통과 코드

``` python
board = input()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    print(board)
```

- 의문 코드 ➡ 해결!

```python
board = input()

cnt = 0
result = []

if len(board) <= 1:
    # 입력 '.'일 경우가 마지막 테스트 케이스
    if board == ".":  # 길이가 1이하일 때 무조건 -1 하려다가 계속 오답...
        print(".")
    else:
        print(-1)

else:
    for char in board:
        if char == 'X':
            cnt += 1
            if cnt == 2:
                result.append(poly[1])
            if cnt == 4:
                result[-1] = poly[0]
                cnt = 0
        else:
            if cnt % 2:
                result = -1
                break
            else:
                cnt = 0
                result.append('.')
    
    if result == -1:
        print(result)
    elif cnt == 1 or cnt == 3:
        print(-1)
    else:
        print(''.join(result))
```

## ✅11000

- 처음 풀이

```python
N = int(input())

time_table = [0] * (10 ** 9)

ans = 0

for _ in range(N):
    start, end = map(int, input().split())
    for i in range(start, end):
        time_table[i] += 1
        if time_table[i] > ans:
            ans = time_table[i]

print(ans)

```

숫자 갯수만큼 0인 리스트를 만들고 start, end 값을 받아오면서 1씩 더해 최대값을 출력하도록 함

하지만 10 ** 9 숫자 크기가 너무 커서 메모리 초과 발생

- 두 번째 풀이

```python
import heapq

N = int(input())

data = [tuple(map(int, input().split())) for _ in range(N)]
data.sort(key=lambda x: (x[0], x[1]))

# 강의실 별 끝 시간 저장할 큐
queue = []
heapq.heappush(queue, data[0][1])

for i in range(1, len(data)):
    # 가장 먼저 끝나는 강의의 끝 시간보다 나중에 시작하는 경우, 같은 강의실 사용하므로 해당 강의실 끝 시간 바꿔줌
    if data[i][0] >= queue[0]:
        heapq.heappop(queue)
        heapq.heappush(queue, data[i][1])
    # 가장 먼저 끝나는 강의의 끝 시간보다 먼저 시작하는 경우, 강의실 하나 더 필요하므로 큐에 그냥 추가
    else:
        heapq.heappush(data[i][1])

print(len(queue))
```

혼자 해결하지 못 하고 구글링 결과 나온 heapq 사용한 풀이 참고.

하지만 여기서도 시간 초과 문제 발생

- 최종 풀이

```python
import sys
import heapq

N = int(sys.stdin.readline())

data = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
data.sort(key=lambda x: x[0])

# 강의실 별 끝 시간 저장할 큐
queue = []
heapq.heappush(queue, data[0][1])

for i in range(1, N):
    # 가장 먼저 끝나는 강의의 끝 시간보다 나중에 시작하는 경우, 같은 강의실 사용하므로 해당 강의실 끝 시간 바꿔줌
    if data[i][0] >= queue[0]:
        heapq.heappop(queue)
        heapq.heappush(queue, data[i][1])
    # 가장 먼저 끝나는 강의의 끝 시간보다 먼저 시작하는 경우, 강의실 하나 더 필요하므로 큐에 그냥 추가
    else:
        heapq.heappush(queue, data[i][1])

print(len(queue))
```

input() 부분을 sys.stdin.readline()으로 수정하고, 정렬 또한 시작 시간 순서대로만 있으면 충분하므로 x[1] 삭제

## ✅17836 공주님을 구해라

### 1. 첫 시도 - not_gram 함수로 탐색하다가 2를 만나면 with_gram 함수로 탐색하여 둘의 값 비교

```python
import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline


def not_gram(start):
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] += 1
    if start[0] == N - 1 and start[1] == M - 1:
        return visited[start[0]][start[1]]
    gram = False

    while queue:
        cur_row, cur_col = queue.popleft()

        for i in range(4):
            nxt_row = cur_row + dr[i]
            nxt_col = cur_col + dc[i]

            if (
                0 <= nxt_row < N
                and 0 <= nxt_col < M
                and visited[nxt_row][nxt_col] == -1
                and data[nxt_row][nxt_col] != 1
            ):
                visited[nxt_row][nxt_col] = visited[cur_row][cur_col] + 1
                if visited[nxt_row][nxt_col] > T:
                    if gram:
                        return gram
                    return "Fail"
                if data[nxt_row][nxt_col] == 2:
                    gram = with_gram((nxt_row, nxt_col))
                elif data[nxt_row][nxt_col] == 0:
                    queue.append((nxt_row, nxt_col))
                    if nxt_row == N - 1 and nxt_col == M - 1:
                        if gram:
                            return min(gram, visited[nxt_row][nxt_col])
                        return visited[nxt_row][nxt_col]
    if gram:
        return gram
    return "Fail"


def with_gram(start):
    queue_gram = deque()
    queue_gram.append(start)
    visited_gram = deepcopy(visited)

    while queue_gram:
        cur_row, cur_col = queue_gram.popleft()
        for i in range(4):
            nxt_row = cur_row + dr[i]
            nxt_col = cur_col + dc[i]

            if 0 <= nxt_row < N and 0 <= nxt_col < M and visited_gram[nxt_row][nxt_col] == -1:
                queue_gram.append((nxt_row, nxt_col))
                visited_gram[nxt_row][nxt_col] = visited_gram[cur_row][cur_col] + 1
                if visited_gram[nxt_row][nxt_col] > T:
                    return False
                if nxt_row == N - 1 and nxt_col == M - 1:
                    return visited_gram[nxt_row][nxt_col]
    return False


N, M, T = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

visited = [[-1 for _ in range(M)] for _ in range(N)]

ans = not_gram((0, 0))

print(ans)
```

=> 57%에서 <span style="color:red">틀렸습니다.</span>

### 2. 스터디 이후 두 번째 시도 - with_gram 함수 사용하지 않고 바로 계산

```python
def not_gram(start):
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] += 1
    if start[0] == N - 1 and start[1] == M - 1:
        return visited[start[0]][start[1]]
    gram = False

    while queue:
        cur_row, cur_col = queue.popleft()

        for i in range(4):
            nxt_row = cur_row + dr[i]
            nxt_col = cur_col + dc[i]

            if (
                0 <= nxt_row < N
                and 0 <= nxt_col < M
                and visited[nxt_row][nxt_col] == -1
                and data[nxt_row][nxt_col] != 1
            ):
                visited[nxt_row][nxt_col] = visited[cur_row][cur_col] + 1
                if visited[nxt_row][nxt_col] > T:
                    if gram:
                        return gram
                    return "Fail"
                # 수정한 부분
                if data[nxt_row][nxt_col] == 2:
                    gram = visited[nxt_row][nxt_col] + abs(N - 1 - nxt_row) + abs(M - 1 - nxt_col)
                elif data[nxt_row][nxt_col] == 0:
                    queue.append((nxt_row, nxt_col))
                    if nxt_row == N - 1 and nxt_col == M - 1:
                        if gram:
                            return min(gram, visited[nxt_row][nxt_col])
                        return visited[nxt_row][nxt_col]
    if gram:
        return gram
    return "Fail"


N, M, T = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

visited = [[-1 for _ in range(M)] for _ in range(N)]

ans = not_gram((0, 0))

print(ans)
```

=> 20% 정도에서 <span style="color:red">틀렸습니다.</span>

### 3. 최종 통과 코드

```python
"""
0: 빈 공간 / 1: 벽 / 2: 그람
도달하면 최단 시간 출력
도달 못 하면 Fail 출력
"""

import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline


def not_gram(start):
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] += 1
    if start[0] == N - 1 and start[1] == M - 1:
        return visited[start[0]][start[1]]
    gram = False

    while queue:
        cur_row, cur_col = queue.popleft()

        for i in range(4):
            nxt_row = cur_row + dr[i]
            nxt_col = cur_col + dc[i]

            if (
                0 <= nxt_row < N
                and 0 <= nxt_col < M
                and visited[nxt_row][nxt_col] == -1
                and data[nxt_row][nxt_col] != 1
            ):
                visited[nxt_row][nxt_col] = visited[cur_row][cur_col] + 1
                if data[nxt_row][nxt_col] == 2:
                    gram = visited[nxt_row][nxt_col] + abs(N - 1 - nxt_row) + abs(M - 1 - nxt_col)
                    ans.append(gram)
                elif data[nxt_row][nxt_col] == 0:
                    queue.append((nxt_row, nxt_col))
                    if nxt_row == N - 1 and nxt_col == M - 1:
                        ans.append(visited[nxt_row][nxt_col])


N, M, T = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

visited = [[-1 for _ in range(M)] for _ in range(N)]

ans = []
not_gram((0, 0))

if ans:
    if min(ans) <= T:
        print(min(ans))
    else:
        print("Fail")
else:
    print("Fail")
```

마지막 점에 도달할 수 있는 경우의 수를 모두 `ans`에 넣고 마지막에 최소값을 뽑아서 풀이

=> 왜 위에서는 통과를 못하고 아래에서는 통과했는지 의문....

