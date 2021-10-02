"""
inorder
"""

import sys


def in_order(root, level):
    global x_axis
    if left[root] != -1:
        in_order(left[root], level + 1)

    x_axis += 1
    levels[level].append(x_axis)

    if right[root] != -1:
        in_order(right[root], level + 1)


N = int(input())

left = [0 for _ in range(N + 1)]
right = [0 for _ in range(N + 1)]

x_axis = 0

levels = [[] for _ in range(N + 1)]
is_root = [1 for _ in range(N + 1)]

for _ in range(N):
    data, l_node, r_node = map(int, input().split())
    left[data] = l_node
    right[data] = r_node

    if l_node > 0:
        is_root[l_node] = 0
    if r_node > 0:
        is_root[r_node] = 0

for i in range(1, N + 1):
    if is_root[i]:
        root = i
        break

in_order(root, 0)

ans = [1, 1]

for i in range(N + 1):
    if levels[i]:
        temp = levels[i][-1] - levels[i][0] + 1  # +1을 안해주면 제대로 비교가 안 됨...
    else:
        continue

    if temp > ans[1]:
        ans = [i + 1, temp]

print(*ans)
