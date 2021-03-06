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
