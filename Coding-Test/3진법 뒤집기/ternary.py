def solution_my(n):
    import math
    answer = 0
    share = 1 
    num_three = []
    while share != 0:
        if len(num_three) == 0:
            share = n // 3
            num_three.insert(0, n % 3)
        else:
            num_three.insert(0, share % 3)
            share = share // 3
    num_three.reverse()
    for idx in range(len(num_three)):
        answer += num_three[idx] * math.pow(3,len(num_three)-(idx+1))
    return answer


def solution_a(n):
    #string 으로 선언
    tmp = ''
    #숫자의 형태로 선언하지 않고 n으로 정하여 0(false)으로 만들기
    while n:
        #입력 할 때부터 거꾸로 이기 때문에 reverse가 불필요
        tmp += str(n % 3)
        n = n // 3
    
    #int의 새로운 기능
    answer = int(tmp, 3)
    return answer