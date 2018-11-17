# Random_number5_20

# Write a program that generates a random number in the range of 1 through 100,
# and asks the user to guess what the number is.
# If the user’s guess is higher than the random number,
# the program should display “Too high, try again.”
# If the user’s guess is lower than the random number,
# the program should display “Too low, try again.”
# If the user guesses the number, the application should congratulate
# the user and generate a new random number so the game can start over.

import random
def main():
   
    user_number=int
    while user_number!='':
        number=random.randrange(1,100)
        user_number=int(input('Enter the number '))
        
        if number>=user_number:
            print('Too low,try again,the number was',number)
        elif number<=user_number:
            print('Too high, try again,the number was',number)
        elif number==number_user:
            print('Congratulations! The number was',number)
        
main()
