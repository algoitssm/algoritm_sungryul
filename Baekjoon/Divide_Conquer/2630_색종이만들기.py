import sys


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
    global white, blue
    if len(square) == 1:
        if square[0][0] == 1:
            return 1
        else:
            return 0

    first, second, third, fourth = divide(square)
    result_1 = conquer(first)
    result_2 = conquer(second)
    result_3 = conquer(third)
    result_4 = conquer(fourth)

    if result_1 == 0 and result_2 == 0 and result_3 == 0 and result_4 == 0:
        return 0
    elif result_1 == 1 and result_2 == 1 and result_3 == 1 and result_4 == 1:
        return 1
    else:
        if result_1 == 1:
            blue += 1
        elif result_1 == 0:
            white += 1
        if result_2 == 1:
            blue += 1
        elif result_2 == 0:
            white += 1
        if result_3 == 1:
            blue += 1
        elif result_3 == 0:
            white += 1
        if result_4 == 1:
            blue += 1
        elif result_4 == 0:
            white += 1
        return -1


N = int(input())

data = [list(map(int, input().split())) for _ in range(N)]

white, blue = 0, 0

result = conquer(data)

if result == 1:
    blue += 1
elif result == 0:
    white += 1

print(white)
print(blue)
