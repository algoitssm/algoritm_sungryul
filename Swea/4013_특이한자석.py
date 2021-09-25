T = int(input())


def clockwise(saw):
    saw = [saw.pop()] + saw
    return saw


def counterclockwise(saw):
    temp = saw.pop(0)
    saw += [temp]
    return saw


def work_left(num, cur_left, d):  # 입력 톱니 기준 왼쪽 톱니 회전
    if num < 0:
        return
    if saws[num][2] == cur_left:
        return

    cur_left = saws[num][6]
    if d == 1:  # 이전 톱니가 시계면 현재 톱니는 반시계
        saws[num] = counterclockwise(saws[num])
        work_left(num - 1, cur_left, -1)
    else:
        saws[num] = clockwise(saws[num])
        work_left(num - 1, cur_left, 1)


def work_right(num, cur_right, d):  # 입력 톱니 기준 오른쪽 톱니 회전
    if num > 3:
        return
    if saws[num][6] == cur_right:
        return

    cur_right = saws[num][2]
    if d == 1:  # 이전 톱니가 시계면 현재 톱니는 반시계
        saws[num] = counterclockwise(saws[num])
        work_right(num + 1, cur_right, -1)
    else:
        saws[num] = clockwise(saws[num])
        work_right(num + 1, cur_right, 1)


def cnt(saws):
    ans = 0
    for i in range(4):
        if saws[i][0]:
            ans += 2 ** i

    return ans


for tc in range(1, T + 1):
    K = int(input())
    saws = [list(map(int, input().split())) for _ in range(4)]

    for _ in range(K):
        num, d = map(int, input().split())
        num -= 1

        cur_left = saws[num][6]
        cur_right = saws[num][2]

        if d == 1:
            saws[num] = clockwise(saws[num])
        else:
            saws[num] = counterclockwise(saws[num])

        work_left(num - 1, cur_left, d)
        work_right(num + 1, cur_right, d)

    ans = cnt(saws)

    print("#{} {}".format(tc, ans))
