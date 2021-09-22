'''
inorder
'''

import sys

sys.stdin = open("input.txt")

def in_order(root, level):
    global x_axis
    if left[root] != -1:
        in_order(left[root], level+1)

    x_axis += 1
    levels[level].append(x_axis)

    if right[root] != -1:
        in_order(right[root], level+1)


N = int(input())

left = [0 for _ in range(N+1)]
right = [0 for _ in range(N+1)]

x_axis = 0

levels = [[] for _ in range(N+1)]
is_root = [True for _ in range(N+1)]

for _ in range(N):
    data, l_node, r_node = map(int, input().split())
    left[data] = l_node
    right[data] = r_node

    is_root[l_node] = False
    is_root[r_node] = False

for i in range(1, N+1):
    if is_root[i]:
        root = i
        break

in_order(root, 0)

ans = [1, 1]

for i in range(len(levels)):
    if levels[i]:
        temp = levels[i][-1] - levels[i][0]
    else:
        continue

    if temp > ans[1]:
        ans = [i+1, temp+1]

print(*ans)