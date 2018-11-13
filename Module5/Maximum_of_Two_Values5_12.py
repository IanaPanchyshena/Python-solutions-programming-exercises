# Maximum_of_Two_Values5_12

# Write a function named max that accepts two integer values as arguments
# and returns the value that is the greater of the two.
# For example, if 7 and 12 are passed as arguments to the function,
# the function should return 12.
# Use the function in a program that prompts the user to enter two integer values.
# The program should display the value that is the greater of the two.


def main():
    number1=int(input('Enter the number1: '))
    number2=int(input('Enter the number2: '))
    max(number1,number2)
    print('The max number is', max(number1,number2))


def max(number1,number2):
    if number1>number2:
        return number1
    else:
        return number2

main()
