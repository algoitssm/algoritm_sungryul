def perm(chk, k):
    if k == M:
        print(*p)
        return

    for i in range(1, N + 1):
        if not chk & (1 << i):
            temp = chk
            chk = chk | (1 << i)
            p[k] = i
            perm(chk, k + 1)
            chk = temp
            p[k] = 0


N, M = map(int, input().split())

visited = [0] * N
p = [0] * M

perm(0, 0)
