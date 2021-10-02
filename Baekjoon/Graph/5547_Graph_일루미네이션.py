from collections import deque


def change_zero(start):
    queue = deque()
    queue.append(start)

    while queue:
        cur_row, cur_col = queue.popleft()

        for i in range(6):
            if cur_row % 2:
                nxt_row = cur_row + dr_odd[i]
                nxt_col = cur_col + dc_odd[i]
            else:
                nxt_row = cur_row + dr_even[i]
                nxt_col = cur_col + dc_even[i]

            if 0 <= nxt_row < H + 2 and 0 <= nxt_col < W + 2:
                if data[nxt_row][nxt_col] == 0:
                    data[nxt_row][nxt_col] = -1
                    queue.append((nxt_row, nxt_col))


def cnt(start):
    global ans
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1

    while queue:
        cur_row, cur_col = queue.popleft()
        for i in range(6):
            if cur_row % 2:
                nxt_row = cur_row + dr_odd[i]
                nxt_col = cur_col + dc_odd[i]
            else:
                nxt_row = cur_row + dr_even[i]
                nxt_col = cur_col + dc_even[i]

            if 0 <= nxt_row < H + 2 and 0 <= nxt_col < W + 2:
                if data[nxt_row][nxt_col] == -1:
                    ans += 1
                elif data[nxt_row][nxt_col] == 1 and not visited[nxt_row][nxt_col]:
                    queue.append((nxt_row, nxt_col))
                    visited[nxt_row][nxt_col] = 1


W, H = map(int, input().split())
data = [[-1 for _ in range(W + 2)]]

for _ in range(H):
    data.append([-1] + list(map(int, input().split())) + [-1])

data.append([-1 for _ in range(W + 2)])

dr_odd = [-1, -1, 0, 0, 1, 1]
dc_odd = [0, 1, 1, -1, 0, 1]
dr_even = [-1, -1, 0, 0, 1, 1]
dc_even = [-1, 0, 1, -1, -1, 0]

visited_minus = [[0 for _ in range(W + 2)] for _ in range(H + 2)]
for row in range(H + 2):
    for col in range(W + 2):
        if data[row][col] == -1:
            change_zero((row, col))

visited = [[0 for _ in range(W + 2)] for _ in range(H + 2)]
ans = 0

for row in range(1, H + 1):
    for col in range(1, W + 1):
        if data[row][col] == 1 and not visited[row][col]:
            cnt((row, col))

print(ans)
