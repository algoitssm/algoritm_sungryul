import sys

input = sys.stdin.readline


def dfs(root):
    stack = [root]
    visited[root] += 1
    giga_len = -1  # 루트 ~ 기가노드까지 거리
    branch_len = 0  # 루트 ~ 리프까지 거리
    node_cnt = 0  # 확인한 노드 개수

    while stack:
        cur = stack.pop()

        if giga_len == -1 and len(tree[cur]) >= 2 and cur == R:  # 루트 노드의 경우 인접 리스트에 2개 이상이면 기가 노드
            giga_len = visited[cur]
        elif giga_len == -1 and len(tree[cur]) > 2:  # 루트 노드가 아닌 경우 인접 리스트에 3개 이상이여야 기가 노드
            giga_len = visited[cur]

        for nxt in tree[cur]:
            if visited[nxt[0]] == -1:
                stack.append(nxt[0])
                node_cnt += 1
                visited[nxt[0]] = visited[cur] + nxt[1]
                if visited[nxt[0]] > branch_len:
                    branch_len = visited[nxt[0]]

        if node_cnt == N:
            break

    if giga_len == -1:
        giga_len, branch_len = branch_len, 0

    return giga_len, branch_len


N, R = map(int, input().split())  # 노드 개수, 루트 노드

tree = [[] for _ in range(N + 1)]  # 인접 리스트 형식으로 트리 구성
visited = [-1 for _ in range(N + 1)]  # visitied에 루트부터 거리 입력

for _ in range(N - 1):
    a, b, d = map(int, input().split())

    tree[a].append((b, d))
    tree[b].append((a, d))

giga, branch = dfs(R)

if giga and branch:  # giga 노드가 리프노드가 아닌 경우
    print(giga, branch - giga)
else:  # giga 노드가 리프노드인 경우
    print(giga, branch)
