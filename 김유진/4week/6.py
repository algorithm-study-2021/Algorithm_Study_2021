def solution(arr, divisor):
    
    newList=[]
    for i in range(len(arr)):
        if arr[i]%divisor==0:
            newList.append(arr[i])
    newList.sort()
    
    if len(newList)==0: return [-1]
    return newList
