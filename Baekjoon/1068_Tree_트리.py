from collections import deque


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
        cnt_sign = True

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

if not visited[root]:
    ans = cnt_terminal(root)

print(ans)
