# 테스트 케이스 수
T = int(input())
# P, Q, R, S, W
test_case = []

for i in range(T):
    test_case.append(list(map(int, input().split())))

for i, case in enumerate(test_case, start = 1):
    P, Q, R, S, W = case
    
    total_A = P * W
    total_B = Q

    if W > R:
        total_B += (W - R) * S
    
    print(f'#{i} {min(total_A, total_B)}')