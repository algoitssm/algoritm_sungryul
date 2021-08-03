T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prime_nums = [2, 3, 5, 7, 11]
    result = []

    for prime_num in prime_nums:
        cnt = 0
        while N % prime_num == 0:
            cnt += 1
            N //= prime_num
        result.append(cnt)
    
    ans = ' '.join(tuple(map(str, result)))

    print(f'#{tc} {ans}')