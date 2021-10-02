"""
0: 빈 공간 / 1: 벽 / 2: 그람
도달하면 최단 시간 출력
도달 못 하면 Fail 출력
"""

import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline


def not_gram(start):
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] += 1
    if start[0] == N - 1 and start[1] == M - 1:
        return visited[start[0]][start[1]]
    gram = False

    while queue:
        cur_row, cur_col = queue.popleft()

        for i in range(4):
            nxt_row = cur_row + dr[i]
            nxt_col = cur_col + dc[i]

            if (
                0 <= nxt_row < N
                and 0 <= nxt_col < M
                and visited[nxt_row][nxt_col] == -1
                and data[nxt_row][nxt_col] != 1
            ):
                visited[nxt_row][nxt_col] = visited[cur_row][cur_col] + 1
                if data[nxt_row][nxt_col] == 2:
                    gram = visited[nxt_row][nxt_col] + abs(N - 1 - nxt_row) + abs(M - 1 - nxt_col)
                    ans.append(gram)
                elif data[nxt_row][nxt_col] == 0:
                    queue.append((nxt_row, nxt_col))
                    if nxt_row == N - 1 and nxt_col == M - 1:
                        ans.append(visited[nxt_row][nxt_col])


N, M, T = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

visited = [[-1 for _ in range(M)] for _ in range(N)]

ans = []
not_gram((0, 0))

if ans:
    if min(ans) <= T:
        print(min(ans))
    else:
        print("Fail")
else:
    print("Fail")
