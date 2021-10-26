import sys

sys.stdin = open("input.txt")

T = int(input())

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

change_d = {
    (0, "3"): 2,  # 상 3 만났을 때 -> 좌
    (0, "2"): 3,  # 상 2 만났을 때 -> 우
    (1, "4"): 2,  # 하 4 만났을 때 -> 좌
    (1, "1"): 3,  # 하 1 만났을 때 -> 우
    (2, "2"): 1,  # 좌 2 만났을 때 -> 하
    (2, "1"): 0,  # 좌 1 만났을 때 -> 상
    (3, "3"): 1,  # 우 3 만났을 때 -> 하
    (3, "4"): 0,  # 우 4 만났을 때 -> 상
}


def move(r, c, d):  # 초기 위치, 방향
    global ans
    cnt = 0
    cur_r, cur_c, cur_d = r, c, d

    while True:
        nxt_r = cur_r + dr[cur_d]
        nxt_c = cur_c + dc[cur_d]

        # 벽에 부딪힌 경우
        if nxt_r < 0 or nxt_r >= N or nxt_c < 0 or nxt_c >= N:
            if cur_d & 1:  # 현재 방향 하, 우
                cur_d -= 1
            else:  # 현재 방향 상, 좌
                cur_d += 1
            cnt += 1
        # 범위 내인 경우
        else:
            # 블랙홀 빠지거나 출발 위치로 돌아온 경우
            if mp[nxt_r][nxt_c] == "-1" or (nxt_r, nxt_c) == (r, c):
                if cnt > ans:
                    ans = cnt
                break
            # 웜홀 만난 경우
            if mp[nxt_r][nxt_c] in ("6", "7", "8", "9", "10"):
                for row, col in worm[mp[nxt_r][nxt_c]]:
                    if (row, col) != (nxt_r, nxt_c):
                        nxt_r, nxt_c = row, col
                        break
            # 블록 만난 경우
            elif mp[nxt_r][nxt_c] in ("1", "2", "3", "4", "5"):
                # 90도 회전해야 하는 경우
                try:
                    cur_d = change_d[(cur_d, mp[nxt_r][nxt_c])]
                # 180도 회전해야 하는 경우
                except:
                    if cur_d & 1:  # 현재 방향 하, 우
                        cur_d -= 1
                    else:  # 현재 방향 상, 좌
                        cur_d += 1
                cnt += 1

        cur_r, cur_c = nxt_r, nxt_c


for tc in range(1, T + 1):
    # 정사각형 한 변 길이
    N = int(input())

    mp = []
    starts = []
    worm = {}
    for r in range(N):
        data = input().split()
        mp.append(data)
        for c in range(N):
            if data[c] == "0":
                starts.append((r, c))
            elif data[c] in ("6", "7", "8", "9", "10"):
                if worm.get(data[c]):
                    worm[data[c]].append((r, c))
                else:
                    worm[data[c]] = [(r, c)]

    ans = 0
    for r, c in starts:
        for d in range(4):
            move(r, c, d)

    print("#{} {}".format(tc, ans))
