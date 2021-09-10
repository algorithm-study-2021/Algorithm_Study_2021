def solution(s):
    s=s.split(" ") #문자열 s를 문자 리스트로 변환
    new_s=list(map(int,s)) #문자 리스트를 정수 리스트로 변환
    
    answer = str(min(new_s))+" "+str(max(new_s))
    
    return answer

# 1. 문자 리스트 상태로 바로 min(), max()로 구하려고 함
# => 음수는 구분할 수 없었음
# 2. 문자 리스트를 정수 리스트로 변환한 후, 나중에 answer을 구할 때 다시 정수로 변환해줌
