from collections import deque


def bfs(s):
    q = deque()
    q.append(s)
    visited = [s]

    while q:
        cur = q.popleft()
        if G.get(cur):
            for nxt in G[cur]:
                if nxt not in visited:
                    q.append(nxt)
                    visited.append(nxt)
                    if ans.get(s):
                        ans[s].append(nxt)
                    else:
                        ans[s] = [nxt]


N = int(input())
G = {}
ans = {}

for _ in range(N):
    s, e = input().split(" => ")
    if G.get(s):
        G[s].append(e)
    else:
        G[s] = [e]

result = []
for c in range(ord("A"), ord("Z") + 1):
    start = chr(c)
    if G.get(start):
        bfs(start)
        if ans.get(start):
            ans[start].sort()
            for end in ans[start]:
                result.append(start + " => " + end)
for c in range(ord("a"), ord("z") + 1):
    start = chr(c)
    if G.get(start):
        bfs(start)
        if ans.get(start):
            ans[start].sort()
            for end in ans[start]:
                result.append(start + " => " + end)

print(len(result))
for line in result:
    print(line)
