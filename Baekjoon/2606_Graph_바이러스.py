"""
1번 컴퓨터부터 시작하여 바이러스에 걸린 연결된 컴퓨터 수를 구하는 문제
모든 경우의 수 고려해야 하므로, DFS, BFS 상관 X
"""
from collections import deque


def dfs(start):
    visited[start] = 1

    for nxt in graph[start]:
        if not visited[nxt]:
            dfs(nxt)


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        num = queue.popleft()

        for nxt in graph[num]:
            if not visited[nxt]:
                queue.append(nxt)
                visited[nxt] = 1


V = int(input())
E = int(input())

graph = [[] for _ in range(V + 1)]
visited = [0 for _ in range(V + 1)]

for _ in range(E):  # 양방향. 인접리스트
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

# dfs(1)
bfs(1)

print(sum(visited) - 1)  # 1번 컴퓨터는 제외해야 하므로 -1
