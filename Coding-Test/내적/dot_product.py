def solution_my(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

def solution_a(a, b):
    #zip을 사용하여 a,b를 iterator로 만들어 줌
    return sum([x*y for x, y in zip(a,b)])