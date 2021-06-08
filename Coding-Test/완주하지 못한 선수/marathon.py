def solution(participant, completion):
    #딕셔너리 자료형 선언
    answer={}
    #참가한 인원은 key 값(이름), value 값(1)
    for i in participant:
        answer[i] = answer.get(i,0) + 1
    #완주한 인원은 value 값(0)
    for i in completion:
        answer[i] -= 1
    #완주하지 못 한 인원의 value 값만 1,
    #따라서 if 문에서 true 로 value 값이 1인 인원이 출력
    for person in answer:
        if answer[person] :
            return person