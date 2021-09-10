import sys

input = sys.stdin.readline


def dfs(root):
    global ans
    stack = [root]
    visited[root] += 1
    temp = 1

    while stack:
        cur = stack.pop()

        for nxt in tree[cur]:
            if visited[nxt] == -1:
                stack.append(nxt)
                visited[nxt] = visited[cur] + 1
                if len(tree[nxt]) == 1:
                    ans += visited[nxt]
                temp += 1

        if temp == N:
            break


N = int(input())
tree = {}
visited = {}

for _ in range(N - 1):
    node1, node2 = map(int, input().split())
    if tree.get(node1):
        tree[node1].append(node2)
    else:
        tree[node1] = [node2]
    if tree.get(node2):
        tree[node2].append(node1)
    else:
        tree[node2] = [node1]

    visited[node1] = -1
    visited[node2] = -1

ans = 0
dfs(1)

if ans % 2:
    print("Yes")
else:
    print("No")
