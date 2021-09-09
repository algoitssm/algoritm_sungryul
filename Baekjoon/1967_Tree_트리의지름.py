import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

def cnt_weight(node1, node2):
    global temp
    if node1 == node2:
        return
    temp += weight[node1][tree[node1][0]] + weight[node2][tree[node2][0]]
    cnt_weight(tree[node1], tree[node2])


n = int(input())    # 노드의 개수
tree = [[] for _ in range(n+1)] # 인덱스가 자식 노드, 값이 부모 노드
check_terminal = [True for _ in range(n+1)]    # 단말 노드 체크 위한 리스트
terminal_node = []  # 단말 노드 저장할 리스트
weight = [[0] * (n+1) for _ in range(n+1)]  # child -> parent 이동 시 weight

for _ in range(n-1):
    parent, child, n_weight = map(int, input().split())
    tree[child].append(parent)
    check_terminal[parent] = False
    weight[child][parent] = n_weight

n_terminal = 0
for i in range(1, n+1):
    if check_terminal[i]:
        terminal_node.append(i)
        n_terminal += 1

ans = 0
for i in range(n_terminal-1):
    for j in range(i+1, n_terminal):
        temp = 0
        cnt_weight(terminal_node[i], terminal_node[j])
        if temp > ans:
            ans = temp

print(ans)

