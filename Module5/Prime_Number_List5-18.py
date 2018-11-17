# Prime_Number_List5-18
# This exercise assumes that you have already written the is_prime function
# in Programming Exercise 17.
# Write another program that displays all of the prime numbers from 1 to 100.
# The program should have a loop that calls the is_prime function.


def is_prime(number):
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
    for number in range (1,101):
        if is_prime(number):
            print(number,end=' ')
    
        


main()
