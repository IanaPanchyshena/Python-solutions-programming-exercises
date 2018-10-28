# Roman Numerals3_4

# Write a program that prompts the user to enter
# a number within the range of 1 through 10.
# The program should display the Roman numeral version of that number.
# If the number is outside the range of 1 through 10, the program should display an error message.
# The following table shows the Roman numerals for the numbers 1 through 10:
# NumberRoman Numeral

def main():
# start program
    I=1
    II=2
    III=3
    IV=4
    V=5
    VI=6
    VII=7
    VIII=8
    IX=9
    X=10
    number=int(input('Enter number within the range of 1 through 10: '))
    if number ==1:
        print('Roman Numeral is I')
    elif number==2:
        print('Roman Numeral is II')
    elif number==3:
        print('Roman Numeral is III')
    elif number==4:
        print('Roman Numeral is IV')    
    elif number==5:
        print('Roman Numeral is V')
    elif number==6:
        print('Roman Numeral is VI')
    elif number==7:
        print('Roman Numeral is VII')
    elif number==8:
        print('Roman Numeral is VIII')
    elif number==9:
        print('Roman Numeral is IX')
    elif number==10:
        print('Roman Numeral is X')
    else:
        print('error message')

main()
# end program
