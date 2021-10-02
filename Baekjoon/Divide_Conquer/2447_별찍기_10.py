import sys


def make_star(n, start_row, start_col, is_blank):
    if n == 1:
        if is_blank:
            data[start_row][start_col] = 0
        else:
            data[start_row][start_col] = 1
    else:
        for row in range(3):
            for col in range(3):
                if row == 1 and col == 1:
                    make_star(n // 3, start_row + row * n // 3, start_col + col * n // 3, 1)
                else:
                    make_star(
                        n // 3,
                        start_row + row * n // 3,
                        start_col + col * n // 3,
                        1 if is_blank else 0,
                    )


N = int(input())

data = [[-1] * N for _ in range(N)]

make_star(N, 0, 0, 0)

for row in range(N):
    for col in range(N):
        if data[row][col]:
            print("*", end="")
        else:
            print(" ", end="")
    print()
