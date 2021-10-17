import sys

sys.stdin = open("input.txt")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    SIZE = max(N, M) + 2 * K

    status = [[0] * SIZE for _ in range(SIZE)]
    life = [[0] * SIZE for _ in range(SIZE)]
    start_r = SIZE // 2 - N
    start_c = SIZE // 2 - M

    for r in range(N):
        data = list(map(int, input().split()))
        for c in range(M):
            status[start_r + r][start_c + c] = data[c]
            life[start_r + r][start_c + c] = data[c]

    for _ in range(K):
        temp = {}
        for r in range(SIZE):
            for c in range(SIZE):
                if life[r][c] != 0:
                    if status[r][c] > 0:
                        status[r][c] -= 1
                    else:
                        if -status[r][c] > life[r][c]:
                            continue
                        else:
                            for d in range(4):
                                nxt_r = r + dr[d]
                                nxt_c = c + dc[d]

                                if life[nxt_r][nxt_c] == 0 and (nxt_r, nxt_c) not in temp:
                                    temp[(nxt_r, nxt_c)] = life[r][c]
                                elif (nxt_r, nxt_c) in temp:
                                    if temp[(nxt_r, nxt_c)] < life[r][c]:
                                        temp[(nxt_r, nxt_c)] = life[r][c]
                        status[r][c] -= 1

        for key, val in temp.items():
            r, c = key
            status[r][c] = val
            life[r][c] = val

    ans = 0

    for r in range(SIZE):
        for c in range(SIZE):
            if life[r][c] and -status[r][c] < life[r][c]:
                ans += 1

    print("#{} {}".format(tc, ans))
