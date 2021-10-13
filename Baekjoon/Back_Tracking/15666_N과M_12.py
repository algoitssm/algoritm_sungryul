def make(k, lst):
    if k == M:
        print(*lst)
        return

    for i in range(N):
        if not place_chk[k] & (1 << nums[i]):
            if not lst or lst[-1] <= nums[i]:
                lst.append(nums[i])
                place_chk[k] |= 1 << nums[i]
                make(k + 1, lst)
                lst.pop()
    place_chk[k] = 0


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

place_chk = [0] * M

make(0, [])
