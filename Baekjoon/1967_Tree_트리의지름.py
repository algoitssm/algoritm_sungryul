"""
1. root ~ terminal까지 최대 값인 terminal node 탐색
2. 해당 terminal node에서 다시 탐색하여 최대값인 곳 탐색
"""

import sys
from collections import deque


def bfs(start):
    global max_total, max_terminal
    queue = deque()
    queue.append(start)
    visited[start] += 1
    cnt = 1

    while queue:
        cur = queue.popleft()

        for nxt in tree[cur]:
            if visited[nxt[0]] == -1:
                queue.append(nxt[0])
                visited[nxt[0]] = visited[cur] + nxt[1]
                if visited[nxt[0]] > max_total:
                    max_total = visited[nxt[0]]
                    max_terminal = nxt[0]
                cnt += 1
        if cnt == n:
            break


input = sys.stdin.readline

n = int(input())  # 노드의 개수

if n == 1:  # 노드 1개일 때
    print(0)
else:
    tree = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        parent, child, weight = map(int, input().split())
        tree[parent].append((child, weight))  # 양 방향으로 탐색해줘야 하므로 두 방향 모두 트리에 넣음
        tree[child].append((parent, weight))

    visited = [-1 for _ in range(n + 1)]
    max_total = 0
    max_terminal = 0

    bfs(1)
    # max_terminal 찾고 나서 초기화 필요
    max_total = 0
    visited = [-1 for _ in range(n + 1)]
    bfs(max_terminal)
    print(max_total)
