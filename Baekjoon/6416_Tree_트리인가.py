"""
1. 각 노드의 부모 노드 1개인지
2. 루트 노드 1개인지
"""

import sys
from collections import deque

input = sys.stdin.readline


def bfs(root):
    queue = deque()
    queue.append(root)
    visited[root] = 1
    cnt = 1

    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = 1
                queue.append(nxt)
                cnt += 1
    return cnt


tc = 1
only_parent = True
parent = {}  # 부모 노드 여러 개인지 판단
root = {}  # 루트 1개인지 판단
graph = {}
visited = {}

while True:
    is_stop = False  # 테스트 케이스 반복 멈출 때 사용. u, v 둘 다 음수일 때

    temp = input().rstrip()

    if temp == "":  # 빈 줄의 경우
        tc += 1
        parent = {}
        only_parent = True
        root = {}
        graph = {}
        visited = {}
    else:
        for uv in temp.split("  "):
            u, v = map(int, uv.split())

            if u < 0 and v < 0:
                is_stop = True
                break

            if u == 0 and v == 0:
                if len(graph) == 0:  # 비어있는 거도 트리 => 33%
                    print("Case {} is a tree.".format(tc))
                elif only_parent and len(root) == 1:
                    N = len(graph)  # 전체 노드 개수
                    start = list(root.keys())[0]  # 루트
                    cnt = bfs(start)

                    if N == cnt:
                        print("Case {} is a tree.".format(tc))
                    else:
                        print("Case {} is not a tree.".format(tc))
                else:
                    print("Case {} is not a tree.".format(tc))
                break

            # 그래프
            if graph.get(u):
                graph[u].append(v)
            else:
                graph[u] = [v]
            if not graph.get(v):
                graph[v] = []
            visited[u] = 0
            visited[v] = 0

            # 부모 노드 여러 개인지 판단
            if parent.get(v):  # 이미 부모 노드 있는 경우
                only_parent = False
            else:  # 부모 노드 없는 경우
                parent[v] = u

            # 루드 노드 판단
            if root.get(v):  # 자식 노드가 루트로 표시되어 있으면 삭제
                del root[v]
            if not parent.get(u):  # u가 부모 노드가 없고, root에도 없다면
                root[u] = True

    if is_stop:
        break
