"""
문제 힌트에 나오듯이 그래프에서 루트 기준으로 경로 제거하면서 풀면 시간 초과
루트부터 탐색하면서 DP 문제처럼 한 번에 리스트에 담고 처리해야 됨
"""

import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline


def countSubnode(start):
    subnode_cnt[start] = 1

    for child in graph[start]:
        if not subnode_cnt[child]:
            countSubnode(child)
            subnode_cnt[start] += subnode_cnt[child]


N, R, Q = map(int, input().split())  # 노드 개수, 루트, 쿼리 수

graph = [[] for _ in range(N + 1)]  # 인접 리스트
subnode_cnt = [0 for _ in range(N + 1)]  # 각 노드의 서브 노트 저장할 리스트

for _ in range(N - 1):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

countSubnode(R)

for _ in range(Q):
    query = int(input())
    print(subnode_cnt[query])
