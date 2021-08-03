T = int(input())

for tc in range(1, T+1):
    N = int(input())

    test_case = []
    for i in range(N):
        test_case.append(input().split())
    
    print(f'#{tc}')
    result = ''
    for lst in test_case:
        for j in range(int(lst[1])):
            result += lst[0]
            if len(result) == 10:
                print(result)
                result = ''
    print(result)