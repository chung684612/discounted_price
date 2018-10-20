while True:
    discounted_price = input('請輸入購物金額, 輸入0結束程式: ') 
    if discounted_price == '0':
        break
    else:
        discounted_price = float(discounted_price)        
        if discounted_price >= 100000:
            discounted_price *= 0.8
            print(discounted_price)
        elif discounted_price >= 50000 and discounted_price < 100000:
            discounted_price *= 0.85
            print(discounted_price)
        elif discounted_price >= 30000 and discounted_price < 50000:
            discounted_price *= 0.9
            print(discounted_price)
        else:
            discounted_price *= 0.95
            print(discounted_price)