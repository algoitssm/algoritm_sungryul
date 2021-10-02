import sys
import heapq

N = int(sys.stdin.readline())

data = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
data.sort(key=lambda x: x[0])

# 강의실 별 끝 시간 저장할 큐
queue = []
heapq.heappush(queue, data[0][1])

for i in range(1, N):
    # 가장 먼저 끝나는 강의의 끝 시간보다 나중에 시작하는 경우, 같은 강의실 사용하므로 해당 강의실 끝 시간 바꿔줌
    if data[i][0] >= queue[0]:
        heapq.heappop(queue)
        heapq.heappush(queue, data[i][1])
    # 가장 먼저 끝나는 강의의 끝 시간보다 먼저 시작하는 경우, 강의실 하나 더 필요하므로 큐에 그냥 추가
    else:
        heapq.heappush(queue, data[i][1])

print(len(queue))
