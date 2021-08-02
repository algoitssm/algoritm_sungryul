T = int(input())

test_cases = []
for i in range(T):
    test_cases.append(int(input()))

for i, case in enumerate(test_cases, start = 1):
    check_num = []
    num = 0

    while len(check_num) <10:
        num += case
        temp = str(num)
        for char in temp:
            if char not in check_num:
                check_num.append(char)

    print(f'#{i} {num}')