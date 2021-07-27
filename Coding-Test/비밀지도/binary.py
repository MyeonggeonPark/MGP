def solution_my(n, arr1, arr2):
    answer = ""
    remain = 0
    number = 0
    num_list_a=[]
    num_list_b=[]

    for num in arr1:
        if num != 1:
            number = num
            while number // 2 >= 1:
                remain = number % 2
                number = number // 2
                answer = str(remain) + answer
                if number < 2 :
                    answer = str(number) + answer
        else:
            answer = "1"
        while len(answer) < n:
            answer = str(0) + answer
        num_list_a.append(answer)
        answer = ""

    for num in arr2:
        if num != 1:
            number = num
            while number // 2 >= 1:
                remain = number % 2
                number = number // 2
                answer = str(remain) + answer
                if number < 2 :
                    answer = str(number) + answer
        else:
            answer = "1"
        while len(answer) < n:
            answer = str(0) + answer
        num_list_b.append(answer)
        answer = ""

    answer_final = []

    for idx_a in range(len(arr1)):
        and_list= ''
        for idx_b in range(len(arr2)):
            if  num_list_a[idx_a][idx_b] == '1' or num_list_b[idx_a][idx_b] == '1':
                and_list += '#'
            else:
                and_list += ' '
        answer_final.append(and_list)

    return answer_final

#%%
#2진수 : bin
#8진수 : oct
#16진수 : hex
# |(or) 사용하여 1이 한번이라도 등장하면 1로 출력

def solution_a(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
