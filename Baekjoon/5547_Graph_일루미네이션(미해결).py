from collections import deque


def change_zero(start):
    queue = deque()
    queue.append(start)
    visited_for_zero[start[0]][start[1]] = 1
    sign = False
    temp = []

    while queue:
        cur_row, cur_col = queue.popleft()
        temp.append((cur_row, cur_col))

        for i in range(6):
            if cur_row % 2:
                nxt_row = cur_row + dr_odd[i]
                nxt_col = cur_col + dc_odd[i]
            else:
                nxt_row = cur_row + dr_even[i]
                nxt_col = cur_col + dc_even[i]

            if 0 <= nxt_row < H and 0 <= nxt_col < W:
                if not visited_for_zero[nxt_row][nxt_col] and not data[nxt_row][nxt_col]:
                    queue.append((nxt_row, nxt_col))
                    visited_for_zero[nxt_row][nxt_col] = 1
            else:
                sign = True
        if sign:
            break
    else:
        for tp in temp:
            data[tp[0]][tp[1]] = 1


def cnt(start):
    global ans
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1

    while queue:
        cur_row, cur_col = queue.popleft()
        temp = 6
        for i in range(6):
            if cur_row % 2:
                nxt_row = cur_row + dr_odd[i]
                nxt_col = cur_col + dc_odd[i]
            else:
                nxt_row = cur_row + dr_even[i]
                nxt_col = cur_col + dc_even[i]

            if 0 <= nxt_row < H and 0 <= nxt_col < W:
                if data[nxt_row][nxt_col]:
                    temp -= 1
                    if not visited[nxt_row][nxt_col]:
                        queue.append((nxt_row, nxt_col))
                        visited[nxt_row][nxt_col] = 1
        ans += temp


W, H = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(H)]

dr_even = [-1, -1, 0, 0, 1, 1]
dc_even = [0, 1, 1, -1, 0, 1]
dr_odd = [-1, -1, 0, 0, 1, 1]
dc_odd = [-1, 0, 1, -1, -1, 0]

visited_for_zero = [[0 for _ in range(W)] for _ in range(H)]
for row in range(H):
    for col in range(W):
        if not data[row][col] and not visited_for_zero[row][col]:
            change_zero((row, col))

visited = [[0 for _ in range(W)] for _ in range(H)]
ans = 0

for row in range(H):
    for col in range(W):
        if data[row][col] and not visited[row][col]:
            cnt((row, col))

print(ans)
