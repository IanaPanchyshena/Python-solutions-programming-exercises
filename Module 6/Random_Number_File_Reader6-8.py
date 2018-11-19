# Random_Number_File_Reader6-8

# This exercise assumes you have completed Programming Exercise 7,
# Random Number File Writer.
# Write another program that reads the random numbers from the file,
# displays the numbers, then displays the following data:
# The total of the numbers
# The number of random numbers read from the file

def main():
    file = open('randomNumber.txt','r')
    line = file.readline().rstrip('\n')
    total = 0
    counter = 0

    while line != '':
        total += int(line)
        counter += 1
        print(line)
        line = file.readline().rstrip('\n')

    print()
    print('The total is', total)
    print('The amount of random numbers is', counter)


main()
