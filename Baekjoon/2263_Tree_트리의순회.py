import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

"""
메모리 초과
"""
# def find_pre_order(in_order, post_order):
#     root = post_order[-1]
#
#     if len(in_order) == 1:
#         print(root, end=' ')
#         return
#
#     left_in = []
#     left_post = []
#     right_in = []
#     right_post = []
#
#     for i in range(len(in_order)):
#         if in_order[i] == root:
#             break
#         left_in.append(in_order[i])
#         left_post.append(post_order[i])
#
#     if in_order[-1] != root:
#         right_in = in_order[i+1:]
#         right_post = post_order[i:len(post_order)-1]
#
#     print(root, end=' ')
#     if left_in:
#         find_pre_order(left_in, left_post)
#     if right_in:
#         find_pre_order(right_in, right_post)


"""
in_order에 있는 값들의 위치를 미리 list에 담고,
root 기준으로 왼쪽 서브 트리 노드 개수와 오른쪽 서브 트리 노드 개수로 인덱스 접근
root 인덱스를 .index()로 접근하면 시간 초과
"""


def find_pre_order(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    root = post_order[post_end]
    left = root_pos[root] - in_start
    right = in_end - root_pos[root]

    print(root, end=" ")
    find_pre_order(in_start, in_start + left - 1, post_start, post_start + left - 1)
    find_pre_order(in_end - right + 1, in_end, post_end - right, post_end - 1)


n = int(input())

in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

root_pos = [0 for _ in range(n + 1)]

for i in range(n):
    root_pos[in_order[i]] = i

in_start, in_end, post_start, post_end = 0, n - 1, 0, n - 1

find_pre_order(in_start, in_end, post_start, post_end)
