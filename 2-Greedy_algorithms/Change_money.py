def change_money(money):
    coins=[10,5,1]
    count=0

    for coin in coins:
        count += money//coin
        money=money%coin
    return count

if __name__=="__main__":
    money=int(input())
    print(change_money(money))