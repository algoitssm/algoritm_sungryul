import sys

input = sys.stdin.readline


def find_k(k, count):
    if k == 0:
        if count & 1:  # 2의 지수승 빼준 횟수가 홀수면 바꿈
            return 1
        else:  # 짝수면 그대로
            return 0
    else:
        temp = k  # 인자 입력값 저장
        cnt = -1  # 인자 입력값의 log 값

        while k > 0:
            k //= 2
            cnt += 1

        temp -= 2 ** cnt  # ex> 10 -> 2 -> 0 : count 2
        count += 1
        return find_k(temp, count)


k = int(input())

print(find_k(k - 1, 0))
