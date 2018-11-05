# Calculating the Factorial of a Number
# In mathematics, the notation n! represents the factorial
# of the nonnegative integer n.
# The factorial of n is the product of all the nonnegative integers from 1 to n.
# For example, 7!=1×2×3×4×5×6×7=5,040 and 4!=1×2×3×4=24
# Write a program that lets the user
# enter a nonnegative integer then uses a loop to calculate
# the factorial of that number. Display the factorial.

def main():
    integer=0
    while integer<1:
        integer=int(input('Enter a nonnegative integer: '))
    factorial=1

    for number in range(1,integer+1):
        factorial=factorial*number

    print('Factorial of',integer,'is',factorial)


main()
