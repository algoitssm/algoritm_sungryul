T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    area = []
    for j in range(N):
        area.append(list(map(int, input().split())))

    max_val = 0
    for k in range(N - M + 1):
        for l in range(N - M + 1):
            total = 0
            for m in range(M):
                total += sum(area[k+m][l:l+M])
            if max_val < total:
                max_val = total

    print(f'#{i+1} {max_val}')