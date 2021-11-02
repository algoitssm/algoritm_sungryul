def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    dist[i][j] = 0
                elif i != k and j != k:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


n, m, r = map(int, input().split())
INF = 15 * n

items = list(map(int, input().split()))

dist = [[INF] * n for _ in range(n)]

for _ in range(r):
    a, b, l = map(int, input().split())
    dist[a - 1][b - 1] = l
    dist[b - 1][a - 1] = l

floyd()

ans = 0
for r in range(n):
    temp = 0
    for c in range(n):
        if dist[r][c] <= m:
            temp += items[c]
    if ans < temp:
        ans = temp

print(ans)
