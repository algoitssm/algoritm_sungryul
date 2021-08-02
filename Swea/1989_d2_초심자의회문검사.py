T = int(input())

for i in range(T):
    input_str = input()
    ans = 1
    start = 0
    end = len(input_str) - 1

    while start < end:
        if input_str[start] != input_str[end]:
            ans = 0
            break
        start += 1
        end -= 1

    print(f'#{i+1} {ans}')