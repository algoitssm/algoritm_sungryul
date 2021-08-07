import sys

N = int(input())

data = list(map(int, sys.stdin.readline().split()))

data.sort()

if len(data) % 2:
    ans = data[-1]
    for i in range((len(data) - 1) // 2):
        if data[i] + data[-i-2] > ans:
            ans = data[i] + data[-i-2] 
else:
    ans = 0
    for i in range(len(data) // 2):
        if data[i] + data[-i-1] > ans:
            ans = data[i] + data[-i-1]

print(ans)