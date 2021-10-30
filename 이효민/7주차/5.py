def solution(word):
    answer = 0
    alpha={'A':1,'E':2,'I':3,'O':4,'U':5}
    gap=[780,155,30,5,0]
    
    word=list(word)
    for i in range(len(word),5):
        word.append("0")
    
    for j in range(0,len(word)):
        if word[j]=='0':
            continue
        else:
            answer+=(alpha[word[j]]+gap[j]*(alpha[word[j]]-1))
    
    return answer
