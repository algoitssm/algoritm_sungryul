T = int(input())

test_cases = []

for i in range(T):
    N = int(input())
    test_cases.append(list(map(int, input().split())))

def calc_profit(lst):
    # 처음에 재귀함수로 풀려다가 시간초과. 앞에서부터 최대값 찾아 그 이전 값 더해주는 방식으로 했으나 시간 초과.
    # 다른 풀이 참조하여 뒤에서부터 lst[-1] max 값으로 두고 거꾸로 더해주면서 더 큰 값 만나면 max 값 갱신하는 방식

    # max_idx = lst.index(max(lst))

    # if max_idx != len(lst) - 1:
    #     return (max(lst) * max_idx - sum(lst[:max_idx])) + calc_profit(lst[max_idx + 1:])
    # else:
    #     return max(lst) * max_idx - sum(lst[:max_idx])

    # ans = 0
    # start = 0

    # while True:
    #     max_idx = lst.index(max(lst[start:]))
    #     ans += max(lst[start:]) * (max_idx - start) - sum(lst[start:max_idx])
    #     start = max_idx + 1
        
    #     if start >= len(lst) - 1:
    #         break
    # return ans

    ans = 0
    max_price = lst[-1]

    for i in range(len(lst) - 2, -1, -1):
        if max_price < lst[i]:
            max_price = lst[i]
        else:
            ans += max_price - lst[i]
    return ans


for i, case in enumerate(test_cases, start = 1):
    print(f'#{i} {calc_profit(case)}')