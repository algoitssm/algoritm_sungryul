def total(mid, final, subject):
    return mid * 0.35 + final * 0.45 + subject * 0.2

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())

for i in range(1, T+1):
    total_scores = []
    N, K = map(int, input().split())
    for j in range(N):
        mid, final, subject = map(int, input().split())
        total_scores.append(total(mid, final, subject))
    K_score = total_scores[K - 1]

    total_scores.sort(reverse = True)

    pos = total_scores.index(K_score)
    ans = grade[pos // (N // 10)]

    print(f'#{i} {ans}')