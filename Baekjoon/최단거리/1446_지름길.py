N, D = map(int, input().split())
dist = list(range(D + 1))
short_path = {}

for _ in range(N):
    s, e, d = map(int, input().split())
    if short_path.get(s):
        short_path[s].append([e, d])
    else:
        short_path[s] = [[e, d]]

for s in range(D + 1):
    if s > 0:
        dist[s] = min(dist[s], dist[s - 1] + 1)
    if short_path.get(s):  # 먼저 해당 s의 거리를 최소값으로 맞추고 e 거리 할당해야 맞음
        for e, d in short_path[s]:
            if e > D:
                continue
            dist[e] = min(dist[e], dist[s] + d)

print(dist[D])
