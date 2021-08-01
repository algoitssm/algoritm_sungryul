T = int(input())

cases = []

for i in range(T):
    cases.append(input())

for idx, case in enumerate(cases, start = 1):
    ans = 0
    for i in range(11):
        if case[:i+1] * (len(case) // (i+1)) == case[:(i+1) * (len(case) // (i+1))]:
            ans = i + 1
            break
    print(f'#{idx} {ans}')