N = int(input())

time_list = list(map(int, input().split()))
ans = 0

time_list.sort()
for i in range(N):
    ans += sum(time_list[:i+1])

print(ans)