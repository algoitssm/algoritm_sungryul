def floyd():
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i == j:
                    dist[i][j] = 0
                elif i != k and j != k:
                    dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])


def chk():
    result = ["Small World!", "Big World!"]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dist[i][j] > 6:
                return result[1]
    return result[0]


N, K = map(int, input().split())
G = [[] for _ in range(N + 1)]
dist = [[100] * (N + 1) for _ in range(N + 1)]

for _ in range(K):
    A, B = map(int, input().split())
    dist[A][B] = 1
    dist[B][A] = 1

floyd()

print(chk())
