def combi(chk, k, c):
    if k == M:
        print(*c)
        return

    for i in range(k + 1, N + 1):
        if not chk & (1 << i):
            temp = chk
            chk = chk | (1 << i)
            c.append(i)
            combi(chk, k + 1, c)
            c.pop()


N, M = map(int, input().split())
combi(0, 0, [])
