def solution_my(array, commands):
    answer = []

    #list의 index 고르는 방법만 고려하면 쉽게 풀 수 있음
    #list의 번호가 0부터 시작하는 것
    #list[a:b] a 이상, b는 미만
    for i in commands:
        temp = array[i[0]-1:i[1]]
        #sort()는 새로 변수에 할당해주지 않아도 바로 리스트에 반영
        temp.sort()
        answer.append(temp[i[2]-1])

    return answer



def solution_a(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))


def solution_b(array, commands):
    answer = []
    #sorted 사용, 세개의 변수를 각각의 문자에 할당
    for i,j,k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer