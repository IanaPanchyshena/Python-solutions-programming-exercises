# Math_Quiz5_11

# Write a program that gives simple math quizzes.
# The program should display two random numbers that are to be added,
# such as: 247 + 129
# The program should allow the student to enter the answer.
# If the answer is correct, a message of congratulations should be displayed.
# If the answer is incorrect,
# a message showing the correct answer should be displayed.


import random
MIN=1
MAX=1000

def main():
    keep_going='y'
    while keep_going=='y' or keep_going=='Y':

        number1=random.randint(MIN,MAX)
        number2=random.randint(MIN,MAX)
        print(number1,'+',number2)
        answer=int(input('Enter the answer: '))
        
        if answer == math_quiz(number1,number2):
            print('Congratulations! The answer',answer,'is correct!')
        else:
            print('Nope! The answer is',math_quiz(number1,number2))

        keep_going=input('Try again (y=yes):')

def math_quiz(number1,number2):
    return number1+number2
        
main()
