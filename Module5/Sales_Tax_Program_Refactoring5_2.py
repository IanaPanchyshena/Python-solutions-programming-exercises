# Sales_Tax_Program_Refactoring5_2

rate_state_tax=0.05
rate_county_tax=0.025

def main():
    # ask user to enter the amount of purchase
    amount_purchase=float(input('Enter the amount of purchase: '))

    # calculate 1.state_tax, 2.county_tax, 3.total_salesTax, 4.total_sale
    state_tax=get_state_tax(amount_purchase)
    county_tax=get_county_tax(amount_purchase)
    total_tax=get_total_tax(state_tax,county_tax)
    total_sales=get_total_sales(amount_purchase,total_tax)

    # display result
    print('State Tax: $',format(state_tax,',.2f'),sep='')
    print('County Tax: $',format(county_tax,',.2f'),sep='')
    print('Tatal Sales Tax: $',format(total_tax,',.2f'),sep='')
    print('Total of the sale: $',format(total_sales,',.2f'),sep='')


def get_state_tax(amount_purchase):
    return amount_purchase*rate_state_tax
    
def get_county_tax(amount_purchase):
    return amount_purchase*rate_county_tax

def get_total_tax(state_tax, county_tax):
    return state_tax+county_tax

def get_total_sales(amount,tax):
    return amount+tax

main()
