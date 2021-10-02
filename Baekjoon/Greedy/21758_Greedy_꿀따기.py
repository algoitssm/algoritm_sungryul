"""
N개의 장소에 1개의 꿀통과 2개의 벌 시작점을 두고, 
각 벌의 시작점에서 꿀통까지 가면서 그 사이의 꿀의 합을 최대로 만드는 문제
"""

import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
total = sum(data)
ans = 0

# 1.
total_1 = total - data[0]
passed_1 = 0
# 2.
total_2 = total - data[N - 1]
passed_2 = 0
for i in range(1, N - 1):
    # 1. data[N-1] 꿀통. data[0] 벌 한마리 시작
    passed_1 += data[i]
    temp = (total_1 - data[i]) + (total_1 - passed_1)
    if ans < temp:
        ans = temp

    # 2. data[0] 꿀통. data[N-1] 벌 한마리 시작
    passed_2 += data[N - 1 - i]
    temp = (total_2 - data[N - 1 - i]) + (total_2 - passed_2)
    if ans < temp:
        ans = temp

    # 3. data[1, N-2] 사이 꿀통
    temp = total - data[0] - data[N - 1] + data[i]
    if ans < temp:
        ans = temp

print(ans)

# data[N-1] > data[0]이라고 해서 무조건 # 1.이 크거나
# data[0] > data[N-1]]이라고 해서 무조건 # 2.이 크지 않음
# 위와 같이 조건문을 달면, 오답
