def checkBinary(a,b):
    abin=bin(a)
    bbin=bin(b)
    
    oneina=0; oneinb=0
    for i in abin:
        if i=='1':
            oneina+=1
    for i in bbin:
        if i=='1':
            oneinb+=1
    
    return oneina==oneinb

def solution(n):
    num=n
    while(1):
        if num>n and checkBinary(num,n):
            return num
        num+=1