from math import gcd

def solution(arr):
    
    for i in range(len(arr)-1):
        temp_gcd=gcd(arr[i],arr[i+1])
        #최소공배수 구하기
        arr[i+1]=int((arr[i]*arr[i+1])/temp_gcd)       

    return arr[len(arr)-1] 

print(solution([2,6,8,14]))