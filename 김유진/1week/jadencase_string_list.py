"""
고려사항)
공백 고려. -> 문자로 들어가는 것은 아니지만 지워서도 안됨. 
ex)     ek =      Ek 와 같이 표현 
"""

def solution(s):
    answer = ''
    word=s.split(' ')
    for i in word:
        if i=='':
            answer+=' '
        else:
            answer+=i[0].upper()+i[1:].lower()+' '

    return answer[:-1]
