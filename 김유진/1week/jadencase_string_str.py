"""
모든 단어의 첫 글자가 대문자
공백 고려 -> 공백을 삭제하면 안 됨.
"""
def solution(s):
    words=s.split(' ') #공백을 기준으로 분할 (빈 문자열이 포함 됨)

    answer=[w[0].upper()+w[1:].lower()+' ' if w!='' else ' ' for w in words]

    return ''.join(answer)[:-1] #문자열로 반환하기 위함 

val=input()
print(solution(val))