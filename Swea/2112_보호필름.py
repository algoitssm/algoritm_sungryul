from copy import deepcopy
from itertools import combinations
from collections import deque
import sys

sys.stdin = open("input.txt")

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
        return col
    return -1


for tc in range(1, T + 1):
    D, W, K = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(D)]

    first_chk = chk(data)
