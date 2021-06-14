def solution_my_failure(board, moves) :
    answer = 0
    double = []
    basket = []
    for a_move in moves :
        zeros = board[a_move-1].count(0)
        for _ in range(zeros):
            board[a_move-1].remove(0)
        for idx, double_num in enumerate(board[a_move-1]):
            double = []
            if idx != 0 :
                if board[a_move-1][idx-1] == board[a_move-1][idx] :
                    double.append(board[a_move-1][idx])
        for num in double:
            board[a_move-1].remove(num)
            board[a_move-1].remove(num)
        if len(board[a_move-1]) != 0 :
            basket.append(board[a_move-1][len(board[a_move-1])-1])
            del board[a_move-1][len(board[a_move-1])-1]
    for idx, double_num in enumerate(basket) :
        if idx != 0 :
            if basket[idx-1] == basket[idx] :
                answer += 2
    return answer

#일단 본인의 첫째 고전의 원인은 list를 0으로 만들려고 함
#인터넷으로 설명을 찾아본 결과 스텍구조를 고려해야하는데, 전혀 그런것 생각하지 않음
#문제를 읽으면서 어디가 위이고 어디가 아래 인가를 고민했는데, 그럴 필요없이 index 순서데로 생각했어야함
#board에 중복되는 인형을 지우는 코드가 없다.(차원을 맞게 그렸으면 중복을 생각 할 필요가 없다.)
#board의 차원을 전혀 잘 못 생각했다.

board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]

board[3][0]

def solution_my_final(board, moves):
    answer = 0
    basket = []
    for i in moves :
        #n X n 구조이기 때문에, board를 len로 잡아서 인덱스를 반환 가능
        #j가 행으로 접근, i-1이 열에 접근
        for j in range(len(board)) :
            if board[j][i-1] == 0 :
                #pass 코드는 더 이상 실행할 코드가 없음
                pass
            else :
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                #break loop를 빠져나감
                break
        if len(basket) >= 2 and basket[len(basket)-1] == basket[len(basket)-2]:
            basket.pop(-1)
            basket.pop(-1)
            answer += 2
    return answer