def win(num):
    win_lotto = 0
    if num == 6 :
        win_lotto = 1
    elif num == 5 :
         win_lotto = 2
    elif num == 4 :
         win_lotto = 3
    elif num == 3 :
        win_lotto = 4
    elif num == 2 :
        win_lotto = 5
    else :
        win_lotto = 6
    return win_lotto

def solution_my(lottos, win_nums):
    zeors = lottos.count(0)
    win_second = 0
    for num in lottos:
        if num != 0:
            if num in win_nums:
                win_second += 1
    answer = [win(win_second+zeors),win(win_second)]
    return answer

#list.count를 사용
#index를 사용하여 rank 반환
def solution_a(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]