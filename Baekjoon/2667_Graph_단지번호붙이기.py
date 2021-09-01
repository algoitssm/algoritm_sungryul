import sys


def dfs(start):
    stack = [start]
    start_row, start_col = start
    visited[start_row][start_col] = cnt
    cnt_each[cnt] = 1  # start는 새로운 단지의 시작이므로 딕셔너리에 cnt 키로 value는 1로 설정

    while stack:
        cur_row, cur_col = stack.pop()
        for i in range(4):
            nxt_row = cur_row + dr[i]
            nxt_col = cur_col + dc[i]
            if 0 <= nxt_row < N and 0 <= nxt_col < N:  # 범위 내인지 여부 판단
                if (
                    data[nxt_row][nxt_col] and not visited[nxt_row][nxt_col]
                ):  # data에서 좌표값 0이 아니고, 방문하지 않은 경우
                    visited[nxt_row][nxt_col] = cnt  # visited를 문제에서 지도와 같이 만들어줌
                    cnt_each[cnt] += 1  # 딕셔너리에서 해당 cnt의 값 1 증가. 키는 위에서 만들어주기 때문에 무조건 있음
                    stack.append([nxt_row, nxt_col])


N = int(sys.stdin.readline())

data = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

cnt = 0  # 단지 개수
cnt_each = dict()  # 각 cnt에 해당하는 좌표 개수 저장하기 위한 딕셔너리


for row in range(N):
    for col in range(N):
        if data[row][col] and not visited[row][col]:  # data에서 0이 아니면서 방문하지 않은 새로운 시작점 탐색
            cnt += 1
            dfs([row, col])


print(cnt)
ans = list(cnt_each.values())
ans.sort()
for val in ans:
    print(val)
