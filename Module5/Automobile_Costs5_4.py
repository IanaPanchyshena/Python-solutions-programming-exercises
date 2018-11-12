# Automobile_Costs5_4

# Write a program that asks the user to enter
# the monthly costs for the following expenses
# incurred from operating his or her automobile:
# loan payment, insurance, gas, oil, tires, and maintenance.
# The program should then display the total monthly cost of these expenses,
# and the total annual cost of these expenses.


def main():
    loan_payment=float(input('Enter loan payment: '))
    insurance=float(input('Enter insurance: '))
    gas=float(input('Enter gas expenses: '))
    oil=float(input('Enter oil expenses: '))
    tires=float(input('Enter tires expenses: '))
    maintenance=float(input('Enter maintenance expenses: '))

    monthly_cost=get_monthly_cost(loan_payment,insurance,gas,oil,tires,maintenance)
    print('Monthly cost is: $', monthly_cost)

    annual_cost=get_annual_cost(monthly_cost)
    print('Annual cost is: $', annual_cost)
    
def get_monthly_cost(loan_payment,insurance,gas,oil,tires,maintenance):
    return loan_payment+insurance+gas+oil+tires+maintenance

def get_annual_cost(monthly_cost):
    return monthly_cost*12
    
main()
