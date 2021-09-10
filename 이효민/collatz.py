def solution(num):
    answer = 0
    while num!=1:
        if answer>=500: #500번 반복해도 1이 안된다면 -1 반환
            return -1
        else:
            if num%2==0: #짝수인 경우: 2로 나눔
                num//=2
            else: #홀수인 경우: 3 곱하고 1 더함
                num=num*3+1
            answer+=1 #동작을 한 번 수행할 때마다 1번씩 추가
    return answer
