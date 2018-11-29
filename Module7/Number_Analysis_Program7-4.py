# Number_Analysis_Program7-4
# Design a program that asks the user to enter a series of 20 numbers.
# The program should store the numbers in a list
# then display the following data:
# The lowest number in the list
# The highest number in the list
# The total of the numbers in the list
# The average of the numbers in the list


def main():
    list_number=[]
    total=0
    for number in range (20):
        number=float(input('Enter the number: '+format(number+1)+' '))
        list_number.append(number)
        total+=number
        average=total/len(list_number)

    print('The lowest number in the list',min(list_number))
    print('The highest number in the list',max(list_number))
    print('The total of the numbers in the list', format(total,',.2f'))
    print('The average of the numbers in the list',format(average,',.2f'))

main()

    
        
