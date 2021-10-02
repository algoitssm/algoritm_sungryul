"""
1. pre_order에서 한 칸씩 전진시키며 in_order를 pre_order에서의 값을 기준으로 left와 right로 나눈다.
2. pre_order는 계속 한 칸씩 전진하고 left -> right 순으로 같은 작업 반복
3. 길이가 1이면 해당 노드 출력
4. left재귀, right재귀 끝나면 해당 루프의 루트 출력

=>  전위 순회는 루트, ___레프트___, ___라이트___ 순으로 오므로 자르는 루트 제공
    중위 순회는 ___레프트___, 루트, ___라이트___ 순으로 잘리는 트리
"""

import sys

input = sys.stdin.readline

T = int(input())


def find_post_order(tree):
    global root_idx

    if len(tree) == 1:
        print(tree[0], end=" ")
        return

    root = pre_order[root_idx]
    left_subtree = []
    right_subtree = []

    for i in range(len(tree)):
        if tree[i] == pre_order[root_idx]:
            break
        left_subtree.append(tree[i])
    if i < len(tree) - 1:
        right_subtree = tree[i + 1 :]

    if left_subtree:
        root_idx += 1
        find_post_order(left_subtree)
    if right_subtree:
        root_idx += 1
        find_post_order(right_subtree)
    print(root, end=" ")


for _ in range(T):
    n = int(input())

    pre_order = input().split()
    in_order = input().split()

    root_idx = 0
    find_post_order(in_order)
    print()
