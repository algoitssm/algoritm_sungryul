# 괄호 없는 +, -로 이루어진 수식에 괄호 넣어서 결과값 최소로 만드는 문제
#
og = input()

# 첫 번째 풀이
# new_str에 og의 문자 하나씩 넣어주면서
# new_str의 마지막 문자가 -이면 괄호 삽입
# og의 i 번째 문자가 -이면 앞쪽 괄호 닫아주며 new_str에 - 삽입
# 이외의 경우 바로 new_str에 og[i] 삽입
# 문제점: 숫자가 0으로 시작하는 경우 eval에서 계산 불가

# new_str = og[0]
# temp = []

# for i in range(1, len(og)):
#     if new_str[-1] == '-':
#         new_str += '(' + og[i]
#         temp.append('(')
#         continue
#     if og[i] == '-' and temp:
#         new_str += ')' + og[i]
#         temp.pop()
#         continue
#     new_str += og[i]


# if temp:
#     new_str += ')'

# print(eval(new_str))

# 두 번째 풀이
ans = 0
# 입력받은 문자열을 - 기준으로 split
minus_split = og.split("-")
# split한 문자열 중 첫번째는 더해주고 나머지는 다 빼기
for i in range(len(minus_split)):
    # 숫자로 만들어주기 위해 + 기준으로 split
    plus_split = list(map(int, minus_split[i].split("+")))
    if i == 0:
        ans += sum(plus_split)
    else:
        ans -= sum(plus_split)
print(ans)
