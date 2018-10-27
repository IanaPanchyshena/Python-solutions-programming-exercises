# Sales Tax 2_6

def main():
    # ask user to enter the amount of purchase
    amount_purchase=float(input('Enter the amount of purchase: '))

    # calculate 1.state_tax, 2.county_tax, 3.total_salesTax, 4.total_sale
    state_tax=amount_purchase*0.05
    county_tax=amount_purchase*0.025
    total_salesTax=state_tax+county_tax
    total_sale=total_salesTax+amount_purchase

    # display result
    print('State Tax: $',format(state_tax,',.2f'),sep='')
    print('County Tax: $',format(county_tax,',.2f'),sep='')
    print('Tatal Sales Tax: $',format(total_salesTax,',.2f'),sep='')
    print('Total of the sale: $',format(total_sale,',.2f'),sep='')

main()
