def solution_my(absolutes, signs):
    return sum([x if y == 1 else x*-1 for x,y in zip(absolutes, signs)])

#true, false 이기때문에 바로 if에 넣을 수 있음

def solution_a(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))