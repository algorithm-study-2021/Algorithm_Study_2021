def solution(s):
    answer = []
    rem=0
    c=0
    while s!='1':
        num=s.count("1")
        rem+=s.count("0")
        s=str(format(num,'b'))
        c=c+1
    answer.append(c)
    answer.append(rem)
    
    return answer
#1. 1의 개수를 num에 추가, num을 2진수로 변환해서 길이 s에 저장
#c에 변환하는 횟수 저장
