from collections import deque


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    # bfs가 중간에서 안 풀릴 때는 큐에 넣어주는 순서 맞는지 확인!
    while queue:
        cur = queue.popleft()
        cur_double = cur * 2
        cur_plus = cur + 1
        cur_minus = cur - 1

        if cur_double <= 100000 and not visited[cur_double]:
            visited[cur_double] = True
            cnt[cur_double] = cnt[cur]
            queue.append(cur_double)
        # - 이후 * 2 해줬을 때 도착하는 것이 +로 도착하는 경우보다 cost 작으므로 minus 먼저 계산  ex> 4 6
        if cur_minus >= 0 and not visited[cur_minus]:
            visited[cur_minus] = True
            cnt[cur_minus] = cnt[cur] + 1
            queue.append(cur_minus)
        if cur_plus <= 100000 and not visited[cur_plus]:
            visited[cur_plus] = True
            cnt[cur_plus] = cnt[cur] + 1
            queue.append(cur_plus)
        if cur == K or cur_double == K or cur_plus == K or cur_minus == K:
            break


N, K = map(int, input().split())
cnt = [0 for _ in range(100001)]
visited = [False for _ in range(100001)]

bfs(N)
print(cnt[K])
