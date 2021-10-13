## ✅2448

- 풀이 코드

```python
import math


def make_star(shift):
    for i in range(len(stars)):
        stars.append(stars[i] + " " + stars[i])
        stars[i] = " " * shift + stars[i] + " " * shift


N = int(input())
k = int(math.log(N // 3, 2))

stars = ["  *  ", " * * ", "*****"]

for i in range(k):
    make_star(2 ** i * 3)

for star in stars:
    print(star)
```

- 풀이 방법(구글링...)
  - 기본 단위를 만들어두고 오른쪽으로 얼마나 빈 공간을 둬야하는지 계산