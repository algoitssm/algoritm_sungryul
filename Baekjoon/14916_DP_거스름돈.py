n = int(input())

result = [-1] * (n+1)

for i in range(1, n+1):
    if i % 5 == 0:
        result[i] = i // 5
    elif (i - (i//5) * 5) % 2 == 0 and i > 5:   # i > 5 조건 없으면 오답!
        result[i] = i // 5 + (i - (i//5) * 5) // 2
    elif (i - (i//5 - 1) * 5) % 2 == 0 and i > 5:
        result[i] = i // 5 - 1 + (i - (i//5 - 1) * 5) // 2
    elif i % 2 == 0:
        result[i] = i // 2
    
print(result[n])