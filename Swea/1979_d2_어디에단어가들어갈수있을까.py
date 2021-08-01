T = int(input())

for i in range(1, T+1):
    N, K = map(int, input().split())
    total_map = []
    for j in range(N):
        total_map.append(list(map(int, input().split())))

    ans = 0
    # 가로 방향
    for k in range(N):
        cnt = 0
        for l in range(N):
            if total_map[k][l] == 1:
                cnt += 1
            if total_map[k][l] == 0 or l == N-1:
                if cnt == K:
                    ans += 1
                cnt = 0
    # 세로 방향
    for l in range(N):
        cnt = 0
        for k in range(N):
            if total_map[k][l] == 1:
                cnt += 1
            if total_map[k][l] == 0 or k == N-1:
                if cnt == K:
                    ans += 1
                cnt = 0

    print(f'#{i} {ans}')