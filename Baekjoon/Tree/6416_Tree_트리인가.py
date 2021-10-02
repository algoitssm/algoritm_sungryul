"""
1. 각 노드의 부모 노드 1개인지
2. 루트 노드 1개인지
3. 루트에서 시작해서 모든 노드를 순회할 수 있는지

억지로 꾸역꾸역 푼 기분...
"""

import sys
from collections import deque

input = sys.stdin.readline


def bfs(root, N):  # 루트에서 모든 노드 순회 가능 여부 bfs로 판단
    queue = deque()
    queue.append(root)
    visited[root] = 1
    cnt = 1

    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = 1
                queue.append(nxt)
                cnt += 1
        if cnt == N:  # cnt와 노드 개수가 같아지면 break
            break
    return cnt


# while문 안에 두면 테스트 케이스 끝나기 전에 한 줄 판단하면 초기화되므로 X
tc = 1  # 테스트 케이스 번호
only_parent = True  # 부모 노드가 1개인지 여부
parent = {}  # 자식 노드의 부모 노드 정보 저장할 딕셔너리
root = {}  # 루트 여부 판단 시 사용할 딕셔너리
graph = {}  # bfs 탐색해야 하므로 인접 딕셔너리
visited = {}  # bfs 탐색 위한 visited

while True:
    is_stop = False  # 테스트 케이스 반복 멈출 때 사용. u, v 둘 다 음수일 때

    temp = input().rstrip()  # 끝에 \n 들어가서 rstrip 필요

    if temp == "":  # 빈 줄의 경우
        tc += 1  # 테스트 케이스 번호 1 증가
        # 그 밖의 조건들 모두 초기화
        parent = {}
        only_parent = True
        root = {}
        graph = {}
        visited = {}
    else:
        for uv in temp.split("  "):
            u, v = map(int, uv.split())

            if u < 0 and v < 0:  # u, v 음수면 바깥 while 문 종료
                is_stop = True
                break

            if u == 0 and v == 0:  # u, v 0이면 테스트 케이스 트리인지 여부 판단
                if len(graph) == 0:  # 비어있는 거도 트리 => 안 해주면 33%에서 틀렸습니다.
                    print("Case {} is a tree.".format(tc))
                elif only_parent and len(root) == 1:  # 모든 노드 부모 노드 1개이고 root 노드 1개
                    N = len(graph)  # 전체 노드 개수
                    start = list(root.keys())[0]  # 루트 노드
                    cnt = bfs(start, N)  # bfs 탐색으로 순회할 수 있는 노드 개수

                    if N == cnt:  # 전체 노드 개수와 같으면 트리
                        print("Case {} is a tree.".format(tc))
                    else:
                        print("Case {} is not a tree.".format(tc))
                else:
                    print("Case {} is not a tree.".format(tc))
                break

            # 위 2가지 경우 아닌 때에만 밑에 코드 실행
            # bfs 탐색 위한 그래프
            if graph.get(u):
                graph[u].append(v)
            else:
                graph[u] = [v]
            if not graph.get(v):  # 자식 노드도 빈 리스트 만들어놔야 전체 노드 순회 가능
                graph[v] = []
            # 양 노드 모두 visited 생성. 딕셔너리라서 중복 문제 X
            visited[u] = 0
            visited[v] = 0

            # 부모 노드 여러 개인지 판단
            if parent.get(v):  # 이미 부모 노드 있는 경우
                only_parent = False
            else:  # 부모 노드 없는 경우 딕셔너리에 저장
                parent[v] = u

            # 루드 노드 판단
            if root.get(v):  # 자식 노드가 루트로 표시되어 있으면 딕셔너리에서 삭제
                del root[v]
            if not parent.get(u):  # u가 부모 노드가 없고, root에도 없다면
                root[u] = True

    # u, v 모두 음수인 경우
    if is_stop:
        break
