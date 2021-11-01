def floyd():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    dist[i][j] = 0
                    ans[i][j] = "-"
                elif i != k and j != k:
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        ans[i][j] = ans[i][k]


n, m = map(int, input().split())

INF = 1001 * n
dist = [[INF] * (n + 1) for _ in range(n + 1)]
ans = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    v1, v2, w = map(int, input().split())
    dist[v1][v2] = w
    dist[v2][v1] = w
    ans[v1][v2] = v2
    ans[v2][v1] = v1

floyd()

for i in range(1, n + 1):
    print(" ".join(list(map(str, ans[i][1:]))))
