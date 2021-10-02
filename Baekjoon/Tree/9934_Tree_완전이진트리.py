"""
이진트리 중위 순회한 결과를 보고 트리를 구하는 문제
"""


def find_tree(data, level):
    if data:
        root_idx = len(data) // 2  # 완전이진트리인 data의 중앙값이 root
        ans[level].append(data[root_idx])
        left = data[:root_idx]  # 루트 기준 왼쪽 트리
        right = data[root_idx + 1 :]  # 루트 기준 오른쪽 트리
        # level 하나 증가 시켜서 재귀
        find_tree(left, level + 1)
        find_tree(right, level + 1)
    else:
        return


K = int(input())  # 도시: 2**K - 1개

data = list(map(int, input().split()))

ans = [[] for _ in range(K)]  # 각 level 별로 입력받을 리스트

find_tree(data, 0)  # 루트의 level은 0

for line in ans:
    print(*line)
