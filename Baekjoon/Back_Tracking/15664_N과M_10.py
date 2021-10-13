def make(k, lst):
    global idx_chk
    if k == M:
        print(*lst)
        return

    for_place = place_chk[k]
    for_idx = idx_chk[:]
    # for_idx = []
    for i in range(N):
        if not place_chk[k] & (1 << nums[i]) and not idx_chk[i]:
            lst.append(nums[i])
            idx_chk[i] = 1
            for_idx.append(i)
            place_chk[k] |= 1 << nums[i]
            make(k + 1, lst)
            lst.pop()

        # 이 조건 추가 안하면
        # 5 3
        # 1 2 2 4 5 반례
        elif not idx_chk[i]:
            idx_chk[i] = 1
            for_idx.append(i)
    place_chk[k] = for_place
    idx_chk = for_idx[:]
    # for idx in for_idx:
    #     idx_chk[idx] = 0
    return


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

idx_chk = [0] * N
place_chk = [0] * M

make(0, [])
