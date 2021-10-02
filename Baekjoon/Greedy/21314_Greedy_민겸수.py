"""
M과 K로 이루어진 민겸수를 입력받아 십진수로 변환하여,
그 중 최대값과 최소값을 구하는 문제
"""

# 최소값의 경우, K는 5, M은 붙어있는 만큼 10의 제곱
def min_val(nums):
    new_nums = ""
    cnt = 0  # M 개수 세기 위한 변수

    for num in nums:
        if num == "M":
            cnt += 1
        else:
            if cnt:
                new_nums += str(10 ** (cnt - 1))
            new_nums += "5"
            cnt = 0
    # 끝이 M으로 끝나는 경우, 10의 제곱으로 더함
    if cnt:
        new_nums += "1" + "0" * (cnt - 1)

    return new_nums


# 최대값의 경우, K 앞에 M의 개수만큼 5 뒤 0을 붙임
def max_val(nums):
    new_nums = ""
    cnt = 0  # M 개수 세기 위한 변수

    for num in nums:
        if num == "M":
            cnt += 1
        else:
            new_nums += "5" + "0" * cnt
            cnt = 0
    # 끝이 M으로 끝나는 경우, 그 개수만큼 1을 더함
    if cnt:
        new_nums += "1" * cnt

    return new_nums


minkyum = input()

print(max_val(minkyum))
print(min_val(minkyum))
