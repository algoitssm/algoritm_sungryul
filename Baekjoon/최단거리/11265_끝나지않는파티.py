"""
다익스트라 사용 시 시간 초과
https://namu.wiki/w/%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
플로이드 워셜 알고리즘: 가능한 모든 노드 쌍에 대해 최단 거리를 구하는 알고리즘
i -> j로 바로 가능 비용을 일단 넣고
k를 갱신하며 k를 거쳐갈 때 더 빠른 경우 갱신
음의 가중치를 가지는 그래프에서도 사용 가능
"""
import heapq

INF = 1000000001


# def dijkstra(s):
#     visited = [0] * (N + 1)
#     heap = []
#     heapq.heappush(heap, (0, s))

#     while heap:
#         w, v = heapq.heappop(heap)

#         if not visited[v]:
#             visited[v] = 1
#             dist[s][v] = w

#             for i in range(1, N + 1):
#                 if not visited[i]:
#                     heapq.heappush(heap, (dist[s][v] + G[v][i], i))


def floyd():
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i == j:
                    dist[i][j] = 0
                else:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


answer = ["Enjoy other party", "Stay here"]

N, M = map(int, input().split())
dist = [[INF] * (N + 1) for _ in range(N + 1)]
for r in range(1, N + 1):
    data = [INF] + list(map(int, input().split()))
    for c in range(1, N + 1):
        if data[c]:
            dist[r][c] = data[c]

floyd()
# chk = [0] * (N + 1)

ans = []
for _ in range(M):
    A, B, C = map(int, input().split())
    #     if not chk[A]:
    #         chk[A] = 1
    #         dijkstra(A)
    if dist[A][B] <= C:
        ans.append(answer[0])
    else:
        ans.append(answer[1])

for line in ans:
    print(line)
