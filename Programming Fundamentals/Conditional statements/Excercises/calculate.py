#product price
product_price = float(input())
#paid amount
paid_amount = float(input())

# change = (paid amount - product price) * 10
change = int((paid_amount - product_price) * 100)

if change >= 100:
    one_lev_coins = change // 100
    change -= one_lev_coins * 100
    print(f"{one_lev_coins} x 1 lev")
    
if change >= 50:
    fifty_coins = change // 50
   
    change -= fifty_coins * 50
    print(f"{fifty_coins} x 50 stotinki")

if change >= 20:
    twenty_coins = change // 20
   
    change -= twenty_coins * 20
    print(f"{twenty_coins} x 20 stotinki")
    
if change >= 10:
    ten_coins = change // 10
   
    change -= ten_coins * 10
    print(f"{ten_coins} x 10 stotinki")
    
if change >= 5:
    five_coins = change // 5
   
    change -= five_coins * 5
    print(f"{five_coins} x 5 stotinki")
    
if change >= 2:
    two_coins = change // 2
   
    change -= two_coins * 2
    print(f"{two_coins} x 2 stotinki")
    
if change >= 1:
    one_coins = change // 1
   
    change -= one_coins * 1
    print(f"{one_coins} x 1 stotinka")
