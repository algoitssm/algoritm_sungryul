import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline


def cnt_cousin(parent_sibling):
    global data_idx, k_cousin
    cnt = 0
    for _ in range(parent_sibling):
        temp = []
        k_brother = 0
        brother_cnt = 0
        while data_idx < n:
            if not temp:
                temp.append(data[data_idx])
                brother_cnt += 1
                cnt += 1
            else:
                if temp[-1] + 1 == data[data_idx]:
                    temp.append(data[data_idx])
                    brother_cnt += 1
                    cnt += 1
                else:
                    break
            if data[data_idx] == k:
                k_cousin = 1
                k_brother = 1
            data_idx += 1
        if k_brother:
            cnt -= brother_cnt

    return cnt


while True:
    n, k = map(int, input().split())
    if not n:
        break
    data = list(map(int, input().split()))

    data_idx = 1
    k_cousin = 0
    parent_sibling = 1

    while True:
        sibling = cnt_cousin(parent_sibling)
        if k_cousin:
            print(sibling)
            break
        parent_sibling = sibling
