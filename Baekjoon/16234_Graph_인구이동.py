# N x N, 인구수 차이 L 이상 R 이하일 때 이동
# Pypy3 로 했을 때는 통과, Python3로 했을 때는 80%에서 시간초과

N, L, R = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]


def dfs(start):
    global cnt
    global total
    stack = [start]
    visited[start[0]][start[1]] = 1

    while stack:
        cur = stack.pop()
        cnt += 1
        total += data[cur[0]][cur[1]]
        cur_visited.append((cur[0], cur[1]))

        for i in range(4):
            nxt_row = cur[0] + dr[i]
            nxt_col = cur[1] + dc[i]
            if (
                0 <= nxt_row < N
                and 0 <= nxt_col < N
                and L <= abs(data[cur[0]][cur[1]] - data[nxt_row][nxt_col]) <= R
                and not visited[nxt_row][nxt_col]
            ):
                stack.append((nxt_row, nxt_col))
                visited[nxt_row][nxt_col] = 1


dc = [1, -1, 0, 0]
dr = [0, 0, 1, -1]

ans = 0

# while True:
while True:
    visited = [[0] * N for _ in range(N)]
    changed = 0

    for row in range(N):
        for col in range(N):
            if visited[row][col]:
                continue
            cnt = 0
            total = 0
            cur_visited = []
            dfs((row, col))

            if cnt > 1:
                for cur_visit in cur_visited:
                    data[cur_visit[0]][cur_visit[1]] = total // cnt
                changed = 1

    if not changed:
        break
    ans += 1

print(ans)
