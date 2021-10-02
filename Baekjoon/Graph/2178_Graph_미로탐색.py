from collections import deque

N, M = map(int, input().split())  # N x M 배열. (1, 1) 출발 (N, M) 도착 위치

# 최단 경로 찾는 문제라 bfs로 풀이
def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1  # visited는 좌표값으로 접근하기 위해 2차원 리스트로 구성

    while queue:
        cur_row, cur_col = queue.popleft()

        for i in range(4):
            nxt_row = cur_row + dr[i]
            nxt_col = cur_col + dc[i]

            if (
                0 <= nxt_row < N
                and 0 <= nxt_col < M
                and not visited[nxt_row][nxt_col]
                and data[nxt_row][nxt_col] == 1
            ):
                queue.append([nxt_row, nxt_col])
                visited[nxt_row][nxt_col] = visited[cur_row][cur_col] + 1
                if nxt_row == dest[0] and nxt_col == dest[1]:
                    return visited[nxt_row][nxt_col]


data = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
# 상하좌우로 이동하며 그래프에 넣어주기 위한 델타
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

start = (0, 0)  # 시작 좌표
dest = (N - 1, M - 1)  # 끝 좌표

print(bfs(start))
