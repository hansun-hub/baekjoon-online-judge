def solution(n):
    sum=0
    if n%2==0:
        for i in range(n,0,-1):
            if i%2==0:
                sum+=i*i
    else:
        for i in range(n,0,-1):
            if i%2 !=0:
                sum+=i
    return sum