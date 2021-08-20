"""
각 컴퓨터 통해 해킹할 수 있는 컴퓨터의 수를 오름차순으로 정렬
모든 노드 다 탐색해야 한다.
"""
from collections import deque


def dfs(start):  # 시간초과
    # visited가 공통이 아니므로 초기화시켜줘야 함
    visited = [0 for _ in range(N + 1)]
    stack = [start]
    total = 0

    while stack:
        start = stack.pop()
        visited[start] = 1
        total += 1

        for w in graph[start]:
            if not visited[w]:
                stack.append(w)

    return total


def bfs(start):  # 시간 초과
    visited = [0 for _ in range(N + 1)]
    queue = deque()
    queue.append(start)
    total = 0

    while queue:
        num = queue.popleft()
        total += 1

        for nxt in graph[num]:
            if not visited[nxt]:
                queue.append(nxt)
                visited[nxt] = 1

    return total


N, M = map(int, input().split())  # N개는 노드 수, M은 엣지 수

graph = [[] for _ in range(N + 1)]

for _ in range(M):  # 단방향
    end, start = map(int, input().split())
    graph[start].append(end)

ans = []
max_val = 0

for i in range(1, N + 1):
    # total = dfs(i)
    total = bfs(i)
    if max_val < total:
        ans = [i]
        max_val = total
    elif max_val == total:
        ans.append(i)

print(*ans)
