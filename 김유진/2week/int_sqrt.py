def solution(n):
    num=1
    while 1:
        if num*num>n:
            return -1
        if num*num==n:
            return (num+1)*(num+1)
        num+=1
