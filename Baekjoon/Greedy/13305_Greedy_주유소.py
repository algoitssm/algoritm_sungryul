import sys

N = int(sys.stdin.readline())

road = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

ans = 0
cnt = 0
min_price = price[0]
min_idx = 0

for i in range(N-1):
    if min_price <= price[i]:
        cnt += 1 
    else:
        ans += sum(road[min_idx : min_idx + cnt]) * min_price
        min_price = price[i]
        min_idx = i
        cnt = 1
    if i == N - 2:  # if ~ else 밖에서 다시 더해줘야 모든 경우의 수에서 마지막 케이스 더해줄 수 있음
        ans += sum(road[min_idx : min_idx + cnt]) * min_price

print(ans)