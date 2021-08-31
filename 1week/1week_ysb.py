def solution(price, money, count):
    fee = 0
    for i in range(1, count + 1):
        fee += i * price

    if fee > money:
        return fee - money
    else:
        return 0
