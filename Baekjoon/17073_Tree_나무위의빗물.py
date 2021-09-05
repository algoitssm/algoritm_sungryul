"""
W를 말단 노드 개수로 나눠준다
"""

import sys


def dfs(start):
    global terminal_node
    stack = [start]
    visited[start] = 1

    while stack:
        cur = stack.pop()
        sign = True

        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = 1
                stack.append(nxt)
                sign = False

        if sign:
            terminal_node += 1


N, W = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

visited = [0 for _ in range(N + 1)]
terminal_node = 0

dfs(1)
print(W / terminal_node)
