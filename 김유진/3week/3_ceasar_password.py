def ceaser(word,offset):
    #소문자 변환
    if word<='Z':
        if ord(word)+offset>=91:
            offset_2nd=offset-91+ord(word)
            return ord('A')+offset_2nd
        else: return ord(word)+offset
    
    else:
        if word<='z':
            if ord(word)+offset>=123:
                offset_2nd=offset-123+ord(word)
                return ord('a')+offset_2nd
            else: return ord(word)+offset


def solution(s,n):
    words=s.split(' ')
    answer=''

    for i in words:
        if len(i)>=2:
            print(i)
            for j in i:
                answer+=chr(ceaser(j,n))
            answer+=' '

        else:
            if i!='':
                answer+=chr(ceaser(i,n))+' '
            else:
                answer+=' '

    return answer[:-1]
