import sys
from itertools import combinations

sys.stdin = open("input.txt")

T = int(input())


def calc(row, col):
    target = honey[row][col : col + M]
    max_val = 0

    for i in range(1, M + 1):
        combis = combinations(target, i)
        for combi in combis:
            temp = 0
            if sum(combi) <= C:
                for num in combi:
                    temp += num ** 2
            if temp > max_val:
                max_val = temp

    return max_val


for tc in range(1, T + 1):
    N, M, C = map(int, input().split())

    honey = [list(map(int, input().split())) for _ in range(N)]

    total = [[0] * (N - M + 1) for _ in range(N)]

    max_start = []
    max_val = 0

    for row in range(N):
        for col in range(N - M + 1):
            total[row][col] = calc(row, col)
            if total[row][col] > max_val:
                max_val = total[row][col]
                max_start = [(row, col)]
            elif total[row][col] == max_val:
                max_start.append((row, col))

    ans = 0

    for start in max_start:
        banned = []
        for i in range(-M + 1, M):
            banned.append((start[0], start[1] + i))

        second_max = 0
        for row in range(N):
            for col in range(N - M + 1):
                if total[row][col] > second_max and (row, col) not in banned:
                    second_max = total[row][col]

        temp = total[start[0]][start[1]] + second_max
        if ans < temp:
            ans = temp

    print("#{} {}".format(tc, ans))
