def solution(arr):
    num=len(arr) #원소의 개수
    sum=0; #배열의 합
    for i in range(0,num):
        sum+=arr[i]
    answer = sum/num
    return answer
