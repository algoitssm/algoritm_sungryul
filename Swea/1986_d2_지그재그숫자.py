T = int(input())

for i in range(T):
    N = int(input())
    ans = 0
    for j in range(1, N+1):
        if j % 2:
            ans += j
        else:
            ans -= j

    print(f'#{i+1} {ans}')