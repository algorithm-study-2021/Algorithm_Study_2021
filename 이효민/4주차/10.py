def solution(arr):
    answer = []
    
    answer.append(arr[0])
    num=arr[0]
    for i in range(1,len(arr)):
        if arr[i]==num:
            continue
        elif arr[i]!=num:
            answer.append(arr[i])
            num=arr[i]
    
    return answer
