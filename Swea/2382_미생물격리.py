import sys

sys.stdin = open("input.txt")

T = int(input())

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # N:한 변의 셀의 개수  M:격리 시간  K:미생물 군집 개수
    microbes = []
    total_map = [[0] * N for _ in range(N)]

    for _ in range(K):
        r, c, n, d = map(int, input().split())  # 미생물 row, col, 현재 개수, 방향
        total_map[r][c] = [n, n, d]  # 기준값(더 큰 값 만나는 경우 변경), 누적 합계, 방향
        microbes.append((r, c))  # 미생물 위치

    for _ in range(M):
        new_microbes = set()  # 이동한 뒤 미생물 위치 좌표. 좌표 중복 방지 위해 set 사용
        new_map = [[0] * N for _ in range(N)]

        for cur_r, cur_c in microbes:  # 미생물의 위치를 하나씩 꺼내면서
            max_n, total_n, d = total_map[cur_r][cur_c]
            # 다음 좌표
            nxt_r = cur_r + dr[d]
            nxt_c = cur_c + dc[d]

            if nxt_r == 0 or nxt_r == N - 1 or nxt_c == 0 or nxt_c == N - 1:  # 약품 도달한 경우
                total_n //= 2  # 개수 반으로 줄이고
                if d & 1:  # 1, 3 방향은 2, 4로
                    d += 1
                else:  # 2, 4 방향은 1, 3으로 변경
                    d -= 1

            if total_n == 0:  # 현재 미생물 수 0인 경우 해당 군집 더이상 진행 못하므로 continue
                continue

            max_n = total_n  # 이동하고 나서 max_n 필요하고, 그 전에는 total_n과 같은 값

            new_microbes.add((nxt_r, nxt_c))

            if new_map[nxt_r][nxt_c]:  # 이미 다음 좌표 방문한 군집 있는 경우
                if max_n > new_map[nxt_r][nxt_c][0]:  # 해당 좌표 방문했던 최대값과 현재 미생물 수 비교
                    # 더 크면 갱신
                    new_map[nxt_r][nxt_c][0] = max_n
                    new_map[nxt_r][nxt_c][2] = d
                # 기존 미생물 수에 현재 방문한 개수 더해줌
                new_map[nxt_r][nxt_c][1] += total_n
            else:  # 방문한 군집 없는 경우에는 현재 미생물 값 넣어줌
                new_map[nxt_r][nxt_c] = [max_n, total_n, d]

        microbes = list(new_microbes)[:]
        total_map = [row[:] for row in new_map]

    ans = 0

    for row in range(N):
        for col in range(N):
            if total_map[row][col]:
                ans += total_map[row][col][1]

    print("#{} {}".format(tc, ans))
