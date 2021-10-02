import sys

N, M = map(int, sys.stdin.readline().split())

cur_r, cur_c, cur_d = map(int, sys.stdin.readline().split())

area = []

for _ in range(N):
    area.append(list(map(int, sys.stdin.readline().split())))

# 문제에서 처음 주어진 방향 숫자에 맞게 인덱스 넣기!
move = ((-1, 0), (0, 1), (1, 0), (0, -1))
ans = 1
cnt = 0
cleared = [(cur_r, cur_c)]

while True:
    cur_d -= 1
    if cur_d < 0:
        cur_d = 3

    nxt_r = cur_r + move[cur_d][0]
    nxt_c = cur_c + move[cur_d][1]

    if area[nxt_r][nxt_c] == 0 and (nxt_r, nxt_c) not in cleared:
        ans += 1
        cur_r, cur_c = nxt_r, nxt_c
        cnt = 0
        cleared.append((cur_r, cur_c))
        continue
    else:
        cnt += 1

    if cnt == 4:
        nxt_r = cur_r - move[cur_d][0]
        nxt_c = cur_c - move[cur_d][1]
        if area[nxt_r][nxt_c] == 0:
            cur_r, cur_c = nxt_r, nxt_c
            cnt = 0
        else:
            break
        
print(ans)            