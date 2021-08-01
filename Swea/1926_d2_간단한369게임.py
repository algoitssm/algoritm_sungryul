N = int(input())

total = list(map(str, range(1, N + 1)))
banned = ['3', '6', '9']
changed = []

for num in total:
    temp = ''
    for char in num:
        if char in banned:
            temp += '-'
    if temp:
        changed.append(temp)
    else:
        changed.append(num)

ans = ' '.join(changed)

print(ans)