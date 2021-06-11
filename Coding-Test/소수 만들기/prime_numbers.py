from itertools import combinations

def solution(nums):
    answer = 0
    #combinations 함수를 사용하여 숫자를 세개씩 조합한 리스트 생성
    comb_list = combinations(nums,3)
    sum_list=[]
    for list_a in comb_list:
        sum_list.append(sum(list_a))
    
    #2이상 이고 본인 보다 작은 수로 나워지는 숫자 탐색
    for num in sum_list:
        prime_number_false = 0
        for div_num in range(2,num):
            if num % div_num == 0:
                prime_number_false += 1
        if prime_number_false == 0:
            answer +=1
            
    return answer