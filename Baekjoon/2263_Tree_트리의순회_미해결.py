import sys

sys.setrecursionlimit(10**5)
sys.stdin = open("input.txt")

'''
메모리 초과
'''
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

def find_pre_order(in_start, in_end, post_start, post_end):
    if in_start > in_end:
        return

    root = post_order[post_end]
    left_in_start = in_start
    left_in_end = in_start - 1
    left_post_start = post_start
    left_post_end = post_start - 1

    for i in range(in_start, in_end+1):
        if in_order[i] == root:
            break
        left_in_end += 1
        left_post_end += 1

    right_in_start = i + 1
    right_in_end = in_end
    right_post_start = i
    right_post_end = post_end - 1

    print(root, end=' ')
    find_pre_order(left_in_start, left_in_end, left_post_start, left_post_end)
    find_pre_order(right_in_start, right_in_end, right_post_start, right_post_end)


n = int(input())

in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

in_start, in_end, post_start, post_end = 0, n-1, 0, n-1

find_pre_order(in_start, in_end, post_start, post_end)
