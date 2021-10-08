def solution(price, money, count):
    allPrice=0;
    for i in count:
        allPrice+=price*i

    if money-allPrice<0: return abs(money-allPrice)
    else: return 0