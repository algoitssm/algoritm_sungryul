from collections import deque

T = int(input())


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        cur_x, cur_y = q.popleft()
        if abs(dest_x - cur_x) + abs(dest_y - cur_y) <= 1000:
            return 0

        for i in range(n):
            if not visited[i]:
                nxt_x, nxt_y = stores[i]
                if abs(nxt_x - cur_x) + abs(nxt_y - cur_y) <= 1000:
                    visited[i] = 1
                    q.append((nxt_x, nxt_y))
    else:
        return 1


result = ["happy", "sad"]

for _ in range(T):
    n = int(input())  # 편의점 개수

    s_x, s_y = map(int, input().split())

    stores = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n

    dest_x, dest_y = map(int, input().split())

    ans = bfs(s_x, s_y)

    print(result[ans])


"""
import sys

input = sys.stdin.readline
inf = sys.maxsize

t = int(input())
for _ in range(t):
    n = int(input())
    graph = []
    for _ in range(n + 2):
        graph.append(list(map(int, input().split())))
    dp = [[inf] * (n + 2) for _ in range(n + 2)]

    for i in range(n + 2):
        for j in range(n + 2):
            if i == j:
                continue
            if abs(graph[i][0] - graph[j][0]) + abs(graph[i][1] - graph[j][1]) <= 1000:
                dp[i][j] = 1
    
    for k in range(n + 2):
        for i in range(n + 2):
            for j in range(n + 2):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j] 
    
    print("happy" if 0 <= dp[0][n+1] < inf else "sad")
"""
