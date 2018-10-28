# Shipping_Charges3_13
# Shipping Company charges the following rates:
# Weight of Package Rate per Pound 2 pounds or less $1.50
# Over 2 pounds but not more than 6 pounds $3.00
# Over 6 pounds but not more than 10 pounds$4.00
# Over 10 pounds $4.75
# Write a program that asks the user to enter the weight of a package
# then displays the shipping charges.



def main():
    
    weight_packages=float(input('Enter the weight of a package in lb: '))
    
    if weight_packages >=0 and weight_packages<=2:
        price_charges=1.5
    elif weight_packages >=2 and weight_packages<=6:
        price_charges=3.00
    elif weight_packages >=6 and weight_packages<=10:
        price_charges=4.00
    else:
        price_charges=4.75

    shipping_charges=weight_packages*price_charges
    print('Shipping charges: $',format(shipping_charges,'.2f'),sep='')

main()
