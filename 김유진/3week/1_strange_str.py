def alphabet_sol(s):
    answer=''
    for i in range(len(s)):
        if i%2==0:
            answer+=s[i].upper()
        else: answer+=s[i].lower()
        
    return answer

def solution(s):
    s_list=s.split(' ')
    answer=[alphabet_sol(i)+' ' if i!='' else ' ' for i in s_list]
    print(answer)
    return ''.join(answer)[:-1]

