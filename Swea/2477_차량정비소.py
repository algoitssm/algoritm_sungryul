import heapq
from collections import deque

T = int(input())

for tc in range(1, T + 1):
    # N:접수창구 개수  M:정비창구 개수  K:고객수  A, B:지갑고객 접수, 정비 번호
    N, M, K, A, B = map(int, input().split())

    info = [0] + list(map(int, input().split()))
    repair = [0] + list(map(int, input().split()))

    customers = [0] + list(map(int, input().split()))

    info_waiting = []
    repair_waiting = deque()

    in_info = [[0, 0] for _ in range(N + 1)]  # [고객 번호, 소요 시간]
    in_repair = [[0, 0] for _ in range(M + 1)]

    customer_chk = [[0, 0] for _ in range(K + 1)]  # [접수창구, 정비창구]

    customer_idx = 1
    t = 0  # 현재 시간
    cnt = 0  # 정비 완료한 손님 카운트

    # 접수 완료한 고객 K명 초과할 때까지
    while cnt < K:
        # 접수 창구에서 접수 끝난 고객 repair_waiting에 넣음
        # => 작은 인덱스부터 조회하므로 접수 창구 번호 작은 고객이 먼저 들어감
        for i in range(1, N + 1):
            if in_info[i][1]:
                in_info[i][1] -= 1
                if not in_info[i][1]:  # 소요시간 0이 된 경우
                    repair_waiting.append(in_info[i][0])

        # 정비 창구에서 정비 끝난 고객 cnt + 1
        for i in range(1, M + 1):
            if in_repair[i][1]:
                in_repair[i][1] -= 1
                if not in_repair[i][1]:
                    cnt += 1

        # 방문한 손님 info_waiting에 넣음
        while customer_idx <= K and customers[customer_idx] == t:
            heapq.heappush(info_waiting, customer_idx)
            customer_idx += 1

        # 고객 번호 작은 순으로 빈 접수 창구로 넣음
        for i in range(1, N + 1):
            if not in_info[i][1] and info_waiting:  # i번 접수 창구 비어있는 경우
                cur_customer = heapq.heappop(info_waiting)
                customer_chk[cur_customer][0] = i
                in_info[i][0] = cur_customer
                in_info[i][1] = info[i]

        # 먼저 기다린 고객 순으로 빈 정비 창구로 넣음
        for i in range(1, M + 1):
            if not in_repair[i][1] and repair_waiting:
                cur_customer = repair_waiting.popleft()
                customer_chk[cur_customer][1] = i
                in_repair[i][0] = cur_customer
                in_repair[i][1] = repair[i]

        t += 1

    ans = 0
    for i in range(1, K + 1):
        if customer_chk[i][0] == A and customer_chk[i][1] == B:
            ans += i

    if not ans:
        ans = -1

    print("#{} {}".format(tc, ans))
