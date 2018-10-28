# Compound Interest2_14

def main():
    # ask user to enter and assign to:
    # originaly_deposit
    # annual_rate
    # compound_per_year
    # years_left
    originaly_deposit=float(input('Enter originaly deposit amount of money $ '))
    annual_rate=float(input('Enter originaly deposit annual rate % '))
    compound_per_year=float(input('Enter times compound per year: '))
    years_left=float(input('Enter number of years account will left money '))

    # calculate amount_after by formula.
    # A=P(1/rn)**nt
    amount_after=originaly_deposit*(1+annual_rate/compound_per_year)**(compound_per_year*years_left)

    # display result.
    print('Amount of money in the account after the specified number of years $',format(amount_after,'.2f'),sep='')
main()
