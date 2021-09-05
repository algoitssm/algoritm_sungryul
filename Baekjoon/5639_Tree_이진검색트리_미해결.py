"""
하나씩 입력받아서 직접 BST 만들고 후위순회로 출력하는 방식
setrecursionlimit 쓰면 Pypy는 1%에서 메모리 초과. python3는 27% 쯤에서 시간초과
setrecursionlimit 쓰면 Pypy Recurtion Error. Python3는 틀렸습니다
"""
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
            else:
                self._insert(value, cur_node.right_child)

    def post_order(self, node):
        if node.left_child:
            self.post_order(node.left_child)
        if node.right_child:
            self.post_order(node.right_child)
        print(node.value)


bst = BST()

while True:
    try:
        bst.insert(int(input()))
    except:
        break

bst.post_order(bst.root)
