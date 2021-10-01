import sys
from itertools import permutations

sys.stdin = open("input.txt")

T = int(input())


def dfs(stack, length):
    global min_val, max_val
    if length == N - 1:
        result = int(nums[0])
        for i in range(N - 1):
            # 시간 초과
            # result = str(result)
            # result += stack[i] + nums[i + 1]
            # result = int(str(eval(result)).split(".")[0])
            num = int(nums[i + 1])
            if stack[i] == "+":
                result += num
            elif stack[i] == "-":
                result -= num
            elif stack[i] == "*":
                result *= num
            else:
                result /= num
                result = int(str(result).split(".")[0])
        if result < min_val:
            min_val = result
        if result > max_val:
            max_val = result
        return
    for i in range(4):
        if operator[i]:
            operator[i] -= 1
            stack.append(ops[i])
            dfs(stack, length + 1)
            stack.pop()
            operator[i] += 1


for tc in range(1, T + 1):
    N = int(input())  # 숫자 개수
    operator = list(map(int, input().split()))  # 0: +  1: -  2: *  3: /
    ops = ["+", "-", "*", "/"]
    nums = input().split()

    min_val = 100000000
    max_val = -100000000

    dfs([], 0)

    print("#{} {}".format(tc, max_val - min_val))

    # op = []
    # for i in range(4):
    #     op += [i] * operator[i]
    #
    # permus = set(permutations(op, N - 1))
    #
    # max_val = -100000000
    # min_val = 100000000
    # for permu in permus:
    #     temp = nums[0]
    #
    #     for i in range(N - 1):
    #         if permu[i] == 0:
    #             temp += nums[i + 1]
    #         elif permu[i] == 1:
    #             temp -= nums[i + 1]
    #         elif permu[i] == 2:
    #             temp *= nums[i + 1]
    #         else:
    #             temp /= nums[i + 1]
    #             temp = int(str(temp).split(".")[0])
    #     if temp < min_val:
    #         min_val = temp
    #     if temp > max_val:
    #         max_val = temp
    #
    # print("#{} {}".format(tc, max_val - min_val))
