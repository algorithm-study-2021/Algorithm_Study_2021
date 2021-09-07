def solution(n):
    n_str=str(n)
    answer=0
    for i in n_str:
        answer+=int(i)
    return answer