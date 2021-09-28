import sys

sys.stdin = open("input.txt")

T = int(input())


def row_chk(data, row):
    global ans
    visited = [0] * N  # 겹치는 부분 확인
    temp = []

    for col in range(N):
        if not temp:
            temp.append(data[row][col])
        else:
            if temp[-1] == data[row][col]:
                continue
            else:
                if abs(temp[-1] - data[row][col]) != 1:
                    return
                if temp[-1] - data[row][col] == 1:  # 높이 1 낮아질 때
                    temp.append(data[row][col])  # 오른쪽 판단 이전에 append
                    visited[col] = 1
                    for i in range(1, X):
                        if col + i >= N or data[row][col + i] != temp[-1] or visited[col + i]:
                            return
                        visited[col + i] = 1
                elif temp[-1] - data[row][col] == -1:  # 높이 1 높아질 때
                    for i in range(1, X + 1):
                        if col - i < 0 or data[row][col - i] != temp[-1] or visited[col - i]:
                            return
                        visited[col - i] = 1
                    temp.append(data[row][col])  # 왼쪽 판단하고 append

    ans += 1  # 평지인 경우에도 포함. return 되지 않고 통과하면 ans += 1


for tc in range(1, T + 1):
    N, X = map(int, input().split())
    ans = 0

    data = [list(map(int, input().split())) for _ in range(N)]
    data_reverse = list(zip(*data))

    for row in range(N):
        row_chk(data, row)
        row_chk(data_reverse, row)

    print("#{} {}".format(tc, ans))
