## ✅1343

- 통과 코드

``` python
board = input()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    print(board)
```

- 의문 코드 ➡ 해결!

```python
board = input()

cnt = 0
result = []

if len(board) <= 1:
    # 입력 '.'일 경우가 마지막 테스트 케이스
    if board == ".":  # 길이가 1이하일 때 무조건 -1 하려다가 계속 오답...
        print(".")
    else:
        print(-1)

else:
    for char in board:
        if char == 'X':
            cnt += 1
            if cnt == 2:
                result.append(poly[1])
            if cnt == 4:
                result[-1] = poly[0]
                cnt = 0
        else:
            if cnt % 2:
                result = -1
                break
            else:
                cnt = 0
                result.append('.')
    
    if result == -1:
        print(result)
    elif cnt == 1 or cnt == 3:
        print(-1)
    else:
        print(''.join(result))
```
