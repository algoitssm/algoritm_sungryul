import sys

N = int(sys.stdin.readline())

ropes = []
for i in range(N):
    ropes.append(int(sys.stdin.readline()))

ropes.sort(reverse=True)

ans = 0
while ropes:
    length = len(ropes)
    min_weight = ropes.pop()
    if ans < length * min_weight:
        ans = length * min_weight

print(ans)