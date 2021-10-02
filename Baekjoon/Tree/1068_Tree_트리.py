"""
전체 트리를 인접 리스트로 입력 받고
del_leaf 함수 통해 트리에서 visited 처리하여 삭제하고
cnt_terminal 함수 통해 자식 노드 없는 말단 노드 개수 계산
"""

from collections import deque

# 방문 처리하면 cnt_terminal에서 방문 X => 삭제와 동일
def del_leaf(start):
    for_del = deque()
    for_del.append(start)
    visited[start] = 1

    while for_del:
        cur = for_del.popleft()

        for nxt in tree[cur]:
            if not visited[nxt]:
                for_del.append(nxt)
                visited[nxt] = 1


def cnt_terminal(root):
    for_cnt = deque()
    for_cnt.append(root)
    visited[root] = 1
    cnt = 0

    while for_cnt:
        cur = for_cnt.popleft()
        cnt_sign = True  # 방문하지 않은 자식 노드가 있는지 여부

        for nxt in tree[cur]:
            if not visited[nxt]:
                for_cnt.append(nxt)
                visited[nxt] = 1
                cnt_sign = False

        if cnt_sign:
            cnt += 1

    return cnt


N = int(input())  # 50 이하 자연수. 노드 개수

data = list(map(int, input().split()))
tree = [[] for _ in range(N)]
visited = [0 for _ in range(N)]

target = int(input())

for i in range(N):
    if data[i] == -1:
        root = i
    else:
        tree[data[i]].append(i)

ans = 0

del_leaf(target)

if not visited[root]:  # 루트부터 제거하는 경우에는 0을 출력해야 하므로 조건 필요
    ans = cnt_terminal(root)

print(ans)
