def gcd(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

def solution(arr):
    
    for i in range(len(arr)-1):
        temp_gcd=gcd(arr[i],arr[i+1])
        #최소공배수 구하기
        arr[i+1]=(arr[i]*arr[i+1])/temp_gcd
        print(arr)        
    

    return arr[len(arr)-1]
