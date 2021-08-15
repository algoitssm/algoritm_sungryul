import heapq
import sys

# N개의 유제품이 주어지고 3개의 유제품을 사면 3개 중 가장 싼 제품은 무료
# N개의 유제품을 살 때, 최소비용
# input() 쓰면 시간 초과!!
N = int(sys.stdin.readline())
data = [-int(sys.stdin.readline()) for _ in range(N)]
heapq.heapify(data)
ans = 0
# 시간초과 풀이
# data.sort()
# # 오름차순으로 정렬해서 큰 값을 무료로 받을 수 있도록 풀이
# while True:
#     ans += data.pop()
#     if not data:
#         break
#     ans += data.pop()
#     if not data:
#         break
#     data.pop()
#     if not data:
#         break

# heapq로 내림차순으로 정렬하려면 - 붙여서 넣어준다
# error 발생하면 queue 내에 데이터 없으므로 break
while True:
    try:
        ans -= heapq.heappop(data)
    except:
        break
    try:
        ans -= heapq.heappop(data)
    except:
        break
    try:
        heapq.heappop(data)
    except:
        break
print(ans)
