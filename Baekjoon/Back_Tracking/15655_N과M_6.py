def make(k, chk, c):
    if k == M:
        print(*c)
        return
    for i in range(k, N):
        if not chk & (1 << i):
            chk |= 1 << i
            c.append(nums[i])
            make(k + 1, chk, c)
            c.pop()


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
make(0, 0, [])
