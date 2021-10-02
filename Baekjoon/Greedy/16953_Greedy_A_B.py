""" 정수 A를
1. 2를 곱한다.(* 2)
2. 1을 수의 가장 오른쪽에 추가한다.(* 10 + 1)
중 하나의 연산을 하며 B를 만들면 연산 횟수를,
못 만들면 -1을 반환하는 문제
"""

# BFS 비슷하게 풀이 위해 deque 활용
from collections import deque

A, B = map(int, input().split())
# 처음에 A를 queue에 넣어준다
queue = deque()
queue.append(A)
# 만들 수 없는 경우 판단 위해 최소값 변수 정의
min_val = A
# 결과 맞추기 위해 1부터 시작
ans = 1

while True:
    # FIFO
    num = queue.popleft()
    # 각 연산 결과 append
    num_1 = num * 2
    num_2 = num * 10 + 1
    # * 2 연산만 한 값이 최소값이므로 최소값 때마다 갱신
    if num_1 == min_val * 2:
        min_val = num_1
    # 같은 수 만듷어지면 break
    if num_1 == B or num_2 == B:
        # ans는 A에 2가 곱해진 횟수
        while min_val > A:
            min_val //= 2
            ans += 1
        break
    # 최소값이 B보다 커지는 경우 불가능
    if min_val > B:
        ans = -1
        break
    # B보다 큰 숫자의 경우, 큐에 넣어줄 필요 없음
    if num_1 > B:
        continue
    queue.append(num_1)
    if num_2 > B:
        continue
    queue.append(num_2)


print(ans)
