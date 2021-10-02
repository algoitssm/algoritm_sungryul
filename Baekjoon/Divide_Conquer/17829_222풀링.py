import sys

input = sys.stdin.readline

N = int(input())


def divide(square):
    cur_N = len(square)
    half_N = cur_N // 2
    first = square[:half_N]
    second = square[:half_N]
    third = square[half_N:]
    fourth = square[half_N:]
    for row in range(half_N):
        first[row] = first[row][:half_N]
        second[row] = second[row][half_N:]
        third[row] = third[row][:half_N]
        fourth[row] = fourth[row][half_N:]

    return first, second, third, fourth


def conquer(square):
    if len(square) == 1:
        return square[0][0]
    else:
        first, second, third, fourth = divide(square)
        result = []
        result.append(conquer(first))
        result.append(conquer(second))
        result.append(conquer(third))
        result.append(conquer(fourth))

        result.sort()

        return result[2]


data = [list(map(int, input().split())) for _ in range(N)]

ans = conquer(data)

print(ans)
