def solution_my(left, right):
    answer = 0
    for num_a in range(left, right+1):
        #약수의 개수를 구하기 위해 list 생성
        num_list=[]
        for num_b in range(1,num_a+1):
            if num_a % num_b == 0:
                num_list.append(num_b)
        if len(num_list) % 2 == 0:
            answer += num_a
        else:
            answer -= num_a
    return answer


def solution_a(left, right):
    answer = 0
    for i in range(left,right+1):
        #제곱수는 약수의 개수가 홀수
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

def solution_b(left, right):
    return sum([-n if int(n ** 0.5) == n ** 0.5 else n for n in range(left, right+1)])