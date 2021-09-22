import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    data = input()
    data += data  # 시작 위치를 바꿔가며 반복하기 위해 동일 문자열을 뒤에 붙여줌

    ans = []

    for i in range(N // 4):  # 시작위치를 i만큼 이동
        for j in range(0, N, N // 4):  # 4개의 면 중 더해줄 면을 j로 접근
            temp = int("0x" + data[i + j : i + j + N // 4], 16)  # 16진수 10진수로 변환
            if temp not in ans:  # 중복되지 않아야 하므로 해당 값 없을 때만 append
                ans.append(temp)

    ans.sort(reverse=True)  # 내림차순 정렬
    print("#{} {}".format(tc, ans[K - 1]))
