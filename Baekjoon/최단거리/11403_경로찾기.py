"""
인접 리스트가 주어지고 정점 i에서 j로 가는 경로가 있는지 확인하는 문제
자기 자신으로 가는 길은 항상 0. 다른 경로 통해 돌아오는 지 확인
"""
from collections import deque


def bfs(start):
    visited = [0] * N
    q = deque()
    q.append(start)

    while q:
        cur = q.popleft()

        for v in range(N):
            if not visited[v] and G[cur][v]:
                q.append(v)
                visited[v] = 1
                ans[start][v] = 1


N = int(input())

G = [list(map(int, input().split())) for _ in range(N)]
ans = [[0] * N for _ in range(N)]

for s in range(N):
    bfs(s)

for r in range(N):
    print(*ans[r])
