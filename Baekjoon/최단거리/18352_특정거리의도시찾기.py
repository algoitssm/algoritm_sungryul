"""
가중치 없기 때문에 bfs로 풀어도 상관 X
"""
# N 도시 개수  M 도로 개수  K 거리 정보  X 출발 도시
from collections import deque
import heapq


def bfs(start):
    q = deque()
    q.append(start)
    visited = [-1] * (N + 1)
    visited[start] += 1
    cnt = 1

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if visited[nxt] == -1:
                visited[nxt] = visited[cur] + 1
                q.append(nxt)
                cnt += 1
                if visited[nxt] == K:
                    heapq.heappush(ans, nxt)
        if visited[cur] > K:
            break


N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

ans = []

bfs(X)

if ans:
    while ans:
        print(heapq.heappop(ans))
else:
    print(-1)
