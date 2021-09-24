#연속되는 수는 한 번만, 이전 수 기억해야함

def solution(arr):
    i=0
    res=[]
    while(1):
        try:
            if arr[i]==arr[i+1]:
                i+=1
            else:
                res.append(arr[i])
                i+=1
        except:
            #i+1 범위 문제 
            res.append(arr[i])
            return res

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))