def make(chk, k, p):
    if k == M:
        print(*p)
        return

    for i in range(N):
        if not chk & (1 << i):
            temp = chk
            chk |= 1 << i
            p.append(nums[i])
            make(chk, k + 1, p)
            chk = temp
            p.pop()


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

make(0, 0, [])
