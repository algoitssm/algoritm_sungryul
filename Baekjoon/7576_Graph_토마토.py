import sys
from collections import deque


def bfs(start):  # 모든 시작점을 큐에 넣고 진행해야 한 번에 날짜 계산 가능
    global zero_cnt, max_day
    que = deque()
    for s in start:
        que.append(s)  # 모든 시작점을 큐에 넣음
        visited[s[0]][s[1]] = 1  # 해당 시작점의 visited를 1로 설정

    while que:
        cur_row, cur_col = que.popleft()
        temp = 0
        for i in range(4):
            nxt_row = cur_row + dr[i]
            nxt_col = cur_col + dc[i]

            if 0 <= nxt_row < N and 0 <= nxt_col < M:
                if data[nxt_row][nxt_col] == 0 and not visited[nxt_row][nxt_col]:
                    visited[nxt_row][nxt_col] = (
                        visited[cur_row][cur_col] + 1
                    )  # visited를 이전 좌표에서 1 증가
                    zero_cnt -= 1  # 0은 하나 없어지므로 zero_cnt 1 감소
                    que.append((nxt_row, nxt_col))

                    if max_day < visited[nxt_row][nxt_col]:  # visited가 max_day보다 크면 갱신
                        max_day = visited[nxt_row][nxt_col]


M, N = map(int, sys.stdin.readline().split())

data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

zero_cnt = 0
start = []
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for row in range(N):
    for col in range(M):
        if data[row][col] == 0:  # 초기 0인 곳 개수
            zero_cnt += 1
        elif data[row][col] == 1:  # 시작점 리스트에 저장
            start.append((row, col))

visited = [[0] * M for _ in range(N)]
max_day = 0

bfs(start)  # 모든 시작점을 인자로 넘겨 bfs

if zero_cnt:  # 초기 0이었던 곳 남아있으면 -1
    print(-1)
else:
    if max_day:  # max_day가 증가했다면 시작점이 1부터 시작하므로 -1
        print(max_day - 1)
    else:  # max_day가 0이라면 변한 곳 없으므로 그대로 0
        print(max_day)
