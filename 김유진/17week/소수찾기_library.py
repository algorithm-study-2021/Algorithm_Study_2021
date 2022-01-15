from itertools import permutations

def isPrime(num): #리스트에서 count를 수행 
    if num<=1: return False
    for i in range(2,num//2+1):
        if num%i==0: return False
    return True

def solution(numbers):
    count=0
    permutationList=[]
    permutationSet=set()

    #모든 순열 구하기
    for i in range(len(numbers)):
        permutationList.extend(permutations(numbers,i+1))
    
    permutationList=[''.join(i) for i in permutationList]

    #중복 제거
    for i in permutationList:
        permutationSet.add(int(i))
        
    for i in permutationSet:
        if isPrime(i): count+=1

    return count