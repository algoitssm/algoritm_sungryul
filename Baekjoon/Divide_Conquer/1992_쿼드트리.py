def divide(r, c, n):
    first = [data[row][c : c + n // 2] for row in range(r, r + n // 2)]
    second = [data[row][c + n // 2 : c + n] for row in range(r, r + n // 2)]
    third = [data[row][c : c + n // 2] for row in range(r + n // 2, r + n)]
    fourth = [data[row][c + n // 2 : c + n] for row in range(r + n // 2, r + n)]

    return first, second, third, fourth


def conquer(data, n, r, c):
    if n == 1:
        return data[0][0]
    first, second, third, fourth = divide(r, c, n)

    result_1 = conquer(first, n // 2, r, c)
    result_2 = conquer(second, n // 2, r, c + n // 2)
    result_3 = conquer(third, n // 2, r + n // 2, c)
    result_4 = conquer(fourth, n // 2, r + n // 2, c + n // 2)

    result = ""
    if (
        len(result_1) == 1  # 길이 1이 아닌 4개 짜리가 같은 경우도 있어서 처리 필요
        and result_1 == result_2
        and result_2 == result_3
        and result_3 == result_4
    ):
        result = result_1
    else:
        result += "(" + result_1 + result_2 + result_3 + result_4 + ")"
    return result


N = int(input())

data = [list(input()) for _ in range(N)]

ans = conquer(data, N, 0, 0)

print(ans)
