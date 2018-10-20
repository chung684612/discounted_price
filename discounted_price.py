while True:
    discounted_price = input('請輸入購物金額, 輸入0結束程式: ') 
    if discounted_price == '0':
        break
    else:
        discounted_price = float(discounted_price)        
        if discounted_price >= 100000:
            discounted_price *= 0.8
            print('\n', discounted_price, end = ' 元\n\n')
        elif discounted_price >= 50000 and discounted_price < 100000:
            discounted_price *= 0.85
            print('\n', discounted_price, end = ' 元\n\n')
        elif discounted_price >= 30000 and discounted_price < 50000:
            discounted_price *= 0.9
            print('\n', discounted_price, end = ' 元\n\n')
        else:
            discounted_price *= 0.95
            print('\n', discounted_price, end = ' 元\n\n')