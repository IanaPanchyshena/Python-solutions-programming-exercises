# Miles-per-Gallon 2_7

def main():
    # get number of miles driven
    # get the gallons of gas used
    miles_driven=float(input('Enter miles of driven '))
    gas_used=float(input('Enter the gallons of gas used '))

    # calculate MPG(miles per gallon) by formula
    # mpg=miles dfiven/gallons of gas used
    mpg=miles_driven/gas_used

    # display result
    print('Miles per gallon is',format(mpg,'.2f'))

main()
