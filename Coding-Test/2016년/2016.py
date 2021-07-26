def solution(a, b):
    answer = 0
    month = {0:0, 1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    days = 0
    for mon in range(a):
        days += month[mon]
    days += b + 5
    answer = days % 7
    return day[answer-1]

#range로 값을 구해오는 것보다 바로 index에 접근이 가능

def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]