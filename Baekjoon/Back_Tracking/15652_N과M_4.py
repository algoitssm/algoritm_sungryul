def make(k, p):
    if k == M:
        print(*p)
        return

    for i in range(1, N + 1):
        if not p or p[-1] <= i:
            p.append(i)
            make(k + 1, p)
            p.pop()


N, M = map(int, input().split())
make(0, [])
