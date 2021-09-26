import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline


def cnt_cousin(parent_sibling):
    global data_idx, k_cousin
    cnt = 0  # 사촌 명 수 세어줄 변수
    for _ in range(parent_sibling):
        temp = []  # 형제 담을 임시 변수
        k_brother = 0  # k의 형제인지 여부
        brother_cnt = 0  # 형제 명 수 세어줄 변수
        while data_idx < n:
            if not temp:  # temp 비어있으면 append하면서 명 수 늘려줌
                temp.append(data[data_idx])
                brother_cnt += 1
                cnt += 1
            else:
                if temp[-1] + 1 == data[data_idx]:  # temp 마지막 값에서 +1 한 값이면 명 수 늘려줌
                    temp.append(data[data_idx])
                    brother_cnt += 1
                    cnt += 1
                else:  # +1 한 값 아니면 break
                    break
            if data[data_idx] == k:  # k 만나면 k_cousin, k_brother True로 바꿔줌
                k_cousin = 1
                k_brother = 1
            data_idx += 1
        if k_brother:
            cnt -= brother_cnt

    return cnt


while True:
    n, k = map(int, input().split())
    if not n:
        break
    data = list(map(int, input().split()))

    data_idx = 1  # data에 접근할 인덱스
    k_cousin = 0  # k의 사촌인지 여부
    parent_sibling = 1  # 부모의 형제 포함 사촌 명 수

    while True:
        sibling = cnt_cousin(parent_sibling)
        if k_cousin:  # k의 사촌이면
            print(sibling)
            break
        parent_sibling = sibling  # k의 사촌 아니면 인자 갱신하여 다시 함수 실행
