def make(k, lst):
    if k == M:
        print(*lst)
        return
    for i in range(N):
        if not lst or lst[-1] <= nums[i]:
            lst.append(nums[i])
            make(k + 1, lst)
            lst.pop()


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
make(0, [])
