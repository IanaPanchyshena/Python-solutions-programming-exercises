# Sum of Numbers4_8
# Write a program with a loop that asks the user to enter
# a series of positive numbers.
# The user should enter a negative number to signal the end of the series.
# After all the positive numbers have been entered,
# the program should display their sum. 


def main():
    total=0
    pos_num=0
    while pos_num>-1:
        total+=pos_num
        pos_num=float(input('Enter a positive numbers or negative to quit: '))

    print('The sum all numbers is: ',total)
        

main()
