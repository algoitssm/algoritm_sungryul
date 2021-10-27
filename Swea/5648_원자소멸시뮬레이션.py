"""
처음에 큐에 넣고 했으나 메모리를 너무 많이 쓰고 시간도 오래 걸려서
딕셔너리로 처리했는데 시간은 절반 가까이 줄었으나 메모리 문제 여전
"""

from collections import deque
import sys

sys.stdin = open("input.txt")

dy = [0.5, -0.5, 0, 0]
dx = [0, 0, -0.5, 0.5]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # q = deque()
    # d_K = {}
    mp = {}

    for _ in range(N):
        x, y, d, K = map(int, input().split())
        # q.append((x, y))
        # d_K[(x, y)] = [[d, K]]

        # 좌표 값을 딕셔너리의 키로 방향과 값을 밸류로
        mp[(x, y)] = [[d, K]]

    ans = 0
    while True:
        # new_d_K = {}
        # new_q = set()
        # while q:
        #     # cur_x, cur_y = q.popleft()
        #     # cur_d, cur_K = d_K[(cur_x, cur_y)][0]

        #     nxt_x = cur_x + dx[cur_d]
        #     nxt_y = cur_y + dy[cur_d]

        #     if -1000 <= nxt_x <= 1000 and -1000 <= nxt_y <= 1000:
        #         if new_d_K.get((nxt_x, nxt_y)):
        #             new_d_K[(nxt_x, nxt_y)].append([cur_d, cur_K])
        #             collision.add((nxt_x, nxt_y))
        #         else:
        #             new_d_K[(nxt_x, nxt_y)] = [[cur_d, cur_K]]
        #             new_q.add((nxt_x, nxt_y))
        # new_q -= collision

        # if not new_q:
        #     break

        # q = deque(new_q)
        # d_K = new_d_K

        new_mp = {}  # 원자 이동 후 새로운 위치에 저장할 맵
        collision = set()  # 충돌한 위치 저장할 set

        for key, val in mp.items():
            cur_x, cur_y = key
            cur_d, cur_K = val[0]

            nxt_x = cur_x + dx[cur_d]
            nxt_y = cur_y + dy[cur_d]
            if -1000 <= nxt_x <= 1000 and -1000 <= nxt_y <= 1000:  # 범위 벗어나는 경우 충돌 가능성 X
                if new_mp.get((nxt_x, nxt_y)):  # 충돌한 경우
                    new_mp[(nxt_x, nxt_y)].append([cur_d, cur_K])
                    collision.add((nxt_x, nxt_y))
                else:  # 충돌하지 않은 경우
                    new_mp[(nxt_x, nxt_y)] = [[cur_d, cur_K]]

        for r, c in collision:
            targets = new_mp.pop((r, c))  # 딕셔너리에서 해당 좌표 키 값 삭제하고
            for target in targets:
                ans += target[1]  # ans에 K 값 더해줌

        if not new_mp:  # 딕셔너리 비어있으면 중단
            break

        mp = new_mp  # mp를 새로운 mp로 갱신

    print("#{} {}".format(tc, ans))
