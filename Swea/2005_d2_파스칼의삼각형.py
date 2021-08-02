T = int(input())

def triangle(num):
    ans = [[1]]

    if num == 1:
        return ans

    for i in range(1, num):
        temp = []
        for j in range(i + 1):
            # try/except 구문으로 IndexError일 때 예외처리 해보려 했으나, 첫 번째 인자의 경우 -1이 오류에 해당하지 않아 불가
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(ans[i-1][j-1] + ans[i-1][j])
        ans.append(temp)
    return ans

    return ans

for i in range(T):
    N = int(input())

    ans = triangle(N)

    print(f'#{i+1}')
    for line in ans:
        print(' '.join(map(str, line)))