def solution_a(n, m):
    answer = []
    num_n=[]
    num_m=[]
    for a in range(1,n+1):
        if n%a==0:
            num_n.append(a)
    for b in range(1,m+1):
        if m%b==0:
            num_m.append(b)
    for a in sorted(num_n,reverse=True):
        if a in num_m:
            answer.append(a)
            break
    num_a=0
    num_b=0
    if n >= m:
        num_a=n
        num_b=m
    else:
        num_b=n
        num_a=m
    for b in range(num_a,(num_a*num_b)+1):
        if (b%n==0)&(b%m==0):
            answer.append(b)
            break
    return answer

#유클리드 호제법 이용
def solution_b(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer