def solution(n):
    n_list=list(map(int,str(n)))
    n_list.sort(reverse=True)
    n_list=list(map(str,n_list))
    return int(''.join(n_list))
