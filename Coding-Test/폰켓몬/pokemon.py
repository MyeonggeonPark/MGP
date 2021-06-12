#from itertools import combinations
#처음에는 combinations를 사용하여 직접적으로 집합을 만들어야한다고 생각
#하지만 원소의 개수만을 가지고 풀 수 있는 문제

def solution_my(nums):
    if len(set(nums)) >= len(nums)//2:
        answer = len(nums)//2
    else:
        answer = len(set(nums))
    return answer


#더욱 간결한 코드
def solution_a(nums):
    return min(len(set(nums)), len(nums)//2)