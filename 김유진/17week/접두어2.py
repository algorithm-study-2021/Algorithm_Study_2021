#효율성 문제-> 중첩 for문

def solution(phone_book):
    #phone_book.sort(key=lambda x:len(x))
    #str로 정렬을 시도하면 길이, 문자의 값을 모두 고려하여 계산할 수 있음 
    #str로 정렬한 후, 뒤에서 앞을 비교하면 됨 (앞->문자의 길이가 작거나 같거나 문자가 작거나 같거나 )

    phone_book.sort()
    for i in range(1,len(phone_book)):
        length=len(phone_book[i-1])
        if phone_book[i-1]==phone_book[i][:length]: return False
    
    return True