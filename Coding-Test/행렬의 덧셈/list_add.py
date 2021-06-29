def solution(arr1, arr2):
    answer = []
    for idx_a in range(len(arr1)):        
        answer.append([arr1[idx_a][idx_b] + arr2[idx_a][idx_b]for idx_b in range(len(arr1[idx_a]))])
    return answer