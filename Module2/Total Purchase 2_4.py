# Total Purchase 2_4

def main():
    #get price for each of 5 items
    item1=float(input('Enter the price for item1 '))
    item2=float(input('Enter the price for item2 '))
    item3=float(input('Enter the price for item3 '))
    item4=float(input('Enter the price for item4 '))
    item5=float(input('Enter the price for item5 '))

    #calculate subtotal of 5 items
    subtotal=item1+item2+item3+item4+item5

    #calculate tax susbtotal*0.07
    tax=subtotal*0.07

    #calculate total subtotal+tax
    total=subtotal+tax

    #print result 
    print('Subtotal: $',format(subtotal,'.2f'),sep='')
    print('Tax: $',format(tax,'.2f'),sep='')
    print('Total: $',format(total,'.2f'),sep='')


main()
