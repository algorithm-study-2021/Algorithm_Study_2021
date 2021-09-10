#가정: A 배열에서 최소값, B 배열에서 최대값을 각자 찾아서 더하면 최소값일 것이다
def solution(A,B):
    ar_len=len(A)
    answer = 0
    
    A.sort()
    B.sort(reverse=True)
    
    for i in range(0,ar_len):
        answer+=A[i]*B[i]
    
    return answer

#1. 효율성 테스트 실패(A에서 최솟값, B에서 최대값 찾기)
#각 배열에서 최소값과 최대값을 찾는 과정이 너무 오래걸림
#=> A와 B를 각자 오름차순, 내림차순으로 바꿔서 곱하기
