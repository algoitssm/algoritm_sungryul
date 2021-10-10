import sys

sys.stdin = open("input.txt")

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def install(r, c, city):
    global ans
    for K in range(N + 1, 0, -1):
        secured_house = 0
        price = 0
        for i in range(-(K - 1), K):
            for j in range(-(K - 1) + abs(i), K - abs(i)):
                price += 1
                if 0 <= r + i < N and 0 <= c + j < N:
                    if city[r + i][c + j] == 1:
                        secured_house += 1

                if price > max_price:
                    break
            if price > max_price:
                break
        if price > max_price:
            continue

        if price <= secured_house * M:
            if ans < secured_house:
                ans = secured_house
            break


for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N:도시 크기  M:개당 지불비용

    cnt_house = 0
    city = []

    for row in range(N):
        data = list(map(int, input().split()))
        city.append(data)
        for col in range(N):
            if data[col]:
                cnt_house += 1

    max_price = cnt_house * M

    ans = 0
    for r in range(N):
        for c in range(N):
            install(r, c, city)

    print("#{} {}".format(tc, ans))
