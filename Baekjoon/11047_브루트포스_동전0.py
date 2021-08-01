import sys

N, K = map(int, sys.stdin.readline().split())

coins = []
for i in range(N):
    coins.append(int(sys.stdin.readline().rstrip()))

coins.sort(reverse=True)
ans = 0

for coin in coins:
    ans += K // coin
    K = K % coin

    if K == 0:
        break

print(ans)