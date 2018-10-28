# TipTaxTotal 2_8

def main():
    
    # get the price for meal, assign to price_meal
    price_meal=float(input('Enter the price for meal: '))
    
    # calculate amount of tip - price_meal*0.08
    # calculate tax - price_meal*0.07
    # calculate total_amount - price_meal+tip+tax
    tip=price_meal*0.08
    tax=price_meal*0.07
    total_amount=price_meal+tip+tax
    
    # display - Price for meal, Tip, Tax, Total amount
    print('Tip 8%: $',format(tip,'.2f'),sep='')
    print('Tax: $',format(tax,'.2f'),sep='')
    print('Total amount: $',format(total_amount,'.2f'),sep='')

main()
