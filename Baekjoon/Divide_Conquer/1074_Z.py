def divide(n, row, col):
    first = (row, col)
    second = (row, col + 2 ** (n - 1))
    third = (row + 2 ** (n - 1), col)
    fourth = (row + 2 ** (n - 1), col + 2 ** (n - 1))

    return first, second, third, fourth


def conquer(n, row, col, num):  # 2의 지수승 n, 시작 좌표 r, c, 넣어줄 num
    global ans
    if n == 0:
        if row == r and col == c:
            ans = num
        return

    first, second, third, fourth = divide(n, row, col)
    if r < third[0] and c < second[1]:
        conquer(n - 1, first[0], first[1], num)
    # 사각형의 시작점은 num에서 2 ** ((n-1) + (n-1)) 더해준 값
    elif r < third[0] and second[1] <= c:
        conquer(n - 1, second[0], second[1], num + 2 ** (2 * n - 2))
    # 사각형의 시작점은 num에서 2 * 2 ** ((n-1) + (n-1)) 더해준 값
    elif third[0] <= r and c < second[1]:
        conquer(n - 1, third[0], third[1], num + 2 * 2 ** (2 * n - 2))
    # 사각형의 시작점은 num에서 3 * 2 ** ((n-1) + (n-1)) 더해준 값
    else:
        conquer(n - 1, fourth[0], fourth[1], num + 3 * 2 ** (2 * n - 2))


N, r, c = map(int, input().split())

ans = 0

conquer(N, 0, 0, 0)
print(ans)
