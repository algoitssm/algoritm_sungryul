from collections import deque


def install():  # 짝수 초에는 현재 O인 곳을 start로 만들어줌
    temp = []
    for row in range(R):
        for col in range(C):
            if data[row][col] == "O":
                temp.append((row, col))
            else:
                data[row][col] = "O"
    return temp


def bomb(start):  # 홀수 초에는 폭탄을 터뜨림
    queue = deque()
    for s in start:
        queue.append(s)

    while queue:
        cur_row, cur_col = queue.popleft()
        data[cur_row][cur_col] = "."

        for i in range(4):
            nxt_row = cur_row + dr[i]
            nxt_col = cur_col + dc[i]
            if 0 <= nxt_row < R and 0 <= nxt_col < C:
                if data[nxt_row][nxt_col] != ".":  # 3초 경과 폭탄은 start에 모두 담겨있으므로 다시 큐에 append하지 않아도 됨
                    data[nxt_row][nxt_col] = "."


R, C, N = map(int, input().split())
data = [list(input()) for _ in range(R)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

if N < 2:  # 0~1초는 그대로 출력
    for d in data:
        print("".join(d))
else:
    sec = 2
    while sec <= N:
        if sec % 2:
            bomb(start)
        else:
            start = install()
        sec += 1

    for d in data:
        print("".join(d))
