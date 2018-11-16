# Prime_Numbers5_17
# A prime number is a number that is only evenly divisible by itself and 1.
# For example, the number 5 is prime because it can only be evenly
# divided by 1 and 5.
# The number 6, however, is not prime because it can be divided
# evenly by 1, 2, 3, and 6.

# Write a Boolean function named is_prime
# which takes an integer as an argument and returns true
# if the argument is a prime number, or false otherwise.

# Use the function in a program that prompts the user to enter a number
# then displays a message indicating whether the number is prime.

# Tip:
# Recall that the % operator divides one number by another
# and returns the remainder of the division.
# In an expression such as num1 % num2,
# the % operator will return 0 if num1 is evenly divisible by num2.
    
def isPrime(number):
    even =0
    if number<=1:
        return False
    for currentNumber in range(1,number+1):
       if number%currentNumber==0:
           even=even+1
           if even>2:
               return False
    return True
def main():
    userNumber=int(input('Enter the number: '))
    if isPrime(userNumber):
        print(userNumber,'is a prime number')
    else:
        print(userNumber,'is NOT a prime number')
        


main()
