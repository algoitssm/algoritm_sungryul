import sys

input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    node1, node2 = map(int, input().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

q = int(input())

for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:  # 부모 노드 포함해서 2개 이상이면 단절점
        if len(tree[k]) > 1:
            print("yes")
        else:
            print("no")
    else:  # 모든 간선은 단절선
        print("yes")
