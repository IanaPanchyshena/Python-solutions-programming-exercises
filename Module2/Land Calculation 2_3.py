#Land Calculation 2_3

def main():
    one_acre=43.560

    #ask user to enter total square feet
    total_squareFeet=float(input('Enter totta in square feet '))

    #calculate number the number of acres
    total_acres=total_squareFeet/43560
    # print result
    print('Number the number of acres:',format(total_acres,'.2f'),'acre')

main()
