from collections import deque
import sys

sys.stdin = open("input.txt")

T = int(input())


def go_down(stair, K):  # stair:선택된 계단, K:해당 계단 내려가는 데 필요한 시간
    result = 0
    cnt = 0
    for i in range(len(stair)):
        if stair[i]:
            cnt += len(stair[i])  # 해당 계단 선택한 사람 수

    in_stair = deque()  # 계단 내려가는 사람
    waiting = deque()  # 3명 차서 기다려야 하는 사람
    while cnt:  # 내려가는 사람 생길 때마다 -1 해서 0 되면 종료
        # 먼저 계단 내려가는 사람 계산
        for i in range(len(in_stair)):  # 1분 경과할 때마다 계단 내려가는 사람 소요시간 -1
            in_stair[i] -= 1
        while True:
            if not in_stair or in_stair[0] != 0:  # 계단에 사람이 없거나 가장 먼저 들어온 사람이 아직 다 내려가지 않은 경우
                break  # 빼줄 필요 없으므로 종료
            in_stair.popleft()  # 가장 먼저 들어온 사람이 0이 되면 다 내려갔으므로 in_stair에서 제거
            cnt -= 1
            if waiting:  # 기다리는 사람 있으면 계단 가장 뒤로 append
                in_stair.append(waiting.popleft())

        # 새로 계단에 들어올 사람 계산
        if result < len(stair) and stair[result]:  # 계단 입구 도착하는 사람 있으면
            for _ in range(len(stair[result])):
                if len(in_stair) < 3:  # 계단에 3명 미만이면
                    in_stair.append(K)  # 바로 append
                else:
                    waiting.append(K)  # 아니면 waiting

        result += 1

    return result


def to_stair(start):  # start:사람 인덱스 위치
    global ans
    if start == people_cnt:  # 모든 사람 계단 선택 완료하면
        result = max(
            go_down(stair_1, stairs[0][2]), go_down(stair_2, stairs[1][2])
        )  # 1, 2 계단 중 소요시간 큰 값을 result
        if result < ans:
            ans = result
        return
    else:  # 계단 선택할 사람 남아있으면
        stair_1_row, stair_1_col, K_1 = stairs[0]
        stair_2_row, stair_2_col, K_2 = stairs[1]
        cur_row, cur_col = people[start]  # 현재 계단 선택할 사람 위치
        to_stair_1 = abs(cur_row - stair_1_row) + abs(cur_col - stair_1_col)  # 1 계단까지 거리
        to_stair_2 = abs(cur_row - stair_2_row) + abs(cur_col - stair_2_col)  # 2 계단까지 거리

        # 1, 2 계단 선택하는 경우 모두 계산
        stair_1[to_stair_1].append(start)
        to_stair(start + 1)
        stair_1[to_stair_1].pop()
        stair_2[to_stair_2].append(start)
        to_stair(start + 1)
        stair_2[to_stair_2].pop()


for tc in range(1, T + 1):
    N = int(input())
    total_map = []
    stairs = []
    people = []
    people_cnt = 0

    for row in range(N):
        data = list(map(int, input().split()))
        for col in range(N):
            if data[col] == 0:
                continue
            elif data[col] == 1:
                people.append((row, col))
                people_cnt += 1
            else:
                stairs.append((row, col, data[col]))

    # 각 계단에 도착하는 시간을 인덱스로 해서 저장
    stair_1 = [[] for _ in range(2 * N)]
    stair_2 = [[] for _ in range(2 * N)]

    ans = 100

    to_stair(0)

    print("#{} {}".format(tc, ans))
