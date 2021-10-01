import sys
sys.stdin = open('input.txt')
T = int(input())


def change_map(col, row, C, P, num):  # map에 BC 정보 반영
    for i in range(-C, C + 1):
        for j in range(-C + abs(i), C - abs(i) + 1):
            if 0 <= row + i <= 10 and 0 <= col + j <= 10:
                if total_map[row + i][col + j]:
                    total_map[row + i][col + j].append((num, P))
                else:
                    total_map[row + i][col + j] = [(num, P)]


direction = {
    "0": (0, 0),
    "1": (-1, 0),
    "2": (0, 1),
    "3": (1, 0),
    "4": (0, -1),
}  # user 별 입력 정보 따라 길 이동 방향


for tc in range(1, T + 1):
    M, A = map(int, input().split())  # M: 이동시간  A: BC 개수
    user_A = input().split()
    user_B = input().split()

    total_map = [[0] * 11 for _ in range(11)]

    for idx in range(1, A + 1):
        col, row, C, P = map(int, input().split())
        change_map(col, row, C, P, idx)

    user_A_row, user_A_col = 1, 1
    user_B_row, user_B_col = 10, 10
    charge_A, charge_B = 0, 0

    for step in range(M + 1):
        cur_A = total_map[user_A_row][user_A_col]
        cur_B = total_map[user_B_row][user_B_col]
        if cur_A:
            cur_A.sort(reverse=True, key=lambda x: x[1])
        if cur_B:
            cur_B.sort(reverse=True, key=lambda x: x[1])

        if cur_A and cur_B:  # 둘 다 충전 가능한 경우
            if cur_A == cur_B:  # 둘의 BC 같은 경우
                if len(cur_A) == 1:  # 길이가 1인 경우
                    charge_A += cur_A[0][1] // 2
                    charge_B += cur_A[0][1] // 2
                else:  # 길이가 2 이상인 경우는 처음과 그 다음 꺼 각각 더해줌
                    charge_A += cur_A[0][1]
                    charge_B += cur_A[1][1]
            else:  # A, B BC 다른 경우
                if cur_A[0][0] != cur_B[0][0]:  # 가장 충전량 큰 BC 다른 경우
                    charge_A += cur_A[0][1]
                    charge_B += cur_B[0][1]
                else:  # 가장 충전량 큰 BC 같은 경우
                    if len(cur_A) > 1 and len(cur_B) > 1:  # 둘 다 속한 BC 2개 이상인 경우
                        if cur_A[1][1] >= cur_B[1][1]:  # 2번째로 큰 값 비교
                            charge_A += cur_A[1][1]
                            charge_B += cur_B[0][1]
                        else:
                            charge_A += cur_A[0][1]
                            charge_B += cur_B[1][1]
                    elif len(cur_A) > 1:  # A만 2개 이상인 경우
                        charge_B += cur_B[0][1]
                        charge_A += cur_A[1][1]
                    elif len(cur_B) > 1:  # B만 2개 이상인 경우
                        charge_A += cur_A[0][1]
                        charge_B += cur_B[1][1]

        elif cur_A:
            charge_A += cur_A[0][1]
        elif cur_B:
            charge_B += cur_B[0][1]

        if step != M:
            user_A_row += direction[user_A[step]][0]
            user_A_col += direction[user_A[step]][1]
            user_B_row += direction[user_B[step]][0]
            user_B_col += direction[user_B[step]][1]

    print("#{} {}".format(tc, charge_A + charge_B))
