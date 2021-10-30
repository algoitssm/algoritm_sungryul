def floyd():
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i == j:
                    dist[i][j] = 0
                elif i != k and j != k:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


N, M = map(int, input().split())

dist = [[5001] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    dist[A][B] = 1
    dist[B][A] = 1

floyd()

max_val = 5001 * N
ans = 0

for r in range(1, N + 1):
    temp = 0
    for c in range(1, N + 1):
        if dist[r][c] != 5001:
            temp += dist[r][c]
    if temp < max_val:
        max_val = temp
        ans = r

print(ans)
