import sys

input = sys.stdin.readline


T = int(input())


def find_ancestor(node1, node2):
    stack = [node1, node2]
    visited[node1] = 1
    visited[node2] = 1

    while stack:
        cur = stack.pop()

        for nxt in tree[cur]:
            if visited[nxt]:  # 다른 노드가 방문한 곳을 만날 때가 가장 가까운 공통 조상
                return nxt
            stack.append(nxt)
            visited[nxt] = 1


for _ in range(T):
    N = int(input())

    tree = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        parent, child = map(int, input().split())
        tree[child].append(parent)  # 자식의 부모 노드에 대한 정보만 트리에 담음

    visited = [0 for _ in range(N + 1)]

    node1, node2 = map(int, input().split())

    ancestor = find_ancestor(node1, node2)

    print(ancestor)
