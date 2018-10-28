#Money_Counting_Game3_10
# That gets the user to enter the number of coins
# required to make exactly one dollar.
# The program should prompt the user to enter the number
# of pennies, nickels, dimes, and quarters.
# If the total value of the coins entered is equal to one dollar,
# the program should congratulate the user for winning the game.
# Otherwise, the program should display a message indicating whether
# the amount entered was more than or less than one dollar.

def main():
    pennies=int(input('Enter the number of pennies: '))
    nickels=int(input('Enter the number of nickels: '))
    dimes=int(input('Enter the number of dimes: '))
    quaters=int(input('Enter the number of quaters: '))

    pennies=pennies*1
    nickels=nickels*5
    dimes=dimes*10
    quaters=quaters*25

    dollar=pennies+nickels+dimes+quaters
    
    if dollar==100:
        print('Congratulations - you entered exact amount for one dollar! ')
    elif dollar>100:
        print('The amount was enetered more than one dollar...Try again! ')
    else:
       print('The amount was entered less than one dollar ...Try again! ')
        
main()
