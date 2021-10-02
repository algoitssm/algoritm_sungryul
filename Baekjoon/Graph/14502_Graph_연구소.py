from copy import deepcopy
from itertools import combinations


def dfs(start):
    # start 위치는 무조건 2

    stack = []
    stack.append(start)
    ans = 0

    while stack:
        cur = stack.pop()
        visited[cur[0]][cur[1]] = 1
        ans += 1

        for i in range(4):
            nxt_row = cur[0] + dr[i]
            nxt_col = cur[1] + dc[i]
            if (
                0 <= nxt_row < N
                and 0 <= nxt_col < M
                and not visited[nxt_row][nxt_col]
                and new_data[nxt_row][nxt_col] == 0
            ):
                stack.append((nxt_row, nxt_col))
                visited[nxt_row][nxt_col] = 1

    return ans


N, M = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
virus = []  # 바이러스 위치
candi_wall = []  # 벽을 세울 수 있는 위치
wall = 0  # 기존 설치 벽 개수

# 바이러스 위치와 벽을 세울 수 있는 위치 모두 탐색
for row in range(N):
    for col in range(M):
        if data[row][col] == 0:  # 바이러스와 인접한 곳에만 벽을 세우는 것 아니므로 모든 0에 대해 탐색
            candi_wall.append((row, col))
        elif data[row][col] == 2:
            virus.append((row, col))
        else:
            wall += 1

# 벽을 세울 수 있는 위치 경우의 수
combi_wall = combinations(candi_wall, 3)

ans = N * M  # 바이러스 옮기는 최대 수

for combi in combi_wall:
    new_data = deepcopy(data)
    for new_wall in combi:  # 새로운 벽을 세워줌
        new_data[new_wall[0]][new_wall[1]] = 1
    temp = 0  # 새로운 맵 기준으로 2의 개수를 세줌

    visited = [[0] * M for _ in range(N)]  # visited는 combi끼리 공유해야 start 위치를 중복해서 계산 X
    for start in virus:  # 2가 있는 곳마다 2가 전염되는 개수 계산
        temp += dfs(start)

    if temp < ans:
        ans = temp  # 바이러스 옮기는 수를 최소로 갱신

wall += 3  # 기존 벽에서 3개 추가
ans = N * M - wall - ans

print(ans)
