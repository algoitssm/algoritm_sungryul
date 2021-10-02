import sys
from collections import deque

N = int(input())

data = []

for _ in range(N):
    data.append(int(sys.stdin.readline().rstrip()))

# 핵심은 순서로 상쇄되는 값을 최소값을 넣어서 상쇄값 최소화
data.sort(reverse = True)
data = deque(data)

ans = 0
i = 0

while len(data) > 0:
    if data[0] > i:
        ans += data.popleft() - i
        i += 1
    else:
        data.popleft()

print(ans)