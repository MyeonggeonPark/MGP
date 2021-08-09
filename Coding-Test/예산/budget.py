#시간 초과

def solution_my(d, budget):
    from itertools import combinations
    answer = 0
    for num in range(len(d)):
        for comb in combinations(d,num+1):
            if sum(comb) <= budget:
                if len(comb) >= answer:
                    answer = len(comb)
    return answer

#최대한 많은 부서에게 지원하는 부분이니까 합계보다는
#얼마나 많은 부서에 지원이 가능한가를 포인트로 잡고 고민하면
#쉽게 풀 수 있었던 문제

def solution_a(d, budget):
    d.sort()
    
    while budget < sum(d):
        d.pop()
    
    return len(d)