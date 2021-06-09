def solution_a(answers):
    scores = [0, 0, 0]
    answer = []
    
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    #index를 사용하여 값에 접근
    # % 연산자를 사용하여 pattern 값에 접근
    # index로 접근하는 값과 나머지의 값이 같다
    for i in range(len(answers)):
        if answers[i] == pattern1[i % len(pattern1)]:
            scores[0] += 1
        if answers[i] == pattern2[i % len(pattern2)]:
            scores[1] += 1
        if answers[i] == pattern3[i % len(pattern3)]:
            scores[2] += 1

    #가장 많이 정답을 맞춘 인원을 오름차순으로 나타내어야 한다
    #이미 score에서 부터 오름차순으로 배열하였기 때문에
    #따로 answer list를 sort 해 줄 필요가 없다.
    max_score = max(scores)
    for i in range(3):
        if scores[i] == max_score:
            answer.append(i + 1)

    return answer


def solution_b(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    #위의 연산과는 다르게 enumerate를 통하여 값과 index를 함께 반환
    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result