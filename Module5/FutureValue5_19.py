# FutureValue5_19
#F=P(1+i)t
#The terms in the formula are:
#F is the future value of the account after the specified time period.
#P is the present value of the account.
#i is the monthly interest rate.
#t is the number of months.

#Write a program that prompts the user to enter the account’s present value,
#monthly interest rate, and the number of months that the money will be left
#in the account. The program should pass these values to a function
#that returns the future value of the account,
#after the specified number of months.
#The program should display the account’s future value


def main():
    p=float(input('Account’s present value:$'))
    i=float(input('Monthly interest rate:%'))
    t=float(input('The number of months that the money will be left'+
                  'in the account: '))
    f=future_value(p,i,t)
    print('Future value is $',format(f,'.2f'),sep='')

def future_value(p,i,t):
    f=p*(1+i)**t
    return f
    

main()
    
