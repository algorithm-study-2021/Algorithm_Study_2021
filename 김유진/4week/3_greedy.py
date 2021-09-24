#탐욕적 기법으로 시행

def searchIn(arr,j):
    max=0
    maxj=0
    for c in range (len(arr)):
        if c!=j and max<arr[c]:
            max=arr[c]
            maxj=c
    return max,maxj
            
def solution(land):
    i=0; j=0
    answer=0
    #내려가면서 탐색 (같은 열 조심)
    while(i<len(land)):
        addVal,j=searchIn(land[i],j)
        answer+=addVal
        i+=1

    return answer