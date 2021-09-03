"""
이진트리 중위 순회한 결과를 보고 트리를 구하는 문제
"""


def find_tree(data, level):
    if data:
        root_idx = len(data) // 2
        ans[level].append(data[root_idx])
        left = data[:root_idx]
        right = data[root_idx + 1 :]
        find_tree(left, level + 1)
        find_tree(right, level + 1)
    else:
        return


K = int(input())  # 도시: 2**K - 1개

data = list(map(int, input().split()))

ans = [[] for _ in range(K)]

find_tree(data, 0)

for line in ans:
    print(*line)
