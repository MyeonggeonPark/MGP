def solution_my(numbers, hand) :
    answer = []
    numbers_matrix = {1:(0,0), 2:(0,1), 3:(0,2), 
                      4:(1,0), 5:(1,1), 6:(1,2),
                      7:(2,0), 8:(2,1), 9:(2,2),
                      0:(3,1)}
    r_h = (3,2)
    l_h = (3,0)
    
    for idx,num in enumerate(numbers):
        #print(l_h,r_h,answer)
        if num in [1,4,7]:
            answer.append('L')
            l_h = numbers_matrix[num]
        elif num in [3,6,9]:
            answer.append('R')
            r_h = numbers_matrix[num]
        elif num in [2,5,8,0]:
            if ((r_h[1]==2)*(l_h[1]==0)):
                if abs(numbers_matrix[num][0]-l_h[0]) < abs(numbers_matrix[num][0]-r_h[0]):
                    answer.append('L')
                    l_h = numbers_matrix[num]
                elif abs(numbers_matrix[num][0]-l_h[0]) > abs(numbers_matrix[num][0]-r_h[0]):
                    answer.append('R')
                    r_h = numbers_matrix[num]
                elif abs(numbers_matrix[num][0]-l_h[0]) == abs(numbers_matrix[num][0]-r_h[0]):
                    if hand == 'left':
                        answer.append('L')
                        l_h = numbers_matrix[num]
                    else:
                        answer.append('R')
                        r_h = numbers_matrix[num]
            else:
                if l_h[1]==1:
                    if abs(numbers_matrix[num][0]-l_h[0]-1) < abs(numbers_matrix[num][0]-r_h[0]):
                        answer.append('L')
                        l_h = numbers_matrix[num]
                    elif abs(numbers_matrix[num][0]-l_h[0]-1) > abs(numbers_matrix[num][0]-r_h[0]):
                        answer.append('R')
                        r_h = numbers_matrix[num]
                    elif abs(numbers_matrix[num][0]-l_h[0]-1) == abs(numbers_matrix[num][0]-r_h[0]):
                        if hand == 'left':
                            answer.append('L')
                            l_h = numbers_matrix[num]
                        else:
                            answer.append('R')
                            r_h = numbers_matrix[num]
                elif r_h[1]==1:
                    if abs(numbers_matrix[num][0]-l_h[0]) < abs(numbers_matrix[num][0]-r_h[0]-1):
                        answer.append('L')
                        l_h = numbers_matrix[num]
                    elif abs(numbers_matrix[num][0]-l_h[0]) > abs(numbers_matrix[num][0]-r_h[0]-1):
                        answer.append('R')
                        r_h = numbers_matrix[num]
                    elif abs(numbers_matrix[num][0]-l_h[0]) == abs(numbers_matrix[num][0]-r_h[0]-1):
                        if hand == 'left':
                            answer.append('L')
                            l_h = numbers_matrix[num]
                        else:
                            answer.append('R')
                            r_h = numbers_matrix[num]
    
    return ''.join(answer)

#거리 구하는 방법을 하나의 함수 안에 녹이려고 했으나
#따로 정의 하는 것이 편리
def get_distance(keypad, finger_position, next_number):
    next_number_position = keypad[next_number]
    distance = abs(finger_position[0] - next_number_position[0]) + abs(finger_position[1] - next_number_position[1])
    return distance

def solution_a(numbers, hand):
    result = ''
    #키패드를 좌표로 정의
    keypad = { 1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2], 0: [3, 1] }
    
    #손가락에 따른 숫자 위치 리스트 만들기
    left_finger_numbers = [1, 4, 7]
    right_finger_numbers = [3, 6, 9]
    #변수가 되는 부분
    center_finger_numbers = [2, 5, 8, 0]
    #처음 시작할 때 손가락의 위치
    left_finger_position = [3, 0]
    right_finger_position = [3, 2]
    
    for number in numbers:
        if number in left_finger_numbers:
            result += 'L'
            left_finger_position = keypad[number]
        elif number in right_finger_numbers:
            result += 'R'
            right_finger_position = keypad[number]
        else:
            #오른쪽 왼쪽의 거리를 측정
            left_finger_distance = get_distance(keypad, left_finger_position, number)
            right_finger_distance = get_distance(keypad, right_finger_position, number)
            if left_finger_distance > right_finger_distance:
                result += 'R'
                right_finger_position = keypad[number]
            elif left_finger_distance < right_finger_distance:
                result += 'L'
                left_finger_position = keypad[number]
            elif left_finger_distance == right_finger_distance:
                #upper 좋은 아이디어
                result += hand[0].upper()
                if hand == 'right':
                    right_finger_position = keypad[number]
                elif hand == 'left':
                    left_finger_position = keypad[number]
    return result