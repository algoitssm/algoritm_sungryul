N = int(input())

data = list(map(int, input().split()))

data.sort()

ans = data[-1] + sum(data[: len(data) - 1]) * 0.5
if ans % 1 == 0:
    ans = int(ans)

print(ans)
