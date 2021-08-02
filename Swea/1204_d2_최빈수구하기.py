T = int(input())

case_lst = []

for i in range(T):
    case_num = int(input())
    case_lst.append(list(map(int, input().split())))

def find_max_score(score_lst, total_lst):
    max_score = 0
    count = 0
    for score in score_lst:
        if count <= total_lst.count(score):
            max_score = score
            count = total_lst.count(score)
    return max_score

for idx, case in enumerate(case_lst, start = 1):
    score_list = list(set(case))
    score_list.sort()
    print(f'#{idx} {find_max_score(score_list, case)}')