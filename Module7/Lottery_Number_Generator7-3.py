# Lottery_Number_Generator2-7
# Design a program that generates a seven-digit lottery number.
# The program should generate seven random numbers,
# each in the range of 0 through 9, and assign each number to a list element.
# Then write another loop that displays the contents of the list.


def main():
    import random
    numbers=[0]*7
    for index in range(7):
        numbers[index]=random.randint(0,9)
    print('Here are your lottery numbers: ')
    for index in range(7):
        print(numbers[index],end='')
    print()

main()
