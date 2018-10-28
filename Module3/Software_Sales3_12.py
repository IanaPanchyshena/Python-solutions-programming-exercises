# Software_Sales3_12

# A software company sells a package that retails for $99.
# Quantity discounts are given according to the following table:
# Quantity Discount 10–19 10% 20–49 20% 50–99 30% 100 or more40%
# Write a program that asks the user to enter the number of packages purchased.
# The program should then display the amount of the discount (if any)
# and the total amount of the purchase after the discount.

def main():
    
    number_purchased=int(input('Enter the number of packages purchased: '))
    price=99
    
    if number_purchased>=10 and number_purchased<=19:
        discount=price*0.1
    elif number_purchased>=20 and number_purchased<=49:
        discount=price*0.2
    elif number_purchased>=50 and number_purchased<=99:
        discount=price*0.3
    else:
        discount=price*0.4
              
    total_amount=price*number_purchased-discount

    print('Discount % ',format(discount,'.2f'),sep='')
    print('Total amount after discount $',format(total_amount,'.2f'),sep='')

main()
