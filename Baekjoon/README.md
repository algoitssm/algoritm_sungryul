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
