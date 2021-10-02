"""
1. input 밑으로 주석 처리된 코드

하나씩 입력받아서 직접 BST 만들고 후위순회로 출력하는 방식
setrecursionlimit 쓰면 Pypy는 1%에서 메모리 초과. python3는 27% 쯤에서 시간초과
setrecursionlimit 안 쓰면 Pypy Recurtion Error. Python3는 틀렸습니다

2. 주석 처리 안 된 코드

풀이 방법이 도저히 생각 안 나서 구글의 힘을 빌려 풀이...
left_node와 right_node 가리키는 포인터 두 개 두고 하나씩 옮겨가며 재귀
"""

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.left_child = None
#         self.right_child = None


# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self, value):
#         if self.root == None:
#             self.root = Node(value)
#         else:
#             self._insert(value, self.root)

#     def _insert(self, value, cur_node):
#         if value < cur_node.value:
#             if cur_node.left_child == None:
#                 cur_node.left_child = Node(value)
#             else:
#                 self._insert(value, cur_node.left_child)
#         elif value > cur_node.value:
#             if cur_node.right_child == None:
#                 cur_node.right_child = Node(value)
#             else:
#                 self._insert(value, cur_node.right_child)

#     def post_order(self, node):
#         if node.left_child:
#             self.post_order(node.left_child)
#         if node.right_child:
#             self.post_order(node.right_child)
#         print(node.value)


# bst = BST()

# while True:
#     try:
#         bst.insert(int(input()))
#     except:
#         break

# bst.post_order(bst.root)


def post_order(start, end):  # 인자 값은 판단할 리스트의 처음 idx, 끝 idx+1
    if start >= end:
        return
    root = data[start]
    left_node_idx = start + 1  # 왼쪽 자식 노드는 root의 바로 다음 인덱스
    right_node_idx = end  # 오른쪽 자식 노드의 초기 값은 가장 오른쪽 노드의 인덱스+1
    for i in range(start + 1, end):  # 오른쪽 자식 노드는 순회하면서 처음으로 root보다 커지는 값의 인덱스
        if data[i] > data[start]:
            right_node_idx = i
            break
    post_order(left_node_idx, right_node_idx)  # 왼쪽 자식 노드를 루트로 하는 트리 탐색
    post_order(right_node_idx, end)  # 오른쪽 자식 노드를 루트로 하는 트리 탐색
    print(root)  # 루트 출력


data = []
N = 0  # 노드 개수

# 노드 개수가 정해지지 않은 입력 값 받는 방식
while True:
    try:
        data.append(int(input()))
        N += 1  # len() 쓰면 시간 초과 날까봐 append하면서 미리 계산
    except:
        break

post_order(0, N)
