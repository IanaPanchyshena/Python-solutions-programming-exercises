# Insurance5_3

# Many financial experts advise that property owners should
# insure their homes or buildings for at least 80 percent of the amount
# it would cost to replace the structure.
# Write a program that asks the user to enter the replacement cost
# of a building, then displays the minimum
# amount of insurance he or she should buy for the property.


def main():
    cost_replacement=float(input('Enter the replacement cost of a building: '))

    amount_insurance=get_amount_insurance(cost_replacement)
    print('Amount of insurance you should buy for the property: $',
          amount_insurance)

def get_amount_insurance(cost):
    return cost*0.8
    
    
main()
