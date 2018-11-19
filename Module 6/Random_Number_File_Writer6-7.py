# Random_Number_File_Writer6-7

# Write a program that writes a series of random numbers to a file.
# Each random number should be in the range of 1 through 500.
# The application should let the user
# specify how many random numbers the file will hold.

import random

def main():
    num = int(input('How many numbers in range from 1 to 500 do you want to save: '))
    randomFile = open('randomNumber.txt','w')
    
    for line in range(1, num+1):
        number = random.randint(1, 500)
        randomFile.write(str(number)+'\n')
        print(number)

    randomFile.close()

main()
