"""
이진 트리를 전위, 중위, 후위 순회한 결과 출력하는 문제
"""


def pre_order(n):
    if n:
        print(chr(n + ord("A") - 1), end="")
        pre_order(left[n])
        pre_order(right[n])


def in_order(n):
    if n:
        in_order(left[n])
        print(chr(n + ord("A") - 1), end="")
        in_order(right[n])


def post_order(n):
    if n:
        post_order(left[n])
        post_order(right[n])
        print(chr(n + ord("A") - 1), end="")


N = int(input())  # 노드 개수

left = [0] * 27
right = [0] * 27

for _ in range(N):
    temp = input().split()
    if temp[1] != ".":
        left[ord(temp[0]) - ord("A") + 1] = ord(temp[1]) - ord("A") + 1
    if temp[2] != ".":
        right[ord(temp[0]) - ord("A") + 1] = ord(temp[2]) - ord("A") + 1

# 전위 순회
pre_order(1)
print()
in_order(1)
print()
post_order(1)
