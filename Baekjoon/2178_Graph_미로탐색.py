from collections import deque

N, M = map(int, input().split())  # N x M 배열. (1, 1) 출발 (N, M) 도착 위치

# 최단 경로 찾는 문제라 bfs로 풀이
def bfs(start, dest):
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1  # visited는 좌표값으로 접근하기 위해 2차원 리스트로 구성

    while queue:
        num = queue.popleft()

        if num == dest:  # dest 찾으면 해당 좌표에 누적된 이동거리 return
            return visited[num[0]][num[1]]

        for nxt in graph[num]:
            if not visited[nxt[0]][nxt[1]]:
                queue.append(nxt)
                visited[nxt[0]][nxt[1]] = (
                    visited[num[0]][num[1]] + 1
                )  # 하나씩 이동하면서 최소 거리 찾기 위해 visited에 누적합. bfs로 접근하기 때문에 중복해서 더해질 문제 X


data = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
# 상하좌우로 이동하며 그래프에 넣어주기 위한 델타
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 인접행렬이나 인접리스트보다 딕셔너리로 하는 게 깔끔할 거 같아서 딕셔너리로 그래프 구성
graph = dict()
# 각 좌표 이동하며 상, 하, 좌, 우에 갈 수 있는 곳 있는지 그래프로 구성
for row in range(N):
    for col in range(M):
        for i in range(4):
            nxt_row = row + dx[i]
            nxt_col = col + dy[i]
            # 좌표 범위 내면서, 이동할 위치가 1이고, 현재 위치도 1이면
            if (
                0 <= nxt_col < M
                and 0 <= nxt_row < N
                and data[nxt_row][nxt_col] == 1
                and data[row][col] == 1
            ):
                if graph.get((row, col)):  # 딕셔너리에 현재 좌표 키 존재하면 append
                    graph[(row, col)].append((nxt_row, nxt_col))
                else:  # 키 존재하지 않으면 새로운 키 생성
                    graph[(row, col)] = [(nxt_row, nxt_col)]

start = (0, 0)  # 시작 좌표
dest = (N - 1, M - 1)  # 끝 좌표

print(bfs(start, dest))
