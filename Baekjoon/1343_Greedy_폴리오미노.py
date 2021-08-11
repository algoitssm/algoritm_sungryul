board = input()

# board = board.replace("XXXX", "AAAA")
# board = board.replace("XX", "BB")

# if "X" in board:
#     print(-1)
# else:
#     print(board)

poly = ["AAAA", "BB"]

cnt = 0
result = []

if len(board) <= 1:
    if board == ".":  # 길이가 1이하일 때 무조건 -1 하려다가 계속 오답...
        print(".")
    else:
        print(-1)

else:
    for char in board:
        if char == "X":
            cnt += 1
            if cnt == 2:
                result.append(poly[1])
            if cnt == 4:
                result[-1] = poly[0]
                cnt = 0
        else:
            if cnt % 2:
                result = -1
                break
            else:
                cnt = 0
                result.append(".")
    if result == -1:
        print(result)
    elif cnt == 1 or cnt == 3:
        print(-1)
    else:
        print("".join(result))
