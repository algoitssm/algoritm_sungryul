from itertools import combinations
from collections import deque

T = int(input())


def chk(data):
    for col in range(W):
        cnt = 0
        checked = []
        for row in range(D):  # column의 row를 하나씩 내려가며 탐색
            if not checked:  # checked 비어있으면
                checked.append(data[row][col])
                cnt += 1
            else:
                if checked[-1] == data[row][col]:  # checked 마지막 값과 같으면 cnt += 1
                    cnt += 1
                else:
                    checked = [data[row][col]]  # 다르면 cnt 초기화
                    cnt = 1
            if cnt == K:  # 연속된 K개 찾으면 break
                break
        if cnt == K:  # 탐색한 column에서 연속 K개 찾으면 계속 진행
            continue
        return False  # 못 찾았으면 False return
    return True  # 반복문 모두 끝내면 모든 column이 연속된 K개 가지므로 True return


for tc in range(1, T + 1):
    D, W, K = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(D)]

    first_chk = chk(data)

    if first_chk:  # 시약 안 쓰고 통과하는 경우
        print("#{} {}".format(tc, 0))
    else:
        is_pass = False
        for i in range(1, D + 1):
            target_rows = list(combinations(range(D), i))  # 약품 넣어줄 row 조합 만들어주기

            for rows in target_rows:  # 조합 하나씩 탐색
                queue = deque()
                cnt = 0
                queue.append(data)  # 원본 데이터 큐에 넣고 시작

                for j in range(i):
                    for _ in range(
                        2 ** j
                    ):  # ex> 2줄의 경우, 한 줄을 0 1로 바꾸고 두가지 경우를 다시 0 0 / 0 1 / 1 0 / 1 1로 바꿔야 하므로
                        cur_data = queue.popleft()
                        new_data_1 = [
                            line[:] for line in cur_data
                        ]  # 큐에서 꺼낸 데이터 복사. deepcopy로 접근하면 35/50 시간초과
                        new_data_1[rows[j]] = [0] * W
                        queue.append(new_data_1)
                        new_data_2 = [line[:] for line in cur_data]
                        new_data_2[rows[j]] = [1] * W
                        queue.append(new_data_2)

                for new_data in queue:  # 큐에서 변경된 데이터 꺼내면서 통과되는 경우 있는지 탐색
                    if chk(new_data):
                        is_pass = True
                        break
                if is_pass:
                    break
            if is_pass:
                print("#{} {}".format(tc, i))
                break
