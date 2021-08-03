T = int(input())

for tc in range(1, T+1):
    N = int(input())
    distance = 0
    velocity = 0
    for i in range(N):
        command = tuple(map(int, input().split()))
        if command[0] == 1:
            velocity += command[1]
            distance += velocity
        elif command[0] == 0:
            distance += velocity
        else:
            velocity -= command[1]
            if velocity < 0:
                velocity = 0
            distance += velocity
    print(f'#{tc} {distance}')