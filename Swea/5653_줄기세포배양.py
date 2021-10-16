from collections import deque
import sys

sys.stdin = open("input.txt")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    data = deque()
    for _ in range(N):
        q = deque()
        temp = list(map(int, input().split()))
        for num in temp:
            q.append([num, 0, 0])   # 생명력, 상태(0: 비활성 1:활성 2:죽음), 지속 시간 카운트
        data.append(q)


    for t in range(1, K+1):
        active = []

        for row in range(len(data)):
            for col in range(len(data[row])):
                if data
