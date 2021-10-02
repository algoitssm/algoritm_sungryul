"""
푼 문제는 파란색(B), 못 푼 문제는 빨간색(R)로 칠하면서
색을 칠하는 횟수를 최소로 만드는 문제
핵심은 문자열에서 연속되는 문자를 하나로 줄여 중복을 없애고
많은 색을 한번에 칠하고, 적은 색의 갯수만큼 더해주면 끝
"""
import sys

N = int(sys.stdin.readline())

data = sys.stdin.readline()

new_data = data[0]

for i in range(1, len(data)):
    if new_data[-1] == data[i]:
        continue
    new_data += data[i]

cnt = [new_data.count("B"), new_data.count("R")]

ans = 1 + min(cnt)
print(ans)
