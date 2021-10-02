ans = [False] * 10000

for x in range(10):
    for y in range(10):
        for z in range(10):
            for w in range(10):
                if 1001*x + 101*y + 11*z + 2*w > len(ans) - 1:
                    break
                ans[1001*x + 101*y + 11*z + 2*w] = True

for i in range(1, len(ans)):
    if ans[i] == False:
        print(i)