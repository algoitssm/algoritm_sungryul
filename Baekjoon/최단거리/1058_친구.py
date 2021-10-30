def floyd():
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k in range(N):
                if i != k and j != k:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[j][k])
            if dist[i][j] and dist[i][j] < 3:
                ans[i] += 1


N = int(input())

dist = [[51] * N for _ in range(N)]
ans = [0] * N

for r in range(N):
    data = list(input())
    for c in range(N):
        if r == c:
            dist[r][c] = 0
        else:
            if data[c] == "Y":
                dist[r][c] = 1

floyd()
print(max(ans))
