import sys
from collections import deque


def bfs(start):
    global not_ripe
    queue = deque()
    for s in start:
        queue.append(s)
        visited[s[0]][s[1]][s[2]] += 1

    while queue:
        cur_h, cur_row, cur_col = queue.popleft()

        for i in range(6):
            nxt_h = cur_h + dh[i]
            nxt_row = cur_row + dr[i]
            nxt_col = cur_col + dc[i]

            if 0 <= nxt_h < H and 0 <= nxt_row < N and 0 <= nxt_col < M:
                if data[nxt_h][nxt_row][nxt_col] == 0 and visited[nxt_h][nxt_row][nxt_col] == -1:
                    visited[nxt_h][nxt_row][nxt_col] = visited[cur_h][cur_row][cur_col] + 1
                    queue.append((nxt_h, nxt_row, nxt_col))
                    not_ripe -= 1

            if not not_ripe:
                return visited[nxt_h][nxt_row][nxt_col]
    return -1


M, N, H = map(int, sys.stdin.readline().split())

data = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

dr = [1, -1, 0, 0, 0, 0]
dc = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

start = []
not_ripe = 0

for height in range(H):
    for row in range(N):
        for col in range(M):
            if data[height][row][col] == 1:
                start.append((height, row, col))
            elif data[height][row][col] == 0:
                not_ripe += 1

visited = [[[-1] * M for _ in range(N)] for _ in range(H)]


if not not_ripe:
    print(0)
else:
    ans = bfs(start)
    print(ans)
