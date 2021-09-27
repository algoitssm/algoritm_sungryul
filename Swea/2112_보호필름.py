from itertools import combinations
from collections import deque

T = int(input())


def chk(data):
    for col in range(W):
        cnt = 0
        checked = []
        for row in range(D):
            if not checked:
                checked.append(data[row][col])
                cnt += 1
            else:
                if checked[-1] == data[row][col]:
                    cnt += 1
                else:
                    checked = [data[row][col]]
                    cnt = 1
            if cnt == K:
                break
        if cnt == K:
            continue
        return False
    return True


for tc in range(1, T + 1):
    D, W, K = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(D)]

    first_chk = chk(data)

    if first_chk:
        print("#{} {}".format(tc, 0))
    else:
        is_pass = False
        for i in range(1, D + 1):
            target_rows = list(combinations(range(D), i))

            for rows in target_rows:
                queue = deque()
                cnt = 0
                queue.append(data)

                for j in range(i):
                    for _ in range(2 ** j):
                        cur_data = queue.popleft()
                        new_data_1 = [line[:] for line in cur_data]  # deepcopy로 접근하면 35/50 시간초과
                        new_data_1[rows[j]] = [0] * W
                        queue.append(new_data_1)
                        new_data_2 = [line[:] for line in cur_data]
                        new_data_2[rows[j]] = [1] * W
                        queue.append(new_data_2)

                for new_data in queue:
                    if chk(new_data):
                        is_pass = True
                        break
                if is_pass:
                    break
            if is_pass:
                print("#{} {}".format(tc, i))
                break
