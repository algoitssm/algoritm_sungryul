w, h = map(int, input().split())  # 가로, 세로
N = int(input())  # 상점 개수
# 1 북 2 남 3 서 4 동
data = [list(map(int, input().split())) for _ in range(N)]  # 상점 위치
cur = list(map(int, input().split()))  # 현재 위치

d = {1: 0, 2: 2, 3: 3, 4: 1}

ans = 0

for store in data:
    if abs(d[store[0]] - d[cur[0]]) == 2:  # 북 - 남 or 동 - 서
        if store[0] in (1, 2):
            ans += h + min(cur[1] + store[1], 2 * w - cur[1] - store[1])
        else:
            ans += w + min(cur[1] + store[1], 2 * h - cur[1] - store[1])
    elif store[0] == cur[0]:  # 위치한 곳 같을 때
        ans += abs(store[1] - cur[1])
    else:  # 북-동, 북-서, 남-동, 남-서
        if cur[0] == 1 and store[0] == 4:
            ans += w - cur[1] + store[1]
        elif cur[0] == 1 and store[0] == 3:
            ans += cur[1] + store[1]
        elif cur[0] == 2 and store[0] == 4:
            ans += w - cur[1] + h - store[1]
        elif cur[0] == 2 and store[0] == 3:
            ans += cur[1] + h - store[1]
        elif cur[0] == 3 and store[0] == 1:
            ans += store[1] + cur[1]
        elif cur[0] == 3 and store[0] == 2:
            ans += store[1] + h - cur[1]
        elif cur[0] == 4 and store[0] == 1:
            ans += w - store[1] + cur[1]
        elif cur[0] == 4 and store[0] == 2:
            ans += w - store[1] + h - cur[1]

print(ans)
