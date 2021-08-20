from collections import deque

N = int(input())  # 노드 개수

parents = [0 for _ in range(N + 1)]


def dfs_recursion(start):  # Recursion Error
    visited_dfs[start] = 1

    for child in graph[start]:
        if not visited_dfs[child]:
            dfs(child)
            # 자식 노드에서 다시 부모 노드로 돌아올 때, 부모 노드 체크
            parents[child] = start


def dfs_stack(start):  # 시간 초과
    stack = [start]
    cnt = 1
    while stack:
        start = stack.pop()

        if not visited_dfs[start]:
            visited_dfs[start] = 1

            for child in graph[start]:
                if not visited_dfs[child]:
                    stack.append(child)
                    parents[child] = start
                    cnt += 1
                if cnt == N:
                    break
        if cnt == N:
            break


def bfs(start):  # 시간 초과 => break 추가 후 통과되지만 시간 오래 걸림(메모리: 51572KB, 시간: 4772ms)
    queue = deque()
    queue.append(start)
    visited_bfs[start] = 1
    cnt = 1

    while queue:
        parent = queue.popleft()

        for child in graph[parent]:
            if not visited_bfs[child]:
                queue.append(child)
                visited_bfs[child] = 1
                parents[child] = parent
                cnt += 1

            if cnt == N:
                break
        if cnt == N:
            break


graph = [[] for _ in range(N + 1)]
visited_dfs = [0 for _ in range(N + 1)]
visited_bfs = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

# dfs_recursion(1)
bfs(1)
# dfs_stack(1)
for parent in parents[2:]:
    print(parent)
