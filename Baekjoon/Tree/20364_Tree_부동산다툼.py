import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())

visited = [0 for _ in range(N + 1)]

for _ in range(Q):
    duck = int(input())

    if not visited[duck]:  # 오리가 가려는 곳 방문하지 않은 경우
        print(0)  # 0 출력
        queue = deque()  # 큐에 담으면서 * 2와 * 2 + 1인 곳 모두 duck으로 방문 체크. 더 먼저 만나는 숫자로 계속 갱신됨
        queue.append(duck)
        while queue:
            cur = queue.popleft()
            visited[cur] = duck
            if cur * 2 <= N:
                queue.append(cur * 2)
            if cur * 2 < N:
                queue.append(cur * 2 + 1)

    else:  # 지금까지의 가장 앞 노드 출력
        print(visited[duck])
