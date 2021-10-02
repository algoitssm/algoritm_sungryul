from collections import deque

N, M, V = map(int, input().split())


def dfs(start):
    visited_dfs[start] = 1
    print(start, end=" ")
    for nxt in graph[start]:
        if not visited_dfs[nxt]:
            dfs(nxt)


def bfs(start):
    queue = deque()
    queue.append(start)
    visited_bfs[start] = 1

    while queue:
        num = queue.popleft()
        print(num, end=" ")
        for nxt in graph[num]:
            if not visited_bfs[nxt]:
                queue.append(nxt)
                visited_bfs[nxt] = 1


graph = [[] for _ in range(N + 1)]
visited_dfs = [0 for _ in range(N + 1)]
visited_bfs = [0 for _ in range(N + 1)]

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for node in graph:  # 정렬해줘야 결과가 똑같이 나옴
    node.sort()

dfs(V)
print()
bfs(V)
