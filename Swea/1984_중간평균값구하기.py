T = int(input())

for i in range(T):
    num_list = list(map(int, input().split()))
    num_list.remove(max(num_list))
    num_list.remove(min(num_list))
    ans = round(sum(num_list) / len(num_list))

    print(f'#{i+1} {ans}')