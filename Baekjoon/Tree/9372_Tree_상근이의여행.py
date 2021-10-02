import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    coun_cnt = 0

    while queue:
        cur = queue.popleft()

        for nxt in graph[cur]:
            if not visited[nxt]:
                queue.append(nxt)
                visited[nxt] = 1
                coun_cnt += 1

    return coun_cnt


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]

    for _ in range(M):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    ans = 0

    for i in range(1, N + 1):  # 루트가 여러 개인 경우 있는 듯, N-1로 하니 50%에서 오답
        if not visited[i]:
            ans += bfs(i)

    print(ans)
