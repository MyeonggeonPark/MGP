def solution_a(arr):
    answer=0
    for num in arr:
        answer += num
    answer = answer / len(arr)
    return answer

#list sum을 활용
def average_b(arr):
    return (sum(arr) / len(arr))