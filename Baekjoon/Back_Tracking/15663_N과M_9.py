def make(k, lst):
    if k == M:
        print(*lst)
        return

    temp = place_chk[k]
    for i in range(N):
        if not place_chk[k] & (1 << nums[i]) and not idx_chk[i]:
            lst.append(nums[i])
            idx_chk[i] = 1
            place_chk[k] |= 1 << nums[i]
            make(k + 1, lst)
            idx_chk[i] = 0
            lst.pop()
    place_chk[k] = temp


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
idx_chk = [0] * N
place_chk = [0] * M
make(0, [])
